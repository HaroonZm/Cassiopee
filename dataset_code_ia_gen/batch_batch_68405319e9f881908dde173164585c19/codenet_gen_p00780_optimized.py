import sys

MAX = 2**15
sieve = [True]*(MAX+1)
sieve[0] = sieve[1] = False
for i in range(2,int(MAX**0.5)+1):
    if sieve[i]:
        for j in range(i*i,MAX+1,i):
            sieve[j] = False

for line in sys.stdin:
    n = int(line)
    if n == 0:
        break
    count = 0
    for p in range(2, n//2+1):
        if sieve[p] and sieve[n-p]:
            count += 1
    print(count)