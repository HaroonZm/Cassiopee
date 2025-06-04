import sys

MAX_N = 10000
# 10000番目の素数は104729より小さい（約104730まで探索すれば十分）
LIMIT = 105000

# エラトステネスの篩で素数一覧を作成
is_prime = [True]*(LIMIT+1)
is_prime[0] = is_prime[1] = False
for i in range(2,int(LIMIT**0.5)+1):
    if is_prime[i]:
        for j in range(i*i, LIMIT+1, i):
            is_prime[j] = False

primes = [i for i, val in enumerate(is_prime) if val][:MAX_N]

# 累積和
acc = [0]
for p in primes:
    acc.append(acc[-1] + p)

for line in sys.stdin:
    n = int(line)
    if n == 0:
        break
    print(acc[n])