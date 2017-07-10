def div_1_n(n):
    res = 1

    divisors = []

    for d in range(2, n):
        tmp = d

        if res % d == 0:
            continue

        for div in divisors:
            if tmp % div == 0:
                tmp = int(tmp / div)

        divisors.append(tmp)
        res *= tmp

    return res


print(div_1_n(20))
