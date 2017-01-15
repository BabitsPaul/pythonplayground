digits = {0: "", 1: "one", 2: "two", 3: "three", 4: "four", 5: "five",
          6: "six", 7: "seven", 8: "eight", 9: "nine"}

single_word = {0: "zero", 1: "one", 2: "two", 3: "three", 4: "four", 5: "five",
               6: "six", 7: "seven", 8: "eight", 9: "nine", 10: "ten",
               11: "eleven", 12: "twelve"}

mult10 = {0: "", 1: "ten", 2: "twenty", 3: "thirty", 4: "fourty", 5: "fifty", 6: "sixty",
          7: "seventy", 8: "eighty", 9: "ninety"}

units = ["", "thousand", "million", "billion", "trillion", "quadrillion",
         "quintillion", "sextillion", "septillion", "octillion", "nonillion",
         "decillion", "undecillion", "duodecillion", "tredecillion", "quattuordecillion",
         "quindecillion", "sedecillion", "septendecillion", "octodecillion",
         "novemdecillion", "vigintillion"]


# spells out an integer as word (correct up to 10**66-1)
def spellout(integer):
    if integer == 0:
        return single_word[0]

    result = ""

    for unit in units:
        if integer == 0:
            break

        tmp = spellout1000(integer % 1000)
        if integer % 1000 != 0:
            tmp += " " + unit
        result = tmp + " " + result
        integer //= 1000

    return result


def spellout1000(number):
    if number == 0:
        return ""

    if number < 13:
        return single_word[number]

    str = ""

    hundreds = number // 100
    if hundreds != 0:
        str += digits[hundreds] + "-hundred "
    number -= hundreds * 100

    if number < 13:
        str += single_word[number]
    else:
        str += mult10[number // 10]
        str += " " + digits[number % 10]

    return str
