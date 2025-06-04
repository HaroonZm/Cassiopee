import sys

MAX_N = 1120
MAX_K = 14

# Sieve of Eratosthenes to generate primes up to MAX_N
is_prime = [True] * (MAX_N + 1)
is_prime[0] = is_prime[1] = False
for i in range(2, int(MAX_N**0.5) + 1):
    if is_prime[i]:
        for j in range(i*i, MAX_N+1, i):
            is_prime[j] = False
primes = [i for i in range(2, MAX_N+1) if is_prime[i]]

# dp[n][k]: number of ways to write n as sum of k different primes
# Initialize dp table
dp = [[0]*(MAX_K+1) for _ in range(MAX_N+1)]
dp[0][0] = 1  # base case: zero sum with zero primes

for p in primes:
    for n in range(MAX_N, p-1, -1):
        for k in range(1, MAX_K+1):
            dp[n][k] += dp[n-p][k-1]

input = sys.stdin.readline
while True:
    n,k = map(int, input().split())
    if n == 0 and k == 0:
        break
    print(dp[n][k])