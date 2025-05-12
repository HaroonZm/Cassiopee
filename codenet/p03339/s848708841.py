N=int(input())
S=input()

E=[0]*N
W=[0]*N

for i in range(N):
    if S[i]=="E":
        E[i]+=1
    else:
        W[i]+=1

for i in range(1,N):
    E[i]=E[i-1]+E[i]
for i in range(N-2,-1,-1):
    W[i]=W[i+1]+W[i]

SUM=[E[i]+W[i] for i in range(N)]
print(N-max(SUM))