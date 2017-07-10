#!/usr/bin/python3

import sys
import random


class InterP(object):
    def __init__(self, code, cfg={}):
        self.cfg = cfg
        self.pos = 0, 0
        self.dir = 0, 1
        self.stop = False
        self.str_mode = False
        self.stack = []
        self.code = [[c for c in s] for s in code.split('\n')]
        self.ops = dict({
            '<': (0, lambda: self.change_dir((0, -1))),
            '>': (0, lambda: self.change_dir((0, 1))),
            '^': (0, lambda: self.change_dir((-1, 0))),
            'v': (0, lambda: self.change_dir((1, 0))),
            '?': (0, lambda: self.change_dir(random.choice([(0, 1), (0, -1), (1, 0), (-1, 0)]))),
            '\"': (0, lambda: self.toggle_str_mode()),
            '#': (0, lambda: self.move()),
            ' ': (0, lambda: 0),
            '@': (0, lambda: self.terminate()),
            '&': (0, lambda: self.push(int(input("Please enter a number")))),
            '~': (0, lambda: self.push(ord(input("Please enter a character")))),
            '!': (1, lambda x: self.stack.append(1 if x == 0 else 0)),
            '_': (1, lambda x: self.change_dir((0, 1) if x == 0 else (0, -1))),
            '|': (1, lambda x: self.change_dir((1, 0) if x == 0 else (-1, 0))),
            ':': (1, lambda x: self.stack.__iadd__([x, x])),
            '$': (1, lambda x: 0),
            '.': (1, lambda x: print(str(x), end="")),
            ',': (1, lambda x: print(chr(x), end="")),
            '\\': (2, lambda a, b: self.stack.__iadd__([a, b])),
            '+': (2, lambda a, b: self.push(b + a)),
            '-': (2, lambda a, b: self.push(b - a)),
            '*': (2, lambda a, b: self.push(b * a)),
            '/': (2, lambda a, b: self.push(b // a)),
            '%': (2, lambda a, b: self.push(b % a)),
            '`': (2, lambda a, b: self.push(1 if b > a else 0)),
            'g': (2, lambda a, b: self.push(ord(self.code[a][b]))),
            'p': (3, lambda y, x, v: self.update_field(x, y, v))
        })

    def run(self):
        while not self.stop:
            c = self.inp[self.pos[1]][self.pos[0]]

            if self.str_mode:
                self.push(ord(c))
            elif c.isdigit():
                self.push(ord(c) - ord('0'))
            else:
                pc = self.ops[c][0]
                cmd = self.ops[c][1]

                if pc == 0:
                    cmd()
                elif pc == 1:
                    cmd(self.pop())
                elif pc == 2:
                    cmd(self.pop(), self.pop())
                elif pc == 3:
                    cmd(self.pop(), self.pop(), self.pop())
                else:
                    print("Invalid count of parameters - misconfiguration")

            self.print_state()

    def update_field(self, x, y, v):
        self.code[y] = self.code[y][0:x] + chr(v) + self.code[y][x + 1:]

    def move(self):
        self.pos = (self.pos[0] + self.dir[0], self.pos[1] + self.dir[1])

    def push(self, x):
        self.stack.append(x)

    def pop(self):
        return self.stack.pop() if self.stack else 0

    def change_dir(self, nd):
        self.dir = nd

    def toggle_str_mode(self):
        self.str_mode = not self.str_mode

    def print_state(self):
        print(dict(self))
        print("\n")

    def terminate(self):
        self.stop = True


def start():
    print("Befunge-Interpreter v1.0")
    print("Author: Babits Paul")
    print("Parameters: ", sys.argv)

    if len(sys.argv) < 2 or len(sys.argv) > 3:
        print("Error - Invalid parameters")
        print("Usage: [--debug] file")
        return

    if len(sys.argv) == 3 and sys.argv[1] != "--debug":
        print("Error - unknown flag: ", sys.argv[1])
        print("Usage: [--debug] file")
        return

    debug = len(sys.argv) == 3

    if debug:
        print("Debugging enabled")

    file = open(sys.argv[2] if debug else sys.argv[1])
    prog = file.read()
    file.close()
    # interpret(prog, debug
    v = InterP(prog)
    v.run()


start()
