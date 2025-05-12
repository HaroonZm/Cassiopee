"""
Bitset I - Bit Flag
http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=ITP2_10_C&lang=jp

"""
class Bit:
    def __init__(self):
        self.data = 0

    def process(self, op, arg):
        funcs = (self.test, self.set, self.clear, self.flip, self.all, self.any, self.none, self.count, self.val)
        funcs[int(op)](arg)

    def test(self, arg):
        print(int(bool(self.data & 1 << int(arg))))

    def set(self, arg):
        self.data |= 1 << int(arg)

    def clear(self, arg):
        self.data &= ~(1 << int(arg))

    def flip(self, arg):
        self.data ^= 1 << int(arg)

    def all(self, arg):
        print(int(bin(self.data).count('1') == 64))

    def any(self, arg):
        print(int(self.data != 0))

    def none(self, arg):
        print(int(self.data == 0))

    def count(self, arg):
        print(bin(self.data).count('1'))

    def val(self, arg):
        print(self.data)

b = Bit()
for _ in range(int(input())):
    op, arg = (input() + ' 1').split()[:2]
    b.process(op, arg)