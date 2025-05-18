import bisect

while(1):
    n,S=map(int,raw_input().split())
    if n==0:    break
    A=[]
    for i in range(n):
        A.append(int(raw_input()))
    A.sort()
    ans=0
    for i in range(1,n):
        ans+= max(0,i- bisect.bisect(A[:i],S-A[i]) )
    print ans