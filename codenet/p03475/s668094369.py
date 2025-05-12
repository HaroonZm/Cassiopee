#!/usr/bin/env python3
import sys, math, itertools, heapq, collections, bisect, string
input = lambda: sys.stdin.buffer.readline().rstrip().decode('utf-8')
sys.setrecursionlimit(10**7)
inf = float('inf')
mod = 10**9+7
ans = inf ;count = 0 ;pro = 1

n=int(input())
C=[];S=[];F=[]
for i in range(n-1):
    c,s,f=map(int,input().split())
    C.append(c)
    S.append(s)
    F.append(f)
for start in range(n-1):
    i=start
    time=S[start]
    while i < n-1:
        while time % F[i] != 0 or time<S[i]:
            time += 1
        time += C[i]
        i+=1
    print(time)
print(0)