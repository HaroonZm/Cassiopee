import math as m
import sys

def _fetch():
    return int(sys.stdin.readline())

k=_fetch()
N=512
lst=[]
for idx in range(N):
    res = 1
    for j in range(1,8):
        res *= (idx + j)
    res //= m.factorial(7)
    lst.append(res)
lst = lst[::-1]

count = 0
ANS=[]
i=0
while i<N:
    base = "FESTIVA"
    mult=lst[i]
    Ls=""
    q, k = divmod(k, mult)
    while q>0:
        Ls += "L"
        q -= 1
    temp=base+Ls
    ANS.append(temp)
    i+=1

def _flip(xs):
    xs2=[]
    for p in range(len(xs)-1,-1,-1):
        xs2.append(xs[p])
    return xs2

X = _flip(ANS)
del lst
S=""
for x in X:
    S+=x
print(S)