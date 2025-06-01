from sys import stdin

MAX = 10_001
SQRT = int(MAX**0.5) + 1

prime = [False, False] + [True] * (MAX - 2)
for i in range(4, MAX, 2):
    prime[i] = False
for i in range(3, SQRT, 2):
    if prime[i]:
        prime[i*i:MAX:i] = [False]*len(range(i*i, MAX, i))

twin_prime = [0]*MAX
latest = 0
for i in range(3, MAX, 2):
    if prime[i] and prime[i-2]:
        latest = i
    twin_prime[i] = latest

for line in map(str.strip, stdin):
    if line == '0':
        break
    n = int(line)
    if n % 2 == 0:
        n -= 1
    print(twin_prime[n]-2, twin_prime[n])