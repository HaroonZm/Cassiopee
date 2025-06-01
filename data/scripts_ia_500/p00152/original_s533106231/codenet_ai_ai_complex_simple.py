from functools import reduce
from operator import itemgetter
def tr(h):return int(h) if h.isdigit() else 0
import sys
def parse():
    line = sys.stdin.readline()
    return list(map(tr,line.strip().split()))
def combo(arr,n=0,i=-1):
    if n==10:return 0
    i+=1
    if arr[i]==10:
        return arr[i]+arr[i+1]+arr[i+2]+combo(arr,n+1,i)
    if arr[i]+arr[i+1]==10:
        return 10+arr[i+2]+combo(arr,n+1,i+1)
    return arr[i]+arr[i+1]+combo(arr,n+1,i+1)
def g():
    while True:
        x = sys.stdin.readline()
        if not x:break
        if x.strip()=='0':break
        n = int(x)
        arrs = []
        for _ in range(n):
            gms = parse()
            sc=sum(map(int,map(str,gms[1:])))
            score=combo(gms[1:])
            arrs.append([gms[0],score])
        for k,s in sorted(sorted(arrs,key=itemgetter(0)),key=itemgetter(1),reverse=True):
            print(k,s)
g()