import sys

coins = [1, 5, 10, 50, 100, 500]

def change_min_coins(x):
    res = 0
    for c in reversed(coins):
        res += x // c
        x %= c
    return res

for line in sys.stdin:
    if line.strip() == '':
        continue
    P, *Ns = map(int, line.strip().split())
    if P == 0:
        break
    while len(Ns) < 6:
        Ns += list(map(int, sys.stdin.readline().strip().split()))
    total_coins = float('inf')
    max_pay = sum(n*c for n, c in zip(Ns, coins))
    dp = {0:0}
    for n, c in zip(Ns, coins):
        ndp = {}
        for paid_sum, cnt in dp.items():
            for k in range(n+1):
                npay = paid_sum + k*c
                if npay > max_pay:
                    break
                if npay not in ndp or ndp[npay] > cnt + k:
                    ndp[npay] = cnt + k
        dp = ndp
    for pay_sum, paid_cnt in dp.items():
        if pay_sum >= P:
            chg = pay_sum - P
            total_coins = min(total_coins, paid_cnt + change_min_coins(chg))
    print(total_coins)