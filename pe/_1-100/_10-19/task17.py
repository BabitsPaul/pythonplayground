from math import floor

single = [
    "",
    "one",
    "two",
    "three",
    "four",
    "five",
    "six",
    "seven",
    "eight",
    "nine",
    "ten"
]

teens = [
    "eleven",
    "twelve",
    "thirteen",
    "fourteen",
    "fifteen",
    "sixteen",
    "seventeen",
    "eighteen",
    "nineteen",
]

tens = [
    "",
    "ten",
    "twenty",
    "thirty",
    "forty",
    "fifty",
    "sixty",
    "seventy",
    "eighty",
    "ninety"
]


def words(n):
    if n > 999:
        t = floor(n / 1000)
        return single[t] + " thousand " + words(n % 1000)

    if n > 99:
        h = floor(n / 100)
        return single[h] + " hundred " + (" and " if n % 100 else "") + words(n % 100)

    if n > 19:
        t = floor(n / 10)
        return tens[t] + " " + words(n % 10)

    if n > 10:
        return teens[n - 11]

    return single[n]


def count_chars(n):
    sum = 0

    for i in range(1, n + 1):
        w = words(i)
        print(w)

        sum += len([x for x in w if x != ' '])

    return sum


print(count_chars(1000))
