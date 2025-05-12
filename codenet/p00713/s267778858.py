#複素数でやってみる
from itertools import combinations
import math

while True:
    N=int(input())
    if N==0:
        break
    mp=[]
    for _ in range(N):
        a,b=map(float,input().split())
        mp.append(complex(a,b))
    center_lst=[]
    for p,q in combinations(mp,2):
        mid=(p+q)/2
        if abs(p-q)>2:
            continue
        d_vec=complex(-(p-q).imag,(p-q).real)/abs(p-q)
        t=1-abs(p-mid)**2
        center_vec1=mid+d_vec*math.sqrt(t)
        center_vec2=mid-d_vec*math.sqrt(t)
        center_lst.append(center_vec1)
        center_lst.append(center_vec2)
    
    ans=1
    for center in center_lst:
        tmp=0
        for x in mp:
            x_center=x-center
            if abs(x_center)<=1+1e-7:
                tmp+=1
        if tmp>ans:
            ans=tmp
    print(ans)