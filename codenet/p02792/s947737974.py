n=int(input())
d = [[0] * 10 for i in range(10)]

ans = 0
for i in range(1,n+1):
    s=str(i)
    if s[0]=="0" or s[-1]=="0":
        continue
    else:
        d[int(s[0])][int(s[-1])] += 1

ans = 0
for i in range(1,10):
    for j in range(1,10):
        ans += d[i][j] * d[j][i]

print(ans)