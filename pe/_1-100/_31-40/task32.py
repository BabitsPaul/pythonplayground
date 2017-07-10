def pandigital(v=set(range(1, 10))):
    c = []

    pandigital_l(v, 0, c)

    return c


def pandigital_l(v, l, c):
    for i in v:
        v.remove(i)

        pandigital_l(v, l * 10 + i, c)
        pandigital_r(v, l, i, c)

        v.add(i)


def pandigital_r(v, l, r, c):
    for i in v:
        v.remove(i)

        pandigital_r(v, l, r * 10 + i, c)
        pandigital_t(v, l, r, i, c)

        v.add(i)


def pandigital_t(v, l, r, t, c):
    if v:
        for i in v:
            v.remove(i)

            pandigital_t(v, l, r, t * 10 + i, c)

            v.add(i)
    elif l * r == t:
        print("{} * {} = {}".format(l, r, t))
        c.append((l, r, t))


def test():
    t = pandigital(set([1, 2, 3, 4, 5, 6, 7, 8, 9]))
    tmp = sorted(set([p[2] for p in t]))
    print(tmp)
    print(sum(tmp))


test()
