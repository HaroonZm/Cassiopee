import math

n, m = map(int, input().split())
ball = list(map(int, input().split()))

lcm = n * m // math.gcd(n, m)

ans = 0
for i in range(lcm // m):
    data = []
    for j in range(m):
        d = ball[(i*m+j) % len(ball)]
        data.append(d)
    ans += (max(data) - min(data))

print(ans)