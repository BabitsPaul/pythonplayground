from collections import OrderedDict

from spellout import spellout


def polybius(key: int =None):
    if key is None:
        # create table
        poly = [[chr(x + ord('A')) for x in range(i * 5, (i + 1) * 5)] for i in range(0, 2)] + \
               [[chr(x + ord('A')) for x in range(i * 5 + 1, (i + 1) * 5 + 1)] for i in range(2, 5)]
        poly[1][4] = 'K'  # override last character in second row, as i and j are grouped together

        # reorder
        zip(poly)

        return poly
    else:
        # strip separators and space
        stripnonalpha = "".join(c for c in spellout(key) if c.isalpha()).upper()
        # append full alphabet
        joinalphabet = stripnonalpha + "".join(chr(c) for c in range(ord('A'), ord('Z') + 1))
        # remove duplicates
        nodups = "".join(OrderedDict.fromkeys(joinalphabet))
        # strip J (grouped with I)
        nodups = [x for x in nodups if x != 'J']

        # generate polybius
        splitat = [0, 5, 10, 15, 20]

        poly = [nodups[s:s + 5] for s in splitat]
        zip(poly)

        return poly


def encrypt(plaintext: str, key: int):
    if key < 0:
        raise "Invalid key " + str(key)

    # build table of characters to replace
    table = dict(zip([p for row in polybius() for p in row],
                     [p for row in polybius(key) for p in row]))

    # correct plaintext to alpha-only and replace j by i (grouping)
    plaintext = [x for x in plaintext.upper().replace('J', 'I') if x.isalpha()]

    return "".join([table[x] for x in plaintext])


def decrypt(ciphertext: str, key: int):
    if key < 0:
        raise "Invalid key " + str(key)

    # lookup table
    table = dict(zip([p for row in polybius(key) for p in row],
                     [p for row in polybius() for p in row]))

    return "".join([table[x] for x in ciphertext])

print(decrypt(encrypt("abcdefghijklmnopqrst", 23), 23))
