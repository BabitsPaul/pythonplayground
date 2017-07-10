from random import random, randint, sample, choice
from string import ascii_uppercase


class Gene(object):
    mutation_rate = 0.2
    overweight_penalty = 50

    def __init__(self, elems):
        self.elems = elems
        self.value, self.weight, self.score = self.calc_metrics()

    @staticmethod
    def rnd(inp_set):
        return Gene(list(zip(inp_set, [randint(0, 1) for i in range(0, len(inp_set))])))

    @staticmethod
    def mate(a, b):
        pivot = randint(0, len(a.elems))

        return (Gene([(e, v) for e, v in a.elems[:pivot]] + [(e, a) for e, a in b.elems[pivot:]]),
                Gene([(e, v) for e, v in b.elems[:pivot]] + [(e, a) for e, a in a.elems[pivot:]]))

    def mutate(self):
        if random() > Gene.mutation_rate:
            return

        index = randint(0, len(self.elems) - 1)
        e = self.elems[index]
        self.elems[index] = (e[0], (e[1] + 1) % 2)

    def calc_metrics(self):
        value = sum(map(lambda e: e[0][1] * e[1], self.elems))
        weight = sum(map(lambda e: e[0][2] * e[1], self.elems))

        return value, weight, value - max(0, weight - max_weight) * 10

    def clone(self):
        return Gene([(e, v) for e, v in self.elems])

    def __str__(self):
        return "Gene - weight: {} value: {} score: {} elems: {}".format(self.weight, self.value, self.score,
                                                                        str([e[0] for e in self.elems if e[1]]))


class Population(object):
    elitism = .2
    size = 100

    def __init__(self, inp_set):
        self.inp_set = inp_set
        self.genes = []
        self.fill()
        self.sort()

    def fill(self):
        self.genes += [Gene.rnd(self.inp_set) for i in range(len(self.genes), Population.size // 3)]
        for i in range(len(self.genes), Population.size):
            self.mate()

    def sort(self):
        self.genes.sort(key=lambda g: g.score, reverse=True)

    def kill(self):
        self.genes = self.genes[0:int(len(self.genes) * Population.elitism)]

    def mate(self):
        self.genes += Gene.mate(choice(self.genes), choice(self.genes))

    def generation(self):
        self.sort()
        self.kill()
        self.fill()

        for g in self.genes:
            g.mutate()

        self.sort()

    def best_score(self):
        return self.genes[0].score

    def __str__(self):
        return str([v for v in map(lambda g: g.score, self.genes)])


max_iterations = 1000
max_weight = 1000

tmp = [("Hydrogen", 389, 400), ("Helium", 309, 380), ("Lithium", 339, 424), ("Beryllium", 405, 387), ("Boron", 12, 174),
       ("Carbon", 298, 483), ("Nitrogen", 409, 303), ("Oxygen", 432, 497), ("Fluorine", 414, 306), ("Neon", 149, 127),
       ("Sodium", 247, 341), ("Magnesium", 327, 98), ("Aluminium", 195, 343), ("Silicon", 356, 122),
       ("Phosphorus", 49, 157), ("Sulfur", 151, 438), ("Chlorine", 56, 460), ("Argon", 317, 395),
       ("Potassium", 383, 221),
       ("Calcium", 281, 395), ("Scandium", 394, 79), ("Titanium", 377, 303), ("Vanadium", 381, 308),
       ("Chromium", 299, 295), ("Manganese", 114, 447), ("Iron", 422, 360), ("Cobalt", 288, 249), ("Nickel", 458, 482),
       ("Copper", 91, 314), ("Zinc", 104, 140), ("Gallium", 470, 254), ("Germanium", 77, 25), ("Arsenic", 213, 393),
       ("Selenium", 419, 96), ("Bromine", 114, 199), ("Krypton", 490, 8), ("Rubidium", 278, 367),
       ("Strontium", 310, 159),
       ("Yttrium", 175, 109), ("Zirconium", 453, 288), ("Niobium", 56, 375), ("Molybdenum", 147, 343),
       ("Technetium", 123, 105), ("Ruthenium", 325, 214), ("Rhodium", 418, 428), ("Palladium", 353, 387),
       ("Silver", 182, 429), ("Cadmium", 411, 394), ("Indium", 322, 329), ("Tin", 490, 436), ("Antimony", 28, 479),
       ("Tellurium", 443, 305), ("Iodine", 345, 253), ("Xenon", 463, 19), ("Caesium", 361, 416), ("Barium", 307, 417),
       ("Lanthanum", 291, 453), ("Cerium", 259, 414), ("Praseodymium", 58, 83), ("Neodymium", 127, 475),
       ("Promethium", 11, 480), ("Samarium", 361, 192), ("Europium", 409, 271), ("Gadolinium", 86, 231),
       ("Terbium", 100, 75), ("Dysprosium", 166, 128), ("Holmium", 54, 109), ("Erbium", 432, 399),
       ("Thulium", 361, 395),
       ("Ytterbium", 417, 222), ("Lutetium", 311, 224), ("Hafnium", 138, 101), ("Tantalum", 177, 397),
       ("Tungsten", 14, 234), ("Rhenium", 480, 141), ("Osmium", 208, 490), ("Iridium", 121, 68), ("Platinum", 182, 29),
       ("Gold", 339, 267), ("Mercury", 259, 438), ("Thallium", 342, 425), ("Lead", 65, 395), ("Bismuth", 33, 497),
       ("Polonium", 293, 394), ("Astatine", 392, 210), ("Radon", 116, 203), ("Francium", 433, 253),
       ("Radium", 303, 109),
       ("Actinium", 149, 317), ("Thorium", 342, 129), ("Protactinium", 457, 50), ("Uranium", 118, 77),
       ("Neptunium", 117, 300), ("Plutonium", 106, 455), ("Americium", 66, 365), ("Curium", 393, 407),
       ("Berkelium", 289, 458), ("Californium", 302, 322), ("Einsteinium", 455, 94), ("Fermium", 216, 347),
       ("Mendelevium", 304, 331), ("Nobelium", 49, 236), ("Lawrencium", 84, 351), ("Rutherfordium", 345, 233),
       ("Dubnium", 168, 187), ("Seaborgium", 361, 125), ("Bohrium", 236, 479), ("Hassium", 201, 353),
       ("Meitnerium", 278, 307), ("Darmstadtium", 308, 344), ("Roentgenium", 171, 201), ("Copernicium", 251, 460),
       ("Ununtrium", 158, 52), ("Ununquadium", 282, 113), ("Ununpentium", 145, 497), ("Ununhexium", 459, 449),
       ("Ununseptium", 327, 7), ("Ununoctium", 184, 411)]


def gen_rnd_inp():
    return [(ascii_uppercase[i // 26] + ascii_uppercase[i % 26], randint(50, 300), randint(60, 1000)) for i in
            range(0, 100)]


def run():
    p = Population(tmp)
    score = p.best_score()
    iter_ct = 0
    iter_total_ct = 0
    print(p)

    while iter_ct < max_iterations:
        p.generation()
        # print(p)
        iter_total_ct += 1

        if p.best_score() == score:
            iter_ct += 1
        else:
            iter_ct = 0
            score = p.best_score()

        print("iteration: {} no change since: {} best score: {} best: {}".format(iter_total_ct, iter_ct, score,
                                                                                 p.genes[0]))


run()
