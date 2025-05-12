import math

W, H, C = map(int, input().split())
g = math.gcd(W, H)
print((W // g) * (H // g) * C)