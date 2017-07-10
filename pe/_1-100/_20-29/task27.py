from util.soe import prime_generator
from math import gcd


def num_iter(start, step):
    ct = start

    while True:
        yield ct

        ct += step


def max_coefficients():
    max_c = (0, 0, 0)
    primes_iter = prime_generator()

    # 168 primes in the range 0 - 1001
    b_range = [next(primes_iter) for i in range(0, 168)]

    primes = list(b_range)

    for a in range(0, 1000):
        for b in b_range:
            # ignore value as it can't yield any result
            if gcd(a, b) != 1 and abs(gcd(a, b)) <= max_c[2]:
                continue

            # print("Testing ", (a, b))

            # iterate over all possible combinations
            for p in [(-a, -b), (-a, b), (a, -b), (a, b)]:
                for n in num_iter(0, 1):
                    h = n * n + n * p[0] + p[1]

                    # expand prime-list, if necessary
                    if h > primes[len(primes) - 1]:
                        print("Expanding prime-list")
                        print("Current maximum prime ", primes[len(primes) - 1])

                        for i in range(0, 1000):
                            primes.append(next(primes_iter))

                    if h not in primes:
                        if max_c[2] < n:
                            max_c = (a, b, n)
                            print("Candidate found ", max_c)

                        break

    print("Solution ", max_c)
    return max_c[0] * max_c[1]

print(max_coefficients())
