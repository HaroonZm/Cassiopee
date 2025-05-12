import sys
N,M=map(int,input().split())
ans=0
if 2*N>=M:
    print(M//2)
    sys.exit()
ans+=N
M-=2*N
print(ans+M//4)