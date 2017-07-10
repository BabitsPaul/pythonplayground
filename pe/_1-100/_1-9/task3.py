def largest_prime_factor(x):
    i = 2

    while i < x:
        while x % i == 0:
            x /= i

        i += 1

    return i

print(largest_prime_factor(600851475143))

