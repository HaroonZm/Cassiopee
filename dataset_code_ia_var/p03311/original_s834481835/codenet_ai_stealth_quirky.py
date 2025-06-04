n = int(input())
a = list(map(int, input().split()))
[ a.__setitem__(j, a[j]-(j+1)) for j in range(n) ]
a = sorted(a)

odd = n&1
if odd:
    acc = sum(map(lambda x: abs(x - a[n//2]), a))
else:
    acc, alt = 0, 0
    x = (a[n//2-1] + a[n//2]) >> 1
    for y in a:
        acc += abs(y - x)
        alt += abs(y - (x-1))
    acc = (acc, alt)[acc > alt]

print(acc)