class cache(object):
    def __init__(self):
        self.tag = [0] * 8
        self.valid = [0] * 8
        self.dirty = [0] * 8
        self.hc = 0

    def write(self, x):
        if self.tag[self.get_index(x)] != self.get_tag(x):
            return

        self.hc += 1
        self.valid[self.get_index(x)] = 1
        self.dirty[self.get_index(x)] = 1

    def read(self, x):
        if self.tag[self.get_index(x)] == self.get_tag(x):
            self.hc += 1
        else:
            self.dirty[self.get_index(x)] = 0

        self.valid[self.get_index(x)] = 1
        self.tag[self.get_index(x)] = self.get_tag(x)

    def __str__(self):
        return str(["{:02x}/{}/{}".format(tag, valid, dirty) for tag, valid, dirty in zip(self.tag, self.valid, self.dirty)]) \
               + "Hits: {}".format(self.hc)

    def acc(self, s):
        if s[0:2] == 'lw':
            self.read(int(s[3:], 16))
        else:
            self.write(int(s[3:], 16))

    @staticmethod
    def get_tag(n):
        return n >> 3

    @staticmethod
    def get_index(n):
        return n & 7


c = cache()
for ac in ['sw 0x37', 'lw 0x17', 'lw 0x72', 'sw 0x0C', 'sw 0x72', 'lw 0x3A', 'lw 0x0C', 'lw 0x34', 'sw 0x0C', 'lw 0x00', 'lw 0x48']:
    c.acc(ac)
    print(ac, c)
