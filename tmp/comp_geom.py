import numpy
from random import randint
from PIL import Image, ImageDraw    # required for draw_convex_hull (only required for drawing-part)

# a.)
# uses the shoelace-formula to find the area
# of the presented polygon


def polygon_area(poly):
    tmp = 0

    tmp += sum(map(lambda a, b: a[0]*b[1], poly, poly[1:]))
    tmp -= sum(map(lambda a, b: a[0]*b[1], poly[1:], poly))
    tmp += poly[len(poly) - 1][0] * poly[0][1]
    tmp -= poly[0][0] * poly[len(poly) - 1][1]

    return abs(tmp) / 2


# b1.)

# result = 0: triangle has no area
# result < 0: points are counter clockwise oriented
# result > 0: points are clockwise oriented
def area(tri):
    return 0.5 * numpy.linalg.det(numpy.matrix([[1, 1, 1], [p[0] for p in tri], [p[1] for p in tri]]))


def convex_hull(p):
    # convex hull doesnt differ from input
    if len(p) <= 3:
        return p

    # sort lexicographical
    p = sorted(sorted(p, key=lambda a: a[1]), key=lambda a: a[0])

    l_upper = [p[0], p[1]]

    # create upper boundary of the polygon
    for x in p[2:]:
        l_upper.append(x)
        while len(l_upper) >= 3 and area(l_upper[len(l_upper) - 3:]) < 0:
            l_upper.remove(l_upper[len(l_upper) - 2])

    l_lower = [p[0], p[1]]

    # create lower boundary of the polygon
    for x in p[2:]:
        l_lower.append(x)

        while len(l_lower) >= 3 and area(l_lower[len(l_lower) - 3:]) > 0:
            l_lower.remove(l_lower[len(l_lower) - 2])

    # trim l_lower by elements already present in l_upper to output a proper polygon
    start = 0
    while l_lower[start] == l_upper[start]:
        start += 1

    end = 1
    while l_lower[len(l_lower) - end] == l_upper[len(l_upper) - end]:
        end += 1

    l_lower = l_lower[start:len(l_lower) - end + 1]

    # concat boundaries
    l_lower.reverse()
    l = l_upper + l_lower

    return l


# b2.)
# takes in a polygon as list of points sorted by
# order on the boundary of the polygon - adjacent points in the list
# are adjacent on the polygon-boundary. No other constraints on order
def is_convex_hull(poly):
    # triangles and simpler primitives will always be convex
    if len(poly) <= 3:
        return True

    tmp = poly + poly[0:2]
    h = area(poly[0:3]) < 0

    for i in range(0, len(poly)):
        if (area(tmp[i:i+3]) < 0) != h:
            return False

    return True


# c.)
# expects a polygon as list of points and line as tuple of points lying on the line
def intersects(poly, line):
    if line[0] == line[1]:
        raise ValueError("Cant deduce line from given points")

    # find at least one point that lies "below" and one that lies "above" the line
    above = False
    below = False
    for p in poly:
        if area([p, line[0], line[1]]) < 0:
            above = True

            if below:
                break
        else:
            below = True

            if above:
                break

    return above and below


# test polygon area
print(polygon_area([(0, 0), (1, 0), (1, 1), (0, 1)]))   # test for square
print(polygon_area([(10, 40), (40, 40), (50, 10), (60, 40), (90, 40), (65, 60), (75, 90), (50, 70), (25, 90), (35, 60)])) # star


# test convex hull
# visual output
def draw_convex_hull(pts):
    out = convex_hull(pts)
    print(out)

    # render polygon in image
    im = Image.new('RGBA', (500, 500), (255, 255, 255, 0))
    draw = ImageDraw.Draw(im)
    draw.polygon(out, fill=(255, 255, 255, 255), outline=(0, 0, 0, 0))
    for pt in pts:
        draw.rectangle([(pt[0] - 2, pt[1] - 2), (pt[0] + 2, pt[1] + 2)], fill=(255, 0, 0, 255))
    im.show(title="abc.jpg", command="eog abc.jpg")

# test with random points
draw_convex_hull([(randint(10, 490), randint(10, 490)) for i in range(0, 50)])
# test with a star as input
draw_convex_hull([(10, 40), (40, 40), (50, 10), (60, 40), (90, 40), (65, 60), (75, 90), (50, 70), (25, 90), (35, 60)])


# test is_convex_hull
print("expected: True actual: {}".format(
    is_convex_hull([(10, 40), (50, 10), (90, 40), (75, 90), (25, 90)]) # test convex-hull of the previous input
))
print("expected: False actual: {}".format(
    is_convex_hull([(50, 50), (75, 75), (50, 100), (75, 150)])
))


# test line intersection
def draw_poly_line(poly, line):
    # render polygon in image
    im = Image.new('RGBA', (500, 500), (255, 255, 255, 0))
    draw = ImageDraw.Draw(im)
    draw.polygon(poly, fill=(255, 255, 255, 255), outline=(0, 0, 0, 0))
    draw.line(line, fill=(0, 0, 0, 255))
    im.show(title="abc.jpg", command="eog abc.jpg")

print("expected: True actual: {}".format(
    intersects([(10, 40), (50, 10), (90, 40), (75, 90), (25, 90)], [(75, 10), (75, 100)])
))
draw_poly_line([(10, 40), (50, 10), (90, 40), (75, 90), (25, 90)], [(75, 10), (75, 100)])

print("expected: False actual: {}".format(
    intersects([(0, 0), (2, 0), (2, 2), (0, 2)], [(1, -1), (3, 2)])
))
draw_poly_line([(10, 10), (20, 10), (20, 20), (10, 20)], [(50, 20), (75, 75)])
