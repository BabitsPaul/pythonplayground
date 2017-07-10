from util.soe import soe_fast

upper = 1
rotate = 0
count = 0

primes = soe_fast(10**6)
print("Primes done")

for i in primes:
    if i > upper * 10:
        upper *= 10
        rotate += 1

    rotational = True
    t = i
    for r in range(0, rotate):
        t = t // 10 + (t % 10) * upper
        if t not in primes:
            rotational = False
            break

    if rotational:
        print("Hit ", i)
        count += 1

print(count)
