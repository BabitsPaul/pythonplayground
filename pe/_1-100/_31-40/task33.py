from util.fact import gcd


def interesting():
    for i in range(10, 100):
        for j in range(i + 1, 100):
            if i % 10 == 0 or i % 11 == 0 or j % 10 == 0 or j % 11 == 0:
                continue

            a = i % 10 / (j // 10)
            b = i // 10 / (j % 10)
            if a == i / j and i // 10 == j % 10 or \
                b == i / j and i % 10 == j // 10:
                yield (i, j)


q = 1
p = 1

for i in interesting():
    q *= i[0]
    p *= i[1]

print(p / gcd(q, p))