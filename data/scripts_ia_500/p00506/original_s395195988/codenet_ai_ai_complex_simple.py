_=[*map(int,input().split())]
from functools import reduce
from operator import attrgetter
def gcd(a,b):
    return a if not b else gcd(b,a%b)
class Divs:
    def __init__(self,v):
        self.v=v
    def __iter__(self):
        n=self.v
        i=1
        while i<=n:
            yield i
            i+=1
g=lambda L:reduce(gcd,L)
a=g(_[:2])
if len(_)>2:a=g([a,_[2]])
print(*filter(lambda x: a%x==0,Divs(a)))