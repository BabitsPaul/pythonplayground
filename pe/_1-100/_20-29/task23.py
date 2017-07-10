from util.fact import divisors
import itertools


def list_abundant_numbers(n):
    return [x for x in range(12, n) if sum(divisors(x)) > x]


def task23(n):
    abundant_numbers = list_abundant_numbers(n)
    sum_abundant_numbers = [x[0] + x[1] for x in itertools.product(abundant_numbers, abundant_numbers)]

    return sum(set(range(1, n)).difference(sum_abundant_numbers))


print(task23(28123))
