
def expand(v):
    return v        # TODO not a valid definition


def order_invariant_hash(input):
    hash = 0

    for char in input:
        hash ^= expand(ord(char))

    return hash

print(order_invariant_hash("abcdefghikl") == order_invariant_hash("abcdefabcghikl"))
