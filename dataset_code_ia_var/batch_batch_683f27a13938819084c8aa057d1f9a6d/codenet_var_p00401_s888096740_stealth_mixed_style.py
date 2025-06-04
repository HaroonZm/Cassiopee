import math

def funky_power(n): return 2 ** (int(math.log2(n)))

N = int(input())
if N <= 0:
    print(0)
else:
    class Printer:
        def show(self, val): print(val)
    p = Printer()
    p.show(funky_power(N))