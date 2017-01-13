class BstNode:
    def __init__(self, value, left = None, right = None):
        self.value = value
        self.right = right
        self.left = left

    def shallow_clone(self):
        return BstNode(self.value, self.left, self.right)

    def print(self, indent):
        print(indent, self.value, "\t", self)
        nindent = indent + "\t"

        if not self.left is None:
            self.left.print(nindent)
        else:
            print(nindent, "none")

        if not self.right is None:
            self.right.print(nindent)
        else:
            print(nindent, "none")


def bst_copy(bst):
    if bst is None:
        return None

    stack = list()
    root = bst.shallow_clone()
    stack.append(root)

    while stack:
        n = stack.pop()

        if not n.left is None:
            n.left = n.left.shallow_clone()
            stack.append(n.left)

        if not n.right is None:
            n.right = n.right.shallow_clone()
            stack.append(n.right)

    return root

root = BstNode(3,
               BstNode(4,
                       BstNode(5),
                       BstNode(2)),
               BstNode(155,
                       BstNode(7),
                       BstNode(9)))

root.print("")
print("\n\n")
bst_copy(root).print("")
