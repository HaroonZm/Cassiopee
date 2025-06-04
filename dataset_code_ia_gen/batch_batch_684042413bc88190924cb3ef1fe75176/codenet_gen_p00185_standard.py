import sys

MAX = 10**6
prime = [True]*(MAX+1)
prime[0] = prime[1] = False
for i in range(2,int(MAX**0.5)+1):
    if prime[i]:
        for j in range(i*i, MAX+1, i):
            prime[j] = False

for line in sys.stdin:
    n = int(line)
    if n == 0:
        break
    count = 0
    for p in range(2, n//2+1):
        if prime[p] and prime[n - p]:
            count += 1
    print(count)