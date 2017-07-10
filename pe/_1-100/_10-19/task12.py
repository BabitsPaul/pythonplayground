from util.lp import list_prod
from util.soe import sieve_of_eratosthenes

from util.fact import factors


def triangular_numbers(upper, i=1, j=2):
    while j < upper:
        yield i

        i += j
        j += 1


def div_ct(n, primes):
    fact = factors(n, primes)
    divs = list_prod([x + 1 for x in fact.values()])
    print(n, divs, fact)

    return divs


def search_div_num(n):
    primes = sieve_of_eratosthenes(n * 20)

    for i in triangular_numbers(1000000):
        if div_ct(i, primes) >= n:
            return i


print(search_div_num(500))
