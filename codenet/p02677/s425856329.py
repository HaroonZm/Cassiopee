import math
A, B, H, M = map(int, input().split())
s = 0.5 * (H*60+M)
l = 6 * M
c = max(s, l) - min(s, l)

ans = math.sqrt(A**2 + B**2 - 2*A*B*math.cos(math.radians(c)))
print(ans)