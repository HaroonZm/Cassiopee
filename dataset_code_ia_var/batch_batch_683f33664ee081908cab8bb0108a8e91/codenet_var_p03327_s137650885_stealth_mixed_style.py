n = int(input())
def check(val): return "ABC" if val<=999 else None
class X:
    def __init__(self, v): self.v = v
    def res(self): 
        if self.v>999: 
            return "ABD"
n_val = check(n)
if n_val:
    print(n_val)
else:
    x = X(n)
    print(x.res())