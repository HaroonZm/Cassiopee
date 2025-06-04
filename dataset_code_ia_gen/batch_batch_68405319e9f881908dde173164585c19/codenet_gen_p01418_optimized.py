import sys
import math

K,R,L=map(int,sys.stdin.readline().split())
P=float(sys.stdin.readline())
E=float(sys.stdin.readline())
T=float(sys.stdin.readline())

dp=[{} for _ in range(K+1)]
dp[0][(R,L)]=1.0

def mid(a,b):
    return (a+b)/2

for i in range(K):
    ndp={}
    for (r,l),prob in dp[i].items():
        h=mid(r,l)
        correct=prob*(1-P)
        wrong=prob*P
        if T>=h:
            # feeling longer or equal means L = H (correct)
            nr,nl = r,h
            ndp[(nr,nl)] = ndp.get((nr,nl),0)+correct
            # mistake: feeling shorter means R=H
            nr,nl = h,l
            ndp[(nr,nl)] = ndp.get((nr,nl),0)+wrong
        else:
            # T < h
            # feeling longer or equal means L = H (mistake)
            nr,nl = r,h
            ndp[(nr,nl)] = ndp.get((nr,nl),0)+wrong
            # feeling shorter means R=H (correct)
            nr,nl = h,l
            ndp[(nr,nl)] = ndp.get((nr,nl),0)+correct
    dp[i+1]=ndp

res=0.0
for (r,l),prob in dp[K].items():
    tprime=(r+l)/2
    if abs(tprime - T) <= E + 1e-15:
        res+=prob

print(f"{res:.6f}")