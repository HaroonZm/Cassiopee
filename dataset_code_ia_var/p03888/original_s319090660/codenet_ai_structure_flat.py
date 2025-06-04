from collections import defaultdict

R1, R2 = map(int, input().split())
ans = R1 * R2 / (R1 + R2)
print(ans)