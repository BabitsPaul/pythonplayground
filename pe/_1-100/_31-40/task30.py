def solutions(n):
    # exclude 1 as it's not a sum
    return [i for i in range(2, 9**n * n) if sum([int(x) ** n for x in str(i)]) == i]


print(sum(solutions(5)))
