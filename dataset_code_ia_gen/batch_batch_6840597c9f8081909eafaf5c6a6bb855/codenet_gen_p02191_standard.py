import sys
import bisect

input=sys.stdin.readline
N,Q=map(int,input().split())
a=sorted(map(int,input().split()))
for _ in range(Q):
    l,r=map(int,input().split())
    print(bisect.bisect_right(a,r)-bisect.bisect_left(a,l))