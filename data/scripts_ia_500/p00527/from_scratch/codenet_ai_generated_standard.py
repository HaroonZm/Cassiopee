import sys
sys.setrecursionlimit(10**7)
M,N=map(int,input().split())
S=input()
T=input()

# Possible car types
# Train must start and end with 'I', and alternate 'I','O','I','O',...
# Cars can only be connected if types alternate and ends are 'I'

# dp[i][j][k]:
# max length of train formed using S[i:], T[j:] with last car taken from k-th garage (0 for S,1 for T)
# last car type known from parity of length (pos 0 is 'I')
# We'll try all possible next choices respecting constraints
from collections import deque

# We try to build trains starting from empty (no cars taken yet)
# So we consider starting points from S or T with an 'I' car.

dp = [[[-1]*2 for _ in range(N+1)] for __ in range(M+1)]
ans=0
q=deque()

# Initialize dp with starting cars (must be 'I')
for i in range(M):
    if S[i]=='I':
        dp[i+1][0][0]=1
        q.append((i+1,0,0))
        ans=1
        break
for j in range(N):
    if T[j]=='I':
        dp[0][j+1][1]=1
        q.append((0,j+1,1))
        if ans<1:
            ans=1
        break

while q:
    i,j,k=q.popleft()
    length=dp[i][j][k]
    # last car from garage k, length-length train formed using first i from S, j from T
    # last car type:
    last_type = 'I' if length%2==1 else 'O'
    # next car type must be opposite
    next_type = 'O' if last_type=='I' else 'I'
    # try take next car from S if k!=0 or k=0, depends on trying both garages
    if k==0:
        # last car from S, next must be from T or S but different type and must be adjacent
        # we try from T since if from S we must ensure adjacency, but problem states car types alternate.
        if j<N and T[j]==next_type:
            if dp[i][j+1][1]<length+1:
                dp[i][j+1][1]=length+1
                q.append((i,j+1,1))
        if i<M and S[i]==next_type:
            if dp[i+1][j][0]<length+1:
                dp[i+1][j][0]=length+1
                q.append((i+1,j,0))
    else:
        # last car from T
        if i<M and S[i]==next_type:
            if dp[i+1][j][0]<length+1:
                dp[i+1][j][0]=length+1
                q.append((i+1,j,0))
        if j<N and T[j]==next_type:
            if dp[i][j+1][1]<length+1:
                dp[i][j+1][1]=length+1
                q.append((i,j+1,1))

# We must ensure train ends with 'I'
# length%2=1 means last car is 'I'

for i in range(M+1):
    for j in range(N+1):
        for k in range(2):
            if dp[i][j][k]>=1 and dp[i][j][k]%2==1:
                if dp[i][j][k]>ans:
                    ans=dp[i][j][k]

print(ans)