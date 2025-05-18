h, w = map(int, input().split())
s = [list(input()) for _ in range(h)]

ans = 0
ci = [0 for _ in range(w)]
for i in range(h - 1, -1, -1):
    co = 0
    for j in range(w - 1, -1, -1):
        if s[i][j] == 'J':
            ans += co * ci[j]
        elif s[i][j] == 'O':
            co += 1
        elif s[i][j] == 'I':
            ci[j] += 1

print(ans)