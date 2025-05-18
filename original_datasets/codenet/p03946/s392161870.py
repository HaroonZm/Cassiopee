N,T=map(int,input().split())
A=list(map(int,input().split()))

MAX=[A[-1]]

for i in range(N-2,-1,-1):
    MAX.append(max(MAX[-1],A[i]))

MAX=MAX[::-1]
SABUN=[MAX[i]-A[i] for i in range(N)]

#print(MAX)
#print(SABUN)
MAXSA=max(SABUN)

ANS=0
for i in range(N):
    if SABUN[i]==MAXSA:
        ANS+=1

print(ANS)