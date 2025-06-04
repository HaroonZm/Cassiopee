N = int(input())
AB = [tuple(map(int, input().split())) for _ in range(N)]
at = AB[-1][0]
bt = AB[-1][1]
if at % bt == 0:
    cnt = 0
elif at > bt:
    cnt = bt - (at % bt)
else:
    cnt = bt - at
res = cnt
for tmp, b in reversed(AB[:-1]):
    a = tmp + res
    if a % b == 0:
        continue
    if a > b:
        res += b - (a % b)
    elif a < b:
        res += b - a
print(res)