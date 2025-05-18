N=int(input())
S=[input() for i in range(N)]
M=int(input())
T=[input() for i in range(M)]
max=0
for i in range(N):
    cnt=0
    for j in range(N):
        if S[i]==S[j]:
            cnt+=1
    for k in range(M):
        if S[i]==T[k]:
            cnt-=1
    if max<cnt:
        max=cnt
print(max)