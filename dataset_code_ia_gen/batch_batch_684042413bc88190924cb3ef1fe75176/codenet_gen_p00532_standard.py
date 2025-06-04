N=int(input())
M=int(input())
targets=list(map(int,input().split()))
scores=[0]*N
for i in range(M):
    guesses=list(map(int,input().split()))
    target=targets[i]-1
    X=0
    for j in range(N):
        if guesses[j]-1==target:
            scores[j]+=1
        else:
            X+=1
    scores[target]+=X
for s in scores:
    print(s)