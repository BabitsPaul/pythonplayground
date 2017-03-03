def modmuladd(ls, x, y, k):
    result = []

    # create tuples of indices and values
    indices = zip(ls, range(0, len(ls)))

    # split up into congruence classes
    congruence_cls = [[] for i in range(0, k)]
    for p in indices:
        congruence_cls[p[0] % k].append(p)

    for n in range(0, k):
        # congruence class to match addition
        if n < x:
            m = x - n
        elif n == x:
            m = 0
        else:
            m = x + k - n

        # check if congruence class matches for multiplication
        if (n * m) % k != y or len(congruence_cls[m]) == 0:
            continue    # no matching congruence class

        # add matching tuple to result
        result += [(a, b) for a in congruence_cls[n] for b in congruence_cls[m] if a[1] <= b[1]]
        result += [(a, b) for a in congruence_cls[m] for b in congruence_cls[n] if a[1] <= b[1]]

    # sort result such according to indices of first and second element, remove duplicates
    sorted_res = sorted(sorted(set(result), key=lambda p: p[1][1]), key=lambda p: p[0][1])

    # remove indices from result-set
    return [(p[0][0], p[1][0]) for p in sorted_res]


def modmuladdct(ls, x, y, k):
    result = 0

    # split up into congruence classes
    congruence_class = {}
    for v in ls:
        if v % k not in congruence_class:
            congruence_class[(v % k)] = [v]
        else:
            congruence_class[v % k].append(v)

    for n in congruence_class.keys():
        # congruence class to match addition
        m = (x - n + k) % k

        # check if congruence class matches for multiplication
        if (n * m % k != y) or len(congruence_class[m]) == 0:
            continue    # no matching congruence class

        # total number of pairs that will be built
        result += len(congruence_class[n]) * len(congruence_class[m])

    return result // 2


print(modmuladdct([1, 2, 3, 2, 1], 1, 0, 2))
