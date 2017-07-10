from math import ceil, floor

bits = [(1 << x, x) for x in range(0, 32)]


def max_one_bit(n):
    return max(bits, key=lambda p: 0 if p[0] & n == 0 else p[1])[1]


def binary_palindrome(n):
    b = [0 if n & (1 << _b)  == 0 else 1 for _b in range(max_one_bit(n), -1, -1)]

    for l, u in zip(range(0, int(ceil(len(b) / 2)) + 1), range(len(b) - 1, int(floor(len(b) / 2)) - 1, -1)):
        if b[l] != b[u]:
            return False

    print(b)
    return True


def list_b10_palindromes(exp):
    return _list_b10_palindromes(exp) + _list_b10_palindromes(exp - 1)


def _list_b10_palindromes(exp):
    if exp == 1:
        return list(range(0, 10))
    if exp == 2:
        return [x * 11 for x in range(1, 10)]

    res = _list_b10_palindromes(exp - 2)
    tmp = [x * 10 for x in res]

    for i in range(1, 10):
        res += [x + i + i * 10 ** (exp - 1) for x in tmp]

    return res


def list_b10_b2_palindromes(exp=6):
    return [x for x in list_b10_palindromes(exp) if binary_palindrome(x)]


t = list_b10_palindromes(6)
print(t)
print(len(t))
tmp = list_b10_b2_palindromes()
print(tmp)
print(sum(tmp))
