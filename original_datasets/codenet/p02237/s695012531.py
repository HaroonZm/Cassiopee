n = int(input())
l = []
tmp = 0 
for _ in range(n):
    a = list(map(int,input().split()))
    l.append(a)
    if a[len(a)-1] > tmp:
        tmp = a[len(a)-1]

ans = [[0 for i in range(tmp)] for j in range(n)]
for i in range(n):
    if l[i][1] > 0:
        for j in range(2,len(l[i])):
            tmp1 = l[i][j]
            ans[i][tmp1-1] = 1

for i in range(n):
    print(" ".join(map(str,ans[i])))