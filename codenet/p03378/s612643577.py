N,M,X = map(int,input().split())
A = list(map(int,input().split()))
tmp1 = list(range(X))
tmp2 = list(range(X+1,N))
ans = []
count = 0
for i in range(len(tmp1)):
    if tmp1[i] in A:
        count += 1
ans.append(count)
count = 0
for j in range(len(tmp2)):
    if tmp2[j] in A:
        count += 1
ans.append(count)
print(min(ans))