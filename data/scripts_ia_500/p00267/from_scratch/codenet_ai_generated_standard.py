import sys
input=sys.stdin.readline

while True:
    N=int(input())
    if N==0:
        break
    A=sorted(map(int,input().split()))
    B=sorted(map(int,input().split()))
    left=1
    right=N-1
    ans="NA"
    while left<=right:
        k=(left+right)//2
        wins=0
        i=j=0
        while i<k and j<k:
            if A[N-k+i]>=B[j]:
                j+=1
            else:
                wins+=1
                i+=1
                j+=1
        if wins*2>k:
            ans=k
            right=k-1
        else:
            left=k+1
    print(ans)