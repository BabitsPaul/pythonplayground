from random import choice, random
from string import printable

mutate_prob = 0.1
population_size = 10
drop_last = .75
generations = 1000


def rnd_str(len):
    return ''.join(choice(printable) for i in range(0, len))


def genetic_algo(n, cost, mate, mutate, restrict):
    population = sorted([rnd_str(n) for i in range(0, population_size)], key=lambda s: cost(s))

    for i in range(0, generations):
        if not population or cost(population[0]) == 0:
            break

        print("Generation=", i, "\tBest so far: ", population[0])

        population = restrict(sorted([mutate(s) for i in range(0, population_size) for s in mate(choice(population), choice(population))],
                            key=lambda s: cost(s)))

    if population:
        if cost(population[0]) == 0:
            print("Match found")
        else:
            print("No match found. Best guess: ", population[0])
    else:
        print("No match was found. Terminated with empty set")


genetic_algo(11,
             lambda s: sum((ord(v[0]) - ord(v[1])) ** 2 for v in zip("Hello world", s)),
             lambda a, b: [''.join(chr((ord(v[0]) + ord(v[1])) // 2) for v in zip(a, b)),
                        a[:len(a) // 2] + b[len(a) // 2:],
                        b[:len(a) // 2] + a[len(a) // 2:]],
             lambda s: ''.join(v if random() >= mutate_prob else chr(ord(v) + 1) if random() < .5 else chr(ord(v) - 1) for v in s),
             lambda p: p[:int(len(p) * (1 - drop_last))])

