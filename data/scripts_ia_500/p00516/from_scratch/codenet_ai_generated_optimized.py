n,m=map(int,input().split())
a=[int(input()) for _ in range(n)]
b=[int(input()) for _ in range(m)]
counts=[0]*n
for bj in b:
    for i in range(n):
        if a[i]<=bj:
            counts[i]+=1
            break
print(counts.index(max(counts))+1)