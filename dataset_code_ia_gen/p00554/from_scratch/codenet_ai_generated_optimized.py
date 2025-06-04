N,M=map(int,input().split())
costs=[]
count=0
for _ in range(M):
    A,B=map(int,input().split())
    if A>=N:
        count+=1
    else:
        costs.append(N-A)
costs.sort()
needed = max(0,M-1 - count)
print(sum(costs[:needed]))