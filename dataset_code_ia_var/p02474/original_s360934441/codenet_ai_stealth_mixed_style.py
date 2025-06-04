def prod(x, y): return x * y

class R:
    @staticmethod
    def parse(): return [int(j) for j in input().split()]

(r1, r2) = R.parse()
res = prod(r1, r2)
print(res)