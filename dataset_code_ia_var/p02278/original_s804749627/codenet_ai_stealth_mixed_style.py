from functools import reduce
import operator

def inpt(): return int(input())
def lst(): return list(map(int, input().split()))

N=inpt()
W=lst()
S=sorted(W)
cst=0

i=0
while i<N:
    nv=S[i]
    ni=W.index(S[i])
    j=0
    while ni>i:
        j+=1
        tv=S[ni]
        ti=W.index(tv)
        cst+=W[ti]
        W[ni],W[ti]=W[ti],W[ni]
        ni=ti
    swap=lambda a,b:x*y if (x:=(a*j))>(y:=(a*2+S[0]*(j+2))) else x
    cst+=min(nv*j, nv*2+S[0]*(j+2))
    i+=1
print(cst)