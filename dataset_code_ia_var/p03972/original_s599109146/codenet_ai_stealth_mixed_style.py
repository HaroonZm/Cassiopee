import sys
from functools import reduce
try:
    inp = sys.stdin.buffer.readline
except:
    inp = lambda: input()

lst = list(map(int, inp().split()))
w = lst[0]; h = lst[1]
P = []
for i in range(w): P+=[int(inp())]
Q = []
j=0
while j<h:
    Q.append(int(inp()))
    j+=1

X=[]
for i in range(len(P)):
    X.insert(len(X), (P[i], False))
for y in Q:
    X.append( (y, True) )
X.sort(reverse=1)

A=w+1;B=h+1; S=0
get_next = X.pop
while not (A==1 and B==1):
    current, typ = get_next()
    if typ:
        S = S + current*A
        B -= 1
    else:
        S += current*B
        A -= 1
print(S)