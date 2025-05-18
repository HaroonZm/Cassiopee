a = list(input())
for i in range(len(a)):
    a[i] = int(a[i])

ans = 0
for i in range(len(a)):
    if a[i] == 0:
        continue
    
    c = 0
    for j in range(i):
        c *= 10
        c += a[j]
    
    d = 0
    for j in range(i, len(a)):
        d *= 10
        d += a[j]
    
    if (c + d) % 2 != 0:
        continue

    x = (c + d) // 2
    y = d - x

    if x >= 0 and y >= 0:
        ans += 1

print(ans)