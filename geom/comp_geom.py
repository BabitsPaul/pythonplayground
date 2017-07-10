from PIL import Image, ImageDraw
from random import randint
import numpy
from typing import Callable

#############################################################################
# convex hull
#


# result = 0: triangle has no area
# result < 0: points are counter clockwise oriented
# result > 0: points are clockwise oriented
def area(tri):
    return 0.5 * numpy.linalg.det(numpy.matrix([[1, 1, 1], [p[0] for p in tri], [p[1] for p in tri]]))


# slow convex hull
# chapter 1.1 (6.3.)
def slow_convex_hull(p):
    poly = dict()

    for i in range(0, len(p)):
        for j in range(0, len(p)):
            if i == j:
                continue

            valid = True

            for k in range(0, len(p)):
                if k == i or k == j:
                    continue

                if area((p[i], p[j], p[k])) > 0:
                    valid = False

            if valid:
                poly[p[i]] = p[j]

    tmp = next(poly.values().__iter__())
    v = poly[tmp]
    res = [tmp]

    while v != tmp:
        res.append(v)
        v = poly[v]

    return res


# gift-wrapping algorithm
# wiki: https://en.wikipedia.org/wiki/Gift_wrapping_algorithm
def gift_wrapping(s):
    # TODO sometimes not terminating
    p = []

    point_on_hull = sorted(s, key=lambda a: a[0])[0]
    i = 0

    loop = True
    while loop:
        p.append(point_on_hull)

        endpoint = s[0]

        for j in range(1, len(s)):
            if endpoint == point_on_hull or area((p[i], endpoint, s[j])) < 0:
                endpoint = s[j]

        i += 1
        point_on_hull = endpoint

        # terminate loop if endpoint is reached
        loop = (endpoint != p[0])

    return p


# convex hull
# chapter 1.1 (13.3.)
def convex_hull(p):
    # convex hull doesnt differ from input
    if len(p) <= 3:
        return p

    # sort lexicographical
    p = sorted(sorted(p, key=lambda a: a[1]), key=lambda a: a[0])

    l_upper = [p[0], p[1]]

    for x in p[2:]:
        l_upper.append(x)
        while len(l_upper) >= 3 and area(l_upper[len(l_upper) - 3:]) < 0:
            l_upper.remove(l_upper[len(l_upper) - 2])

    l_lower = [p[0], p[1]]

    for x in p[2:]:
        l_lower.append(x)

        while len(l_lower) >= 3 and area(l_lower[len(l_lower) - 3:]) > 0:
            l_lower.remove(l_lower[len(l_lower) - 2])

    l_lower.reverse()
    l = l_upper + l_lower

    return l


def run_convex_hull():
    # generate set of random points
    pts = [(randint(10, 490), randint(10, 490)) for i in range(0, 50)]
    out = convex_hull(pts)

    # render polygon in image
    im = Image.new('RGBA', (500, 500), (255, 255, 255, 0))
    draw = ImageDraw.Draw(im)
    draw.polygon(out, fill=(255, 255, 255, 255), outline=(0, 0, 0, 0))
    for pt in pts:
        draw.rectangle([(pt[0] - 2, pt[1] - 2), (pt[0] + 2, pt[1] + 2)], fill=(255, 0, 0, 255))
    im.show(title="abc.jpg", command="eog abc.jpg")


################################################################################
# balanced binary tree
#

"""
Provides an AVLTree implementation that inserts elements
ordered by the provided comparator (cmp). Requirements for cmp:
- returns a negative value, if the first argument is "smaller" than the second
- returns 0, if  elements are equal according to the comparison operation
- returns a positive value if the first argument is greater than the second
- must provide total ordering. This means the relationship must be antisymmetric,
  transitive and total
"""


class AVLTree(object):
    def __init__(self, comparator: Callable, vals=[]):
        self.root = None
        self.comparator = comparator

        for v in vals:
            self.insert(v)

    def __iter__(self):
        if self.root is None:
            return
        else:
            return self.root.__iter__()

    def __add__(self, other):
        return self.__copy__().__iadd__(other)

    def __iadd__(self, other):
        for v in other:
            self.insert(v)

        return self

    def __sub__(self, other):
        return self.__copy__().__isub__(other)

    def __isub__(self, other):
        for v in other:
            self.remove(v)

        return self

    def __copy__(self):
        res = AVLTree()
        res.root = self.root.__copy__()

        return res

    def __and__(self, other):
        return self.__copy__().__iand__(other)

    def __iand__(self, other):
        for v in other:
            self.remove(v)

        return self

    def __or__(self, other):
        return self.__add__(other)

    def __ior__(self, other):
        return self.__iand__(other)

    def __xor__(self, other):
        return self.__copy__().__ixor__(other)

    def __ixor__(self, other):
        for v in other:
            if v in self:
                self.remove(v)
            else:
                self.insert(v)

    def __len__(self):
        if self.root is None:
            return 0

        return self.root.len

    def __concat__(self, other):
        return self.__add__(other)

    def __iconcat__(self, other):
        return self.__iadd__(other)

    def __delitem__(self, key):
        return self.remove(key)

    def __getitem__(self, item):
        if self.root is None:
            return None

        return self.root.__getitem__(item)

    def indexof(self, item):
        if self.root is None:
            return -1

        return self.root.indexof(item)

    def insert(self, val):
        if self.root is None:
            self.root = AVLTree.AVLNode(self.comparator, val)
        else:
            self.root.insert(val)

    def remove(self, val):
        if self.root is None:
            return False

        tmp = self.root.len
        self.root = self.root.delete(val)

        return self.root is None or self.root.len + 1 == len

    def range(self, lower, upper):
        if self.root is None:
            return

        self.root.list_sub_tree(lower, upper)

    def __contains__(self, item):
        if self.root is None:
            return False
        else:
            return item in self.root

    def struct_str(self):
        if self.root is None:
            return "None"
        else:
            return self.root.struct_str()

    def min(self):
        if self.root is None:
            return None
        else:
            return self.root.min()

    def max(self):
        if self.root is None:
            return None
        else:
            return self.root.max()

    class AVLNode(object):
        def __init__(self, cmp, value=None, left=None, right=None):
            self.comparator = cmp
            self.left = left  # set values of node
            self.right = right  #
            self.value = value  #
            self.len = 0
            self.height = 0
            self.balance = 0
            self.update_height()  # set height of node
            self.update_balance_factor()  # check balance of tree
            self.update_length()

        def __iter__(self):
            if self.left is not None:
                yield from self.left.__iter__()

            yield self.value

            if self.right is not None:
                yield from self.right.__iter__()

        def __str__(self) -> str:
            return self.value.__str__()

        def __contains__(self, item) -> bool:
            if self.comparator(item, self.value) < 0:
                if self.left is None:
                    return False
                else:
                    return item in self.left
            elif self.comparator(item, self.value) > 0:
                if self.right is None:
                    return False
                else:
                    return item in self.right
            else:
                return True

        def __copy__(self):
            res = AVLTree.AVLNode(self.comparator, self.value)

            res.left = None if self.left is None else self.left.__copy__()
            res.right = None if self.right is None else self.right.__copy__()

            res.height = self.height
            res.balance = self.balance
            res.len = self.len

            return res

        def __eq__(self, other):
            if other is None or type(other) is not AVLTree.AVLNode:
                return False

            if self.value is not other.value:
                return False

            if self.left is not None:
                if not self.left.__eq__(other.left):
                    return False

            if self.right is not None:
                if not self.right.__eq__(other.right):
                    return False

            return True

        def __getitem__(self, item):
            if self.left is None:
                if item == 0:
                    return self.value
                elif self.right is None:
                    return None
                else:
                    return self.right.__getitem__(item - 1)
            elif self.left.len == item:
                return self.value
            elif self.left.len > item:
                return self.left.__getitem__(item)
            else:
                if self.right is None:
                    return None
                else:
                    return self.right.__getitem__(item - self.left.len - 1)

        def indexof(self, item):
            cmp = self.comparator(self.value, item)
            len_left = 0 if self.left is None else self.left.len

            if cmp == 0:
                return 1 + len_left
            elif cmp < 0:
                if self.right is None:
                    return -1
                else:
                    tmp = self.right.indexof(item)

                    if tmp == -1:
                        return -1
                    else:
                        return tmp + 1 + len_left
            else:
                if self.left is None:
                    return -1
                else:
                    return self.left.indexof(item)

        # balance-factor of the node
        def update_balance_factor(self):
            l = 0 if self.left is None else -self.left.height
            r = 0 if self.right is None else self.right.height

            self.balance = r + l

        # height of the subtree starting at this node
        def update_height(self):
            l = 0 if self.left is None else self.left.height
            r = 0 if self.right is None else self.right.height

            self.height = max(l, r) + 1

        def update_length(self):
            l = 0 if self.left is None else self.left.len
            r = 0 if self.right is None else self.right.len

            self.len = l + r + 1

        def find(self, x):
            cmp = self.comparator(self.value, x)

            if cmp == 0:
                return self
            elif cmp > 0:
                if self.left is None:
                    return None
                else:
                    return self.left.find(x)
            else:
                if self.right is None:
                    return None
                else:
                    return self.right.find(x)

        def insert(self, val) -> bool:
            cmp = self.comparator(self.value, val)

            if cmp == 0:
                return False
            elif cmp < 0:
                if self.right is None:
                    self.right = AVLTree.AVLNode(self.comparator, val)
                else:
                    self.right.insert(val)
            else:
                if self.left is None:
                    self.left = AVLTree.AVLNode(self.comparator, val)
                else:
                    self.left.insert(val)

            self.rebalance()

        def delete(self, val):
            cmp = self.comparator(self.value, val)

            if cmp == 0:
                if self.left is None or self.right is None:
                    # just replace this node by the not-none child if available or none else
                    return self.left if self.right is None else self.right
                else:
                    # search for the minimum-node of the right subtree
                    node = self.right
                    while node.left is not None:
                        node = node.left

                    # remove value that will be swapped into this node
                    self.right = self.right.delete(node.value)

                    # set minimum of right subtree as value
                    self.value = node.value

                    # rebalance tree
                    self.rebalance()
                    return self
            elif cmp < 0:
                if self.right is not None:
                    self.right = self.right.delete(val)
                    self.rebalance()

                return self
            else:
                if self.left is not None:
                    self.left = self.left.delete(val)
                    self.rebalance()

                return self

        def min(self):
            if self.left is None:
                return self.value
            else:
                return self.left.min()

        def max(self):
            if self.right is None:
                return self.value
            else:
                return self.right.max()

        def list_sub_tree(self, lower, upper):
            if self.comparator(self.value, lower) < 0 or self.comparator(self.value, upper) > 0:
                return

            if self.left is not None:
                self.left.list_sub_tree(lower, upper)

            yield self.value

            if self.right is not None:
                self.right.list_sub_tree(lower, upper)

        def rebalance(self):
            self.update_balance_factor()
            self.update_length()

            def rotate_left(n):
                n.left = AVLTree.AVLNode(self.comparator, n.value, n.left, n.right.left)
                n.value = n.right.value
                n.right = n.right.right

            def rotate_right(n):
                n.right = AVLTree.AVLNode(self.comparator, n.value, n.left.right, n.right)
                n.value = n.left.value
                n.left = n.left.left

            if self.balance < -1 or self.balance > 1:
                if self.balance < 0:
                    # simple balance (left heavy)
                    if self.left.balance <= 0:
                        rotate_right(self)
                    # double balance (left heavy)
                    else:
                        rotate_left(self.left)
                        rotate_right(self)
                elif self.balance > 0:
                    # simple balance (right heavy)
                    if self.right.balance >= 0:
                        rotate_left(self)
                    # double balance (right heavy)
                    else:
                        rotate_right(self.right)
                        rotate_left(self)

            self.update_height()

        def struct_str(self, indent=""):
            tmp = indent + self.__str__() + "\n"

            if self.left is not None:
                tmp += self.left.struct_str(indent + "\t")

            if self.right is not None:
                tmp += self.right.struct_str(indent + "\t")

            return tmp


################################################################################
# line segments
#

def line_segment_intersection(line_segments):
    class Event(object):
        TYPE_SEGMENT_START = 1
        TYPE_SEGMENT_INTERSECTION = 2
        TYPE_SEGMENT_END = 3

        def __init__(self, type, pt, *segments):
            self.type = type
            self.pt = pt
            self.segments = segments

        def get_type(self) -> int:
            return self.type

        def get_point(self) -> tuple:
            return self.pt

        def get_segments(self):
            return self.segments

    class Segment(object):
        # a is higher y-coordinate (display coordinate-system!)
        def __init__(self, a, b):
            if a == b:
                raise ValueError("Points must not be equal")

            self.a = a if a[1] < b[1] else b
            self.b = b if a[1] < b[1] else a

            x = b[0] - a[0]
            y = b[1] - a[1]
            self.length = (x ** 2 + y ** 2) ** 0.5
            self.nvec = x / self.length, y / self.length

        def get_a(self):
            return self.a

        def get_b(self):
            return self.b

        # returns x for the specified y coordinate, or the y-range
        # covered by the segment doesnt contain y
        def interpolate(self, y):
            # solve self.a[1] * alpha + (1 - alpha) * self.b[1] = y for alpha:
            # alpha = (y - b.y) / (a.y - b.y)

            # segment is parallel to x-axis => either infinitely many or no point
            if self.a[1] - self.b[1] == 0:
                return None

            alpha = (y - self.b[1]) / (self.a[1] - self.b[1])

            # alpha must lie in range [0, 1], no point on the segment has the specified y-coordinate
            if alpha < 0 or alpha > 1:
                return None

            # interpolate x-coordinate
            return self.a[0] * alpha + (1 - alpha) * self.b[0]

        # returns the normalized vector of this segment (length = 1)
        # this vector is always oriented downwards
        def get_delta(self):
            return self.nvec

        def __repr__(self):
            return "(" + self.a.__str__() + ", " + self.b.__str__() + ")"

    def normalize(ls):
        for i in range(0, len(ls)):
            # order line_segments such that the first point has a higher y-coordinate if possible
            if ls[i][0][1] > ls[i][1][1]:
                ls[i] = ls[i][1], ls[i][0]

        # transform all tuples into segment-objects
        return [Segment(s[0], s[1]) for s in ls]

    # orders events lexicographically by y, x and
    # by type in the following order: START, INTERSECTION, END
    def cmp_evts(a: Event, b: Event) -> int:
        pt_a = a.get_point()
        pt_b = b.get_point()

        if pt_a[1] != pt_b[1]:
            return pt_a[1] - pt_b[1]
        elif pt_a[0] != pt_b[0]:
            return pt_a[0] - pt_b[0]
        else:
            return a.type - b.type

    # TODO error when calculating factors!!!
    def get_intersection(a: Segment, b: Segment):
        # uses cramers rule to solve the equation
        # a.a + t * (a.b - a.a) = b.a + s * (b.b - b.a)
        dx1, dx2 = a.get_b()[0] - a.get_a()[0], b.get_b()[0] - b.get_a()[0]
        dy1, dy2 = a.get_b()[1] - a.get_a()[1], b.get_b()[1] - b.get_a()[1]
        dxh = b.get_a()[0] - a.get_a()[0]
        dyh = b.get_a()[1] - a.get_a()[1]

        base = dx1 * dy2 - dx2 * dy1

        # line segments are parallel
        if base == 0:
            return None

        s = (dxh * dy2 - dx2 * dyh) / base
        t = -(dx1 * dyh - dxh * dy1) / base

        # s and t must be in range [0, 1]
        # if s < 0 or s > 1 or t < 0 or t > 1:
        #    return None

        # interpolate point based on given factors
        return a.get_a()[0] + s * dx1, a.get_a()[1] + t * dy1

    # returns the index i in the list where
    # i is maximum such that l[i] <= v or i = -1, if v < l[0]
    def get_lower_index(ls, v, cmp):
        l, u = 0, len(ls) - 1

        while l < u:
            mid = (l + u) // 2
            c = cmp(ls[mid], v)

            if c < 0:
                l = mid + 1
            elif c > 0:
                u = mid - 1
            else:
                return mid

        # assert that the result is within bounds
        return u

    def gen_cmp_seg(y: int) -> Callable[[Segment, Segment], int]:
        def cmp_seg(a: Segment, b: Segment):
            # if a failure occurs here this indicates that a segment is in the
            # status that shouldn't be there (inserted prematurely, or failed removal)
            tmp = a.interpolate(y) - b.interpolate(y)

            if tmp != 0:
                return tmp

            return b.get_delta()[0] - a.get_delta()[0]

        return cmp_seg

    # normalize line-segments
    line_segments = normalize(line_segments)
    # enqueue all linestarts/-ends
    queue = AVLTree(cmp_evts, list(map(lambda s: Event(Event.TYPE_SEGMENT_START, s.get_a(), s), line_segments)) +
                    list(map(lambda s: Event(Event.TYPE_SEGMENT_END, s.get_b(), s), line_segments)))
    status = []  # contains segment ordered by current neighboring and orientation

    while queue:
        # pop next value from the queue
        e = queue.min()
        queue.remove(e)

        print("New event: type=", e.get_type(), " point=", e.get_point())

        if e.get_type() == Event.TYPE_SEGMENT_START:
            # insert segment according to intersections
            seg = e.get_segments()[0]
            ind = get_lower_index(status, seg, gen_cmp_seg(seg.get_a()[1])) + 1
            status.insert(ind, seg)

            # check for intersections with neighboring segments
            if ind != 0:
                intersection = get_intersection(seg, status[ind - 1])

                if intersection is not None:
                    queue.insert(Event(Event.TYPE_SEGMENT_INTERSECTION, intersection, seg, status[ind - 1]))

            if ind != len(status) - 1:
                intersection = get_intersection(seg, status[ind + 1])

                if intersection is not None:
                    queue.insert(Event(Event.TYPE_SEGMENT_INTERSECTION, intersection, seg, status[ind + 1]))
        elif e.get_type() == Event.TYPE_SEGMENT_END:
            seg = e.get_segments()[0]
            status.pop(get_lower_index(status, seg, gen_cmp_seg(seg.get_b()[1])))  # remove segment from status
        else:   # Event.TYPE_SEGMENT_INTERSECTION
            seg = e.get_segments()[0]
            pt = e.get_point()

            # search the section of segments in the status sharing this intersection-point
            l = u = get_lower_index(status, seg, gen_cmp_seg(pt[1]))

            while l > -1 and status[l].interpolate(pt[1]) == pt[0]:
                l -= 1
            l += 1

            while u < len(status) and status[u].interpolate(pt[1]) == pt[0]:
                u += 1
            u -= 1

            # report intersection
            print("Intersection at", pt, " for segments: ", status[l:u + 1])

            # reverse order of all lines in the intersection
            status[l:u + 1] = status[l:u + 1][::-1]


def run_line_segmentation():
    line_segment_intersection([((2, 4), (2, 0)), ((0, 0), (4, 10))])

run_line_segmentation()
