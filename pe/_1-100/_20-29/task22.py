def load_names():
    with open("../../names.txt") as file:
        tmp = file.read().split(",")

        file.close()

        return [x.replace("\"", "") for x in tmp]


def namescore(n):
    sum

    return 0


def score():
    names = sorted(load_names())

    return sum([x[0] * x[1] for x in \
            zip([sum([ord(c) - ord('A') + 1 for c in n]) for n in names], \
            range(1, len(names) + 1))])


print(score())
