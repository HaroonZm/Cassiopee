import math

n, m = map(int, input().split())
ball = list(map(int, input().split()))

lcm = n * m // math.gcd(n, m)

i = 0
ans = 0
while i < lcm // m:
    j = 0
    data = []
    while j < m:
        idx = (i * m + j) % len(ball)
        d = ball[idx]
        data.append(d)
        j += 1
    max_data = data[0]
    min_data = data[0]
    k = 1
    while k < len(data):
        if data[k] > max_data:
            max_data = data[k]
        if data[k] < min_data:
            min_data = data[k]
        k += 1
    ans += (max_data - min_data)
    i += 1

print(ans)