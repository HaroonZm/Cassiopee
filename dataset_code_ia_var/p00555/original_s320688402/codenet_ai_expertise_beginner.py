n, m, d = map(int, input().split())
mp = []
for i in range(n):
    mp.append(input())

t = ''
for i in range(d):
    t += '.'

cnt = 0
for i in range(n):
    for j in range(m):
        # horizontal check
        if j <= m - d:
            str1 = ''
            for k in range(d):
                str1 += mp[i][j + k]
            if str1 == t:
                cnt += 1
        # vertical check
        if i <= n - d:
            str2 = ''
            for k in range(d):
                str2 += mp[i + k][j]
            if str2 == t:
                cnt += 1
print(cnt)