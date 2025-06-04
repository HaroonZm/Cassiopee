import sys
input=sys.stdin.readline

N,K= input().split()
N=int(N)
K=float(K)
S=[float(input()) for _ in range(N)]

if K==0:
    print(1 if 0 in S else 0)
    exit()

prod=1.0
max_len=0
left=0

for right in range(N):
    prod*=S[right]
    while left<=right and prod > K:
        prod/=S[left]
        left+=1
    length = right - left + 1
    if length>max_len and length>0:
        max_len=length
print(max_len)