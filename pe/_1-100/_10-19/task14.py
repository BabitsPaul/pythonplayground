collatz_len = {1: 0}


def collatz_seq(n):
    stack = []
    while n not in collatz_len:
        stack.append(n)

        if n % 2 == 0:
            n = int(n / 2)
        else:
            n = 3 * n + 1

    offs = collatz_len[n]
    for s in reversed(stack):
        offs += 1
        collatz_len[s] = offs

    return offs


def scan_collatz(n):
    m = 0
    m_v = -1

    for i in range(2, n):
        l = collatz_seq(i)

        if l > m:
            m = l
            m_v = i

    return m_v, m

print(scan_collatz(1000000))

# print(scan_collatz(1000))
# for k, v in collatz_len.items():
#    print(k, v)
