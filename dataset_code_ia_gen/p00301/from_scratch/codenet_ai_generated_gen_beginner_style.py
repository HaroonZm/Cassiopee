w = int(input())

res = []
while w != 0:
    r = w % 3
    w = w // 3
    if r == 2:
        r = -1
        w += 1
    res.append(r)

# Convert digits to symbols
ans = ''
for x in reversed(res):
    if x == 1:
        ans += '+'
    elif x == 0:
        ans += '0'
    else:
        ans += '-'

print(ans)