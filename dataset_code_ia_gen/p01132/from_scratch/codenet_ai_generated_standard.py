import sys
from collections import deque

coins = [10, 50, 100, 500]

def coin_count(cnts):
    return sum(cnts)

def add_coins(a, b):
    return tuple(a[i] + b[i] for i in range(4))

def sub_coins(a, b):
    return tuple(a[i] - b[i] for i in range(4))

def leq(a, b):
    return all(a[i] <= b[i] for i in range(4))

def solve(pay, wallet):
    max_sum = sum(c*w for c,w in zip(coins, wallet))
    dp = {}
    # dp[(used_coins_tuple)] = minimal total coins after change
    # Using BFS to try all payment patterns
    # State: (used_coins_tuple)
    # Constraint: used_coins <= wallet
    # For each payment, change = usage_sum - pay
    # Change is given optimally from infinite coins
    # Condition: no coin type used both in pay and returned as change
    # For each usage tuple, compute usage_sum and usage_coin_count
    # Compute change = usage_sum - pay, minimal coins for change with unlimited coins
    # For minimal change coins, check which coins are used
    # if intersection of used coins and return coins is empty, valid
    # total = usage_coin_count + minimal change coins count
    # minimize total over all valid usage tuples

    # First, precompute change minimal coins and coins used for each amount <= max_sum
    INF = 10**9
    ch_mincoins = [INF]*(max_sum+1)
    ch_used = [set() for _ in range(max_sum+1)]
    ch_mincoins[0] = 0
    for x in range(max_sum+1):
        for i,c in enumerate(coins):
            if x+c <= max_sum and ch_mincoins[x]+1 < ch_mincoins[x+c]:
                ch_mincoins[x+c] = ch_mincoins[x]+1
                ch_used[x+c] = ch_used[x].copy()
                ch_used[x+c].add(coins[i])
    # BFS over usage of coins (avoid huge states, but wallet max 20 coins each)
    # Use nested loops, acceptably small 21**4=~200k
    best = INF
    ans = None
    for a in range(wallet[0]+1):
        for b in range(wallet[1]+1):
            for c_ in range(wallet[2]+1):
                for d in range(wallet[3]+1):
                    usage = [a,b,c_,d]
                    usage_sum = sum(u*co for u,co in zip(usage,coins))
                    if usage_sum < pay:
                        continue
                    change = usage_sum - pay
                    if ch_mincoins[change] == INF:
                        continue
                    # check intersection of coins used in usage and in change
                    used_coins_set = set(coins[i] for i,u in enumerate(usage) if u>0)
                    if used_coins_set & ch_used[change]:
                        continue
                    total_coins = sum(usage) + ch_mincoins[change]
                    if total_coins < best:
                        best = total_coins
                        ans = usage
    return ans

def main():
    input = sys.stdin.readline
    first = True
    while True:
        line = input()
        if not line:
            break
        pay = int(line)
        if pay == 0:
            break
        wallet = tuple(map(int,input().split()))
        usage = solve(pay,wallet)
        if not first:
            print()
        first = False
        for c,u in sorted(zip(coins,usage)):
            if u > 0:
                print(c,u)

if __name__ == '__main__':
    main()