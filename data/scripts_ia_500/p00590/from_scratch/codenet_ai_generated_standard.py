import sys

MAX = 10000
prime = [True] * (MAX + 1)
prime[0] = prime[1] = False
for i in range(2, int(MAX**0.5) + 1):
    if prime[i]:
        for j in range(i*i, MAX+1, i):
            prime[j] = False

for line in sys.stdin:
    N = line.strip()
    if not N.isdigit():
        continue
    N = int(N)
    count = 0
    for i in range(1, N+1):
        if prime[i] and prime[N - i + 1]:
            count += 1
    print(count)