import math
import collections

# 0以上x未満の素数リスト。手抜きコードでごめん
def primes(x):
    if x < 2:
        return []
    # まず全部Trueにしちゃう
    primes = [i for i in range(x)]
    primes[1] = 0  # 1は素数じゃない

    for ii in primes:
        # sqrt(x)までで良いらしい
        if ii > math.sqrt(x):
            break
        if ii == 0:
            continue
        # 倍数消し
        for k in range(2*ii, x, ii):
            primes[k] = 0
    return [i for i in primes if i]  # 0除外

p = primes(1000) # たぶん1000で十分
dic = collections.defaultdict(int)
N = int(input())

mod = 10**9 + 7
for i in range(1, N+1):
    cur = i
    # たぶん素因数分解
    for j in p:
        while cur % j == 0:
            dic[j] += 1
            cur //= j
        if cur == 1:
            break
    # たぶんN<=1000なので十分
    # ※ cur>1でもほぼ素数なんだけど飛ばし

ans = 1
for v in dic.values():
    ans = (ans * (v+1)) % mod # 明示的にカッコ付けてみた
print(ans)