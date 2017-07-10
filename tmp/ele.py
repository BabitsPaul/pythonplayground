def decode(n, c):
    return ((n & (1 << i)) != 0 for i in range(0, c))


def testA(n):
    a, b, c, d = decode(n, 4)

    return not (a and (b or d and (c or not a)))


def testB(n):
    a, b, c, d = decode(n, 4)

    return not a or not b and (not d or not c and a)


def testC(n):
    a, b, c, d = decode(n, 4)

    return (not a) or not (b or (d and c))


def test_d(n):
    a, b, c, d, e, f = decode(n, 6)

    return (not ((a or b) and c)) and (d or e) and f


def test_e(n):
    a, b, c, d, e, f = decode(n, 6)

    return not ((a or b) and c or (not d and not e) or not f)


def test_f(n):
    a, b, c, d, e, f = decode(n, 6)

    return not not (not (not (not a and not b) and c) and not (not (d and f) and not (e and f)))


def test_g(n):
    a, b, c = decode(n, 3)

    return ((not a) and (not b) and c) ^ (((not b) or c) and a)


def test_h(n):
    a, b, c = decode(n, 3)

    return ((not b) and (a or c)) or (a and b and c)


def test_i(n):
    a, b, c, d = decode(n, 4)

    return not (a and b) or c and d


def test_j(n):
    a, b, c, d = decode(n, 4)

    return not (a and b and not (c and d))


def test(a, b, n):
    print("Starting test")

    for i in range(0, 1 << n):
        if a(i) != b(i):
            print("failed for ", bin(i))

    print("Completed")


test(test_i, test_j, 4)
