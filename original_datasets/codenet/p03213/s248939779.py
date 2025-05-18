import sys
from collections import defaultdict

input = sys.stdin.readline
INF = float('inf')
MOD = 10 ** 9 + 7

def inpl(): return list(map(int, input().split()))

N = int(input())

prime_cnt = defaultdict(int)
for n in range(N):
    n += 1
    i = 2
    while i * i <= n:
        if n % i == 0:
            cnt = 0
            while n % i == 0:
                cnt += 1
                n //= i
            prime_cnt[i] += cnt
        i += 1

    if n != 1:
        # nに素数が残っている場合処理をする
        prime_cnt[n] += 1

def num(n):
    cnt = 0
    for key in prime_cnt.keys():
        if prime_cnt[key] >= n - 1:
            cnt += 1

    return cnt

# 75 -> 3*5*5, 3*25, 5*15, 75
# 2^4*3^4*5^2と3^4*2^4*5^2は同じ，(重複の数)!で割る
print(num(75) + num(15) * (num(5) - 1) + num(25) * (num(3) - 1)
      + num(5) * (num(5) - 1) * (num(3) - 2) // 2)