import sys
import math

MAX = 60000  # 50,000より大きい素数も扱うため余裕を持たせる

# エラトステネスの篩で素数リスト作成
is_prime = [True] * (MAX + 1)
is_prime[0] = False
is_prime[1] = False
for i in range(2, int(math.sqrt(MAX)) + 1):
    if is_prime[i]:
        for j in range(i*i, MAX +1, i):
            is_prime[j] = False

primes = [i for i, val in enumerate(is_prime) if val]

def find_neighbor_primes(n):
    # n より小さい最大の素数
    left = None
    # n より大きい最小の素数
    right = None

    # primes は昇順なので二分探索で近い素数を探す
    import bisect
    idx = bisect.bisect_left(primes, n)

    # 左側の素数
    if idx == 0:
        # 3以上なのでこのケースはないと考えるが念のため
        left = None
    elif primes[idx] == n:
        left = primes[idx-1]
        right = primes[idx+1] if idx +1 < len(primes) else None
    else:
        left = primes[idx-1] if idx > 0 else None
        right = primes[idx] if idx < len(primes) else None

    return left, right

for line in sys.stdin:
    line = line.strip()
    if not line:
        continue
    n = int(line)
    left, right = find_neighbor_primes(n)
    print(left, right)