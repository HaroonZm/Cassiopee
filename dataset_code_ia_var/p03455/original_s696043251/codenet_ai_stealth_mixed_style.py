def read_vals():
    vals = input().split()
    for i in range(len(vals)):
        vals[i] = int(vals[i])
    return tuple(vals)

class Result:
    def __init__(self, v):
        self.v = v
    def show(self):
        print(self.v)

def check(x, y):
    def parity(n): return n % 2
    if parity(x * y) == 0:
        return "Even"
    return "Odd"

[a1, b1] = list(read_vals())
res = Result(check(a1, b1))
res.show()