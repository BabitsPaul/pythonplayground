# longest increasing sequence


def lis(seq):
    max_len = [0 for x in range(0, 9)]
    result = list()

    for digit in [ord(d) - ord('0') for d in seq]:
        max_len[digit] = max(max_len[0:digit]) + 1
        result.append(max_len[digit])

    return result


print(lis("1531"))
