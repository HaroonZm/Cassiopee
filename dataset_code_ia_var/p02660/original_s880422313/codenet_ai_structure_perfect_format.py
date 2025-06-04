n = int(input())

if n == 1:
    print(0)
    exit()

x = n ** 0.5
d = {}
z = 2
ans = 0
while True:
    if n % z == 0:
        n //= z
        if d.get(z) is None:
            d[z] = 1
        else:
            d[z] += 1
    else:
        z += 1
    if n == 1:
        break
    if x < z:
        ans = 1
        break

for dv in d.values():
    i = 1
    tmp = dv
    while True:
        tmp -= i
        i += 1
        if tmp < 0:
            break
        ans += 1

print(ans)