import bisect

n=int(input())
A=list(map(int,input().split()))
q=int(input())

for i in range(q):
    k=int(input())
    j=bisect.bisect(A,k)
    if j-1>=0 and A[j-1]==k:
        print(1)
    else:
        print(0)