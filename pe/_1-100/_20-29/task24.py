from math import factorial


def permutation_lex(of, n):
    of = [x for x in of]
    fact = [factorial(x) for x in range(1, len(of))]

    ind = []
    for f in reversed(fact):
        i = (int(n / f))

        if i * f == n:
            i -= 1

        n -= f * i
        ind.append(i)

        print(f, i, n)

    res = []
    for i in ind[0:len(ind)]:
        res.append(of.pop(i))
    res.append(of[0])

    return res


print(permutation_lex(range(0, 10), 1000000))
