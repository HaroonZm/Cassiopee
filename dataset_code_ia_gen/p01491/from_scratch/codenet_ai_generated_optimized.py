import sys
input=sys.stdin.readline
M,N,m0,md,n0,nd=map(int,input().split())

m=[0]*(M)
n=[0]*(N)

m[0]=m0
for i in range(M-1):
    m[i+1]=(m[i]*58+md)%(N+1)

n[0]=n0
for i in range(N-1):
    n[i+1]=(n[i]*58+nd)%(M+1)

from collections import Counter

count_m=Counter(m)
count_n=Counter(n)

# m and n keys are values of carrot and kiwi types
# For each type of carrot and kiwi (0 to max key), min of counts represents max rabbits
res=0
for k in count_m:
    if k in count_n:
        res+=min(count_m[k],count_n[k])

print(res)