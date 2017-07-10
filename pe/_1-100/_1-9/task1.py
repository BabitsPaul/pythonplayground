from math import floor


def naive(upper):
    return sum([x for x in range(1, upper) if x % 5 == 0 or x % 3 == 0])


def sum_to_n(n):
    return n * (n + 1) / 2


def efficient(upper):
    upper -= 1

    # -2: ignore 0 (divisible by 3 and 5)
    # - upper / 15: remove duplicates if divisible by 15, divisible by 5 and 3
    return sum_to_n(floor(upper / 5)) * 5 + \
            sum_to_n(floor(upper / 3)) * 3 - \
            sum_to_n(floor(upper / 15)) * 15


def test():
    upper = 1000

    print("Naive: ", naive(upper))
    print("Efficient: ", efficient(upper))

test()