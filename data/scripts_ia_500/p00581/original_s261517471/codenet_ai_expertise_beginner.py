h, w = input().split()
h = int(h)
w = int(w)

s = []
for i in range(h):
    row = input()
    s.append(list(row))

ans = 0
ci = []
for j in range(w):
    ci.append(0)

i = h - 1
while i >= 0:
    co = 0
    j = w - 1
    while j >= 0:
        if s[i][j] == 'J':
            ans = ans + co * ci[j]
        elif s[i][j] == 'O':
            co = co + 1
        elif s[i][j] == 'I':
            ci[j] = ci[j] + 1
        j = j - 1
    i = i - 1

print(ans)