def sum_square_dif(n):
    sqr_of_sums = sum(range(1, n + 1)) ** 2
    sum_of_sqrs = sum([x * x for x in range(1, n + 1)])

    return sqr_of_sums - sum_of_sqrs


print(sum_square_dif(100))
