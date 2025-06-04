import sys
import math

input=sys.stdin.readline
T=int(input())
for _ in range(T):
    h,w=map(int,input().split())
    R= (h+w-1)//2
    B= (h+w-1)-R
    g=math.gcd(R,B)
    print(R//g,B//g)