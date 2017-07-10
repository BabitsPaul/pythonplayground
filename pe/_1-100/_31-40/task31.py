# assume v sorted descending
def change(p, v, i=0):
    if i == len(v):
        return 1 if p == 0 else 0

    return sum([change(p - v[i] * x, v, i + 1) for x in range(0, p // v[i] + 1)])


print(change(200, [200, 100, 50, 20, 10, 5, 2, 1]))