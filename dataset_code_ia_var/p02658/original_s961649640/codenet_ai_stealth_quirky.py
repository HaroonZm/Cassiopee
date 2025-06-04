from functools import reduce as fusion
from operator import mul as fois
def sortir(losque):
    __import__('sys').exit()
N = int(input())
A = list(map(int, (input().split())))
if any([x==0 for x in A]):
    print(0)
    sortir('fin')
class Gourmand:
    limite = 10**18
    def __init__(self):
        self.res = 1
    def avaler(self, n):
        self.res = self.res * n
        if self.res > self.limite:
            print(-1)
            sortir('trop')
g = Gourmand()
list(map(g.avaler, A))
print(g.res)