def inc(s):
    # convert to number
    v = [ord(x) - ord('0') if x.isdigit() else 10 + ord(x) - ord('A') for x in s]
    p = [36 ** x for x in range(0, len(s)).__reversed__()]
    t = sum([a * b for (a, b) in zip(v, p)])

    # increment
    t += 1

    # restore original number
    r = []
    while t != 0:
        r.append(t % 36)
        t //= 36
    r.reverse()

    return "".join([chr(t + ord('A') - 10) if t > 9 else chr(t + ord('0')) for t in r])


def inc_special(s):
    return inc(s[:-2]) + s[-2:]


print(inc_special("AX0034"))
