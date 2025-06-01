import sys
import math

MAX_N = 60000  # 安全に50,000より大きい素数を探すための上限

# エラトステネスの篩でMAX_Nまでの素数判定表を作る
is_prime = [True] * (MAX_N + 1)
is_prime[0] = False
is_prime[1] = False
for i in range(2, int(math.sqrt(MAX_N)) + 1):
    if is_prime[i]:
        for j in range(i * i, MAX_N + 1, i):
            is_prime[j] = False

for line in sys.stdin:
    n = line.strip()
    if not n:
        continue
    n = int(n)
    # nより小さい最大の素数を探す
    lower = n - 1
    while lower >= 2 and not is_prime[lower]:
        lower -= 1
    # nより大きい最小の素数を探す
    upper = n + 1
    while upper <= MAX_N and not is_prime[upper]:
        upper += 1
    print(lower, upper)