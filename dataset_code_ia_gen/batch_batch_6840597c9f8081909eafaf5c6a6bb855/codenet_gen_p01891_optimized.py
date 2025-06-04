N,M,A,B=map(int,input().split())
D=list(map(int,input().split()))
discard=[]
idx=0
while idx<N and D[idx]>=A:
    discard.append(idx)
    idx+=1
while N-len(discard)<M:
    if not discard:
        break
    inner=discard[-1]
    if D[inner]<=B:
        discard.pop()
    else:
        discard=discard
        break
print(len(discard))