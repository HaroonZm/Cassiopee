from math import fmod

N, K = map(int, input().split())
b = N % K
print(min(b, (K - b) % K))