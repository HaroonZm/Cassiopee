import heapq
N,K=map(int,input().split())
V=list(map(int,input().split()))

#a:左からとる b:右からとる K-a-b:捨てる
score=0
torikata=[]
for d in range(101):
    for a in range(101):
        for b in range(101):
            if d+a+b<=K and a+b<=N:
                torikata.append((a,b,d))

for i in range(len(torikata)):
    A,B,D=torikata[i][0],torikata[i][1],torikata[i][2]
    H=[]
    for i in range(A):
        H.append(V[i])
    for i in range(B):
        H.append(V[-(i+1)])
    heapq.heapify(H)
    for i in range(min(D,A+B)):
        heapq.heappop(H)
    score=max(score,sum(H))

print(score)