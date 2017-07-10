def distinct_powers(a_max, b_max):
    res = set()

    for a in range(2, a_max + 1):
        for b in range(2, b_max + 1):
            res.add(a ** b)

    return len(res)


print(distinct_powers(100, 100))
