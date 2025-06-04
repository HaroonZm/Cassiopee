_=_=lambda x:x
Q=int(input())
N=list(map(int,input().split()))
X=[[_ for _ in [_ for __ in range(21)]] for __ in [_ for ___ in range(Q-1)]]
X[0][N[0]]=1
for I in range(Q-2):
    for J in range(21):
        if J+N[I+1]<21:X[I+1][J+N[I+1]]+=X[I][J]
        if J-N[I+1]>=0:X[I+1][J-N[I+1]]+=X[I][J]
print(X[Q-2][N[-1]])