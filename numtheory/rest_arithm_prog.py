"""
Input: 
An arithmetic progression, all elements where all numbers were divided by 2
as long as possible:
1 1 3 1 5 = 1 2 3 4 5

Output:
Sum of all elements of the original progression
"""
import random


def restore(l):
    lt = l[:4]

    # the first three elements represent a valid arithmetic progression =>
    # input is already valid arithmetic progression
    if lt[1] - lt[0] == lt[2] - lt[1]:
        return lt[0], lt[1] - lt[0]

    # numbers alternating even and odd =>
    # either lt[1] and lt[3] correspond to values of original progression or lt[0] and lt[2] =>
    if lt[2] > lt[1]:  # lt[0] was odd originally
        return lt[0], (lt[2] - lt[0]) // 2
    else:
        return lt[1] - (lt[3] - lt[1]) // 2, (lt[3] - lt[1]) // 2


def sum_prog(a0, d, l):
    return a0 * l + (l - 1) * l // 2 * d


# test cases provided in question
def test_user():
    inp = [
        ([1, 1, 3, 1, 5, 3], 21),
        ([1, 1, 1, 1, 1, 1], 6),
        ([3, 3, 3, 3], 12),
        ([3, 5, 1, 3, 1, 1], 21),
        ([21, 27, 33, 39, 45, 51], 216),
        ([37, 15, 23, 1, 9, 1], 117),
        ([1019, 1077, 1135, 1193, 1251, 1309, 1367, 1425, 1483, 1541], 12800),
        ([1103, 2067, 241, 1789, 825, 1511, 343, 1233, 547, 955, 51, 677, 269, 399, 65, 121], 18616),
        ([5, 5, 5, 5, 5], 25),
        ([5, 1, 11, 7, 17], 55)
    ]

    for i in inp:
        a0, d = restore(i[0])
        s = sum_prog(a0, d, len(i[0]))
        original_prog = [a0 + d * i for i in range(0, len(i[0]))]

        print("inp={} original={} a0={} d={} sum={} correct={}".format(i, original_prog, a0, d, s, s == i[1]))


# random testing
def random_seq():
    a0 = random.randint(5, 1000)
    d = random.randint(5, 1000)
    l = random.randint(5, 10)

    reduce = lambda p: p if p % 2 != 0 else reduce(p // 2)

    return [reduce(i) for i in range(a0, a0 + d * l, d)], a0, d, [a0 + d * i for i in range(0, l)]


def test_rnd():
    failure = []

    for i in range(0, 10000):
        inp, a0, d, act = random_seq()
        a0r, dr = restore(inp)

        print("v: {} a0: {}/{} d: {}/{} s: {}/{}/{}".format(a0 // a0r * dr == d, a0, a0r, d, dr, inp,
                                                            [a0r + dr * n for n in range(0, len(inp))], act))

        if a0 // a0r * dr != d:
            failure.append((inp, a0, d, act, a0r, dr))

    print("Errors: ", len(failure))
    if failure:
        print("Failure:")
        for inp, a0, d, act, a0r, dr in failure:
            print("a0: {}/{} d: {}/{} s: {}/{}/{}".format(a0, a0r, d, dr, inp,
                                                                [a0r + dr * n for n in range(0, len(inp))], act))
    else:
        print("all successful")

test_user()
