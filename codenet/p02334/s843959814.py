# 文字列の入力
import math
k = input()
k = k.split()
N = int(k[0])
K = int(k[1])
def combinations_count(n, r):
    return math.factorial(n) // (math.factorial(n - r) * math.factorial(r))
print(combinations_count(N+K-1, N)%(10**9+7))