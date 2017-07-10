def gen_triple(sum):
    '''
        a + b + c = 1000
    and
        a^2 + b^2 = c^2

        a + b + sqrt(a^2+b^2) = 1000

    w.k.:
    a = (m² - n²) * k , b = 2mn * k , c = k * (m² + n²)

    a or b is divisible by 3 and 4
    a, b or c is divisible by 5
    2 | a or 2 | b
    '''

    for m in range(0, sum):
        for n in range(0, m):
            a = m * m - n * n
            b = 2 * m * n
            c = m * m + n * n

            if a * a + b * b == c * c and a + b + c == sum:
                return a, b, c

    return ()


triple = gen_triple(1000)
print(triple)
print(triple[0] * triple[1] * triple[2])

