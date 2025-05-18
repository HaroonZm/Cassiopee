n = int(input())
eff = [0]*360
days = [list(map(int, input().split())) for i in range(n)]

for m, d, v, s in days:
    # [a, b)
    a = (m-1)*30 + d - 1
    b = a + v
    for i in range(a, b):
        eff[i%360] = max(eff[i%360], s)
    for i in range(b, a+360):
        eff[i%360] = max(eff[i%360], s - min(i - b + 1, 360 + a - i))
print(min(eff))