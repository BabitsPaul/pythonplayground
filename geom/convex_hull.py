def area(a, b, c):
    return b[0] * c[1] + c[0] * a[1] + a[0] * b[1] - b[0] * a[1] - a[0] * c[1] - c[0] * b[1]


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

                if area(p[i], p[j], p[k]) < 0:
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

print(slow_convex_hull([(4, 5), (2, 3), (7, 8), (1, 3), (3, 3), (5, 3)]))