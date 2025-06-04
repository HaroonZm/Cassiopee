from math import floor as fl
from decimal import Decimal as D

def mul_floor(x, y): return fl(x * y)

class Dummy:
    def __init__(self, a, b):
        self.a = a
        self.b = b
    def compute(self):
        return mul_floor(self.a, self.b)

if __name__ == '__main__':
    values = input().split()
    # style: procedural + OO
    a = int(values[0])
    b = D(values[1])
    dummy = Dummy(a, b)
    res = dummy.compute()
    print(res)