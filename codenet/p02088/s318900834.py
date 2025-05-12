n = int(input())
a = list(map(int, input().split()))

p, q = 0, 0
for i in a:
    if i % 2 == 0:
        p += 1
    else:
        q += 1
    
if p == 0 or q == 0:
    print(0)
    exit()

res = p

if q % 2 == 0:
    res += 2 * max(q // 2 - 1, 0)
else:
    res += (q // 2) * 2

print(res)