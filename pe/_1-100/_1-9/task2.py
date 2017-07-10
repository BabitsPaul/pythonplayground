def fib_to_n(n):
    first = 0
    second = 1

    while first < n:
        yield first

        tmp = first + second
        first = second
        second = tmp


def filter_even(n):
    return sum([x for x in fib_to_n(n) if x % 2 == 0])


print(filter_even(4000000))