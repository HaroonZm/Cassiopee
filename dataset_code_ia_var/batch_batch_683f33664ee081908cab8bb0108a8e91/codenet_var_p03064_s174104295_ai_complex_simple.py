from functools import reduce
from operator import mul

Q=998244353
N=int(input())
A=[int(input())for _ in range(N)]
S=reduce(lambda x,y:x+y,A)
H=(S+1)//2

def double_list(L):
    return list(map(lambda x:x*2%Q,L))

def merge_lists(L1,L2):
    return list(map(lambda x,y:(x*2+y)%Q,zip(L1,L2)))

dp=[1]+[0]*S

for a in A:
    spawned=[[0]*S for _ in range(a)]
    for i in range(a):spawned[i]=dp[i:S-a+1+i]
    zipped=zip(*spawned)
    intermediate=[sum(z)%Q for z in zipped]
    z=double_list(dp)
    for idx, v in enumerate(intermediate):
        z[a+idx]=(z[a+idx]+v)%Q
    dp=z

ans=(pow(3,N,Q)-(sum(dp[H:])%Q*3)%Q)%Q

if S%2<1:
    dp2=reduce(lambda acc,a:merge_lists(acc,[0]*a+acc[:-a]),A,[1]+[0]*S)
    ans=(ans+dp2[H]*3)%Q

print(ans)