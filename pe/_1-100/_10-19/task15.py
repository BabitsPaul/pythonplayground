nodes = {}


def grid_paths(n, p=(0, 0), indent=""):
    if p in nodes:
        return nodes[p]

    res = 0

    if p[0] < n:
        res += grid_paths(n, (p[0] + 1, p[1]), indent + "  ")

    if p[1] < n:
        res += grid_paths(n, (p[0], p[1] + 1), indent + "  ")

    if res == 0:
        res = 1

    nodes[p] = res

    print(indent, p, res)
    return res


print(grid_paths(20))
