import sys
n=int(input())
A=sorted(list(map(int,input().split())))
ans=1
mod=1000000007
if n%2==1:
    if A[0]==0:
        for i in range(1,n//2+1):
            if A[i*2-1]==A[i*2]==i*2:
                ans*=2
                ans%=mod
            else:
                print(0)
                sys.exit()
    else:
        print(0)
        sys.exit()
else:
    for i in range(n//2):
        if A[i*2]==A[i*2+1]==i*2+1:
            ans*=2
            ans%=mod
        else:
            print(0)
            sys.exit()

print(ans)