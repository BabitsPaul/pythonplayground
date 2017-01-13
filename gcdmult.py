from math import gcd


# pa = product(a)
# pb = product(b)
#
# the prim-factorisation of gcd(pa, pb) is the intersection
# of the prim-factorisations of pa and pb
#
# the prim-factorisation of pa is the union of the prim-factorisations
# of all elements in a. Same applies to pb
#
# thus the product of the gcds of all elements in a with all elements in b
# (duplicates eliminated) is equivalent to gcd(pa, pb)
#
# e.g. 7200 =  25 * 48 * 6    = 2^5 * 3^2 * 5^2
#      43740 = 27 * 45 * 36   = 2^2 * 3^7 * 5^1
#
#      gcd(7200, 43740) = 180 = 2^2 * 3^2 * 5^1
#
#      a = [25, 48, 6]   b = [27, 45, 36]
#      gcd(25, 45) = 5 => a = [5, 48, 6]  b = [27, 9, 36] totalgcd = 5
#      gcd(48, 27) = 3 => a = [5, 16, 6]  b = [9, 9, 36]  totalgcd = 5 * 3
#      gcd(16, 36) = 4 => a = [5, 4, 6]   b = [9, 9, 9]   totalgcd = 5 * 3 * 2^2
#      gcd(6, 9) = 3   => a = [5, 4, 2]   b = [3, 9, 9]   totalgcd = 5 * 3^2 * 2^2
#      no more further non-coprime pairs can be built from elements in a and b => terminate
#
# this method is an brute-force implementation of the above described algorithm
def gcd_mult(a, b):
    gcd_total = 1

    for i in a:
        c = list()

        for j in b:
            gcd_tmp = gcd(i, j)
            gcd_total *= gcd_tmp

            i //= gcd_tmp
            c.append(j // gcd_tmp)

        c = b

    return gcd_total

#test case
print(gcd_mult([1, 2, 3, 4, 5], [6, 8, 3]) - gcd(120, 144) == 0)
