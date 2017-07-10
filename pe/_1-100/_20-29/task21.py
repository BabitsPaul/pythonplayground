def divisor_sum(n):
    return sum([x for x in range(1, n) if n % x == 0])


print(sum([x for x in range(1, 10000) if x == divisor_sum(divisor_sum(x)) and divisor_sum(x) != x]))
