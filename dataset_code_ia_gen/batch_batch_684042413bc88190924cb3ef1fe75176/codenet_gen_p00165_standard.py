import sys
import bisect

MP = 999983
primes = []
is_prime = [True] * (MP + 1)
is_prime[0] = False
is_prime[1] = False
for i in range(2, int(MP**0.5) + 1):
    if is_prime[i]:
        for j in range(i*i, MP+1, i):
            is_prime[j] = False
primes = [i for i, val in enumerate(is_prime) if val]

input = sys.stdin.readline
while True:
    n = int(input())
    if n == 0:
        break
    count_by_p = {}
    for _ in range(n):
        p,m = map(int,input().split())
        left = bisect.bisect_left(primes, max(0,p-m))
        right = bisect.bisect_right(primes, min(MP,p+m))
        X = right - left
        if p in count_by_p:
            count_by_p[p] += X
        else:
            count_by_p[p] = X
    king_cost = 0
    for p,total_X in count_by_p.items():
        if total_X == 0:
            # X=0, no payout, 1 prime goes to king’s fund
            king_cost += 1
        else:
            king_cost += total_X - 1
    print(king_cost)