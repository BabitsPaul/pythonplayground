from math import floor, log

# doesn't handle special cases like NaN, infinity, etc...

def get_exp(n):
    return n >> 23 & 0xFF


def get_sign(n):
    return n >> 31


def get_mantissa(n):
    return n & 0x7FFFFF


def get_mantissa_decimal(n):
    mantissa = get_mantissa(n)
    return [(1 << 23 - i) ** (-1) if mantissa & (1 << i) != 0 else 0 for i in range(22, -1, -1)]


def to_float(n, o=True):
    sign = get_sign(n)
    exp = get_exp(n)
    mantissa = get_mantissa(n)
    mantissa_abs = get_mantissa_decimal(n)
    res = (-1 if sign == 1 else 1) * (sum(mantissa_abs) + 1) * 2 ** (exp - 127)

    if o:
        print("===============================================")
        print("inp= ", hex(n))
        print("sign= ", sign, " / ", '-' if sign == 1 else '')
        print("exp= ", exp)
        print("mantissa= ", bin(mantissa), " / vals= ", mantissa_abs)
        print("mantissa abs= ", sum(mantissa_abs) + 1)
        print("total= ", res)

    return res


def to_ieee_float_bits(n, o=True):
    sign = (n < 0)

    if sign:
        n *= -1

    exp = floor(log(n) / log(2.))
    mantissa = round((n / 2 ** exp - 1) * 2 ** 23) # convert float to int
    res = sign << 31 | (exp + 127) << 23 | mantissa

    if o:
        print("===============================================")
        print("inp= ", n)
        print("sign= ", sign, " / ", '-' if sign == 1 else '')
        print("exp= ", exp)
        print("mantissa= ", mantissa)
        print("total: ", hex(res))

    return res


def mult_ieee_float(a, b, o=True):
    sign = get_sign(a) ^ get_sign(b)
    exp = get_exp(a) + get_exp(b) - 2 * 127
    # add up mantissas and drop overflow
    mantissa = (get_mantissa(a) + get_mantissa(b)) & 0x7FFFFF
    res = sign << 31 | (exp + 127) << 23 | mantissa

    if o:
        print("================================================")
        print("A= ", to_float(a, False))
        print("B= ", to_float(b, False))
        print("sign= ", sign)
        print("exp= ", exp)
        print("mantissa= ", hex(mantissa))
        print("result= ", hex(res), " dec= ", to_float(res, False))
        print("expected: ", to_float(a, False) * to_float(b, False))

    return res


def add_ieee_float(a, b, o=True):
    # a contains smaller absolute value
    if abs(a) > abs(b):
        a, b = b, a

    a = to_ieee_float_bits(a, False)
    b = to_ieee_float_bits(b, False)

    sign = get_sign(b)
    delta = get_exp(b) - get_exp(a)
    mantissa = (get_mantissa(b) + (get_mantissa(a) >> delta)) & 0x7FFFFF
    exp = get_exp(b) - 127
    res = sign << 31 | (exp + 127) << 23 | mantissa

    if o:
        print("================================================")
        print("A= ", to_float(a, False))
        print("B= ", to_float(b, False))
        print("sign= ", sign)
        print("exp= ", exp)
        print("delta= ", delta)
        print("mantissa= ", hex(mantissa))
        print("result= ", hex(res), " dec= ", to_float(res, False))
        print("expected: ", to_float(a, False) + to_float(b, False))


w = 0xC0C80000
x = 0x43010300
y = -13.25
z = 0.890625

to_float(w)
to_float(x)
to_ieee_float_bits(y)
to_ieee_float_bits(z)
mult_ieee_float(w, x)
add_ieee_float(y, z)
