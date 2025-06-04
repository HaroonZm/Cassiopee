def getVal():
    return tuple(map(int,input().split()))
N,M = getVal()
from math import floor
x = M // N
flag = False; i = x
while i > 0:
    if not (M%i): print(i); flag=True; break
    i -= 1
if not flag:
    def p():pass