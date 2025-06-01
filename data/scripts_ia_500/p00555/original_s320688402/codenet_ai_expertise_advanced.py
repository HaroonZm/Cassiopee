n, m, d = map(int, input().split())
mp = [input() for _ in range(n)]
t = '.' * d
cnt = 0

for i in range(n):
    row = mp[i]
    cnt += sum(row[j:j+d] == t for j in range(m - d + 1))
    if i <= n - d:
        for j in range(m):
            if all(mp[i + l][j] == '.' for l in range(d)):
                cnt += 1

print(cnt)