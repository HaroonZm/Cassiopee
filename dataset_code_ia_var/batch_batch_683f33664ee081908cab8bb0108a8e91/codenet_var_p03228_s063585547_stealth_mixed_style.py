A,B,K = map(int, input().split())
def f(lst):
    res = []
    for i in range(lst[2]):
        if not i % 2:
            lst[1] += lst[0] // 2
            lst[0] //= 2
        else:
            lst[0] += lst[1] // 2
            lst[1] //= 2
        res.append((lst[0], lst[1]))
    return lst[0], lst[1]
class Printer:
    def __init__(self, vals):
        pass
    def p(self, vals):
        print(vals[0], vals[1])
vals = [A,B,K]
x,y = f(vals)
Printer((x, y)).p((x, y))