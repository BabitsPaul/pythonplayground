def shirt(c, s):
    if c.isalpha():
        if c.isupper():
            return chr((ord(c) - ord('A') + s) % 26 + ord('A'))
        else:
            return chr((ord(c) - ord('a') + s) % 26 + ord('a'))
    else:
        return c


def moving_shift(s, shift):
    tmp = zip(s, range(shift, shift + len(s) + 1))
    trans = [shirt(p[0], p[1]) for p in tmp]
    return ''.join(trans)


def demoving_shift(s, shift):
    tmp = zip(s, range(shift, shift + len(s) + 1))
    trans = [shirt(p[0], -p[1]) for p in tmp]
    return ''.join(trans)


print(demoving_shift(moving_shift("Hello, World aslodgij eogi asdg asod jgjalskd ggsdgas gdlk!!!", 1), 1))
