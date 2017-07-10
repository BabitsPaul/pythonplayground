from math import floor, ceil

def reverse_number(n, partial=0):
    if n == 0:
        return partial
    return reverse_number(n / 10, partial * 10 + n % 10)


def is_palindrome(n):
    tmp = str(n)
    return tmp == tmp[::-1]


def largest_palindrome(upper):
    tmp_max = -1

    '''
    9x9=81
    8x9=72     8x8=64
    7x9=63     7x8=56     7x7=49
    6x9=54     6x8=48     6x7=42     6x6=36
    5x9=45     5x8=40     5x7=35     5x6=30     5x5=25

    (n - 1) * (n + 1) <= n * n
    n ^ 2 - 1 <= n ^ 2
    '''

    #scan for palindrome in zig-zag pattern
    for l_offs in range(0, upper):
        for i_offs in range(0, int(l_offs / 2) + 1):
            i = upper - l_offs + i_offs - 1
            j = upper - i_offs - 1

            #print(i, "\t", j, "\t", i * j)
            if is_palindrome(i * j):
                return {i, j}

tmp = largest_palindrome(1000)
res = 1
for t in tmp:
    res *= t

print(tmp)

print(res)
