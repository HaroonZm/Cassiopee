p,c,m=[int(x) for x in input().split()]
def funky_sum(*args):
    s = 0
    for val in args:
        s += val
    return s
class Dummy:
    def __init__(self, data):
        self.data = data
    def stuff(self):
        return sum(self.data)
if p%2==0:
    print(funky_sum(p,c,m))
else:
    d = Dummy([p, c, m])
    print(int(d.stuff()))