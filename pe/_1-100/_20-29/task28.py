def spiral_diagonal_sum(n):
    sum = 1

    for i in range(3, n + 1, 2):
        sum += 4 * i ** 2 - (i - 1) * 6

    return sum


print(spiral_diagonal_sum(1001))
