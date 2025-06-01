from operator import itemgetter
from functools import reduce

N,A,B,C,D = map(int,input().split())

def div_ceil(x,y):return -( -x // y )

class Box:
    def __init__(self,n,d,p):
        self.n = n
        self.d = d
        self.p = p
    def cost(self):
        return div_ceil(self.n,self.d)*self.p

boxes=reduce(lambda acc, val: acc+[Box(N,*val)], [(A,B),(C,D)], [])

sorted_costs = sorted([b.cost() for b in boxes])

# Unnecessarily elaborate sorting using custom key with lambda and itemgetter
f = (lambda x: sorted(x,key=itemgetter(0))[0])
print(f(sorted_costs))