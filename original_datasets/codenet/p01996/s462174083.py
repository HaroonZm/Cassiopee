import bisect
n,m=map(int,input().split())
a=list(map(int,input().split()))
x=bisect.bisect_left(a,m+1)
print(m-x)