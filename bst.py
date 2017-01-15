class BstNode:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.right = right
        self.left = left

    def shallow_clone(self):
        return BstNode(self.value, self.left, self.right)

    def print(self, indent):
        print(indent, self.value, "\t", self)
        nindent = indent + "\t"

        if self.left is not None:
            self.left.print(nindent)
        else:
            print(nindent, "none")

        if self.right is not None:
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

        if n.left is not None:
            n.left = n.left.shallow_clone()
            stack.append(n.left)

        if n.right is not None:
            n.right = n.right.shallow_clone()
            stack.append(n.right)

    return root


tree = BstNode(3,
               BstNode(4,
                       BstNode(5),
                       BstNode(2)),
               BstNode(155,
                       BstNode(7),
                       BstNode(9)))

tree.print("")
print("\n\n")
bst_copy(tree).print("")
