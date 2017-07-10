from util.soe import sieve_of_eratosthenes

print(983)

# see https://en.wikipedia.org/wiki/Repeating_decimal

# computational:


def full_reptendant_test(n):
    # TODO proper implementation of full-reptendant-test
    return 0


def longest_cycle(n):
    def bound(n, primes):
        return primes[len(primes) - 1] < n

    return max([x for x in sieve_of_eratosthenes(1000, bound) if x % 10 == 1 and full_reptendant_test(x)])

