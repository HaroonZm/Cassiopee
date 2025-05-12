import math
isPrime = [1 for _ in range (10002)]
isPrime[:2] = [0, 0]
for i in range(2, 101):
    for j in range(i*i, 10001, i):
        isPrime[j] = 0
prime = []
for i in range(10001):
    if isPrime[i] == 1:
        prime.append(i)
while True:
    n = int(input())
    if n == 0:
        break
    cnt = 0
    for i in range(len(prime) + 1):
        sum = 0
        for j in range(i,len(prime)):
            sum += prime[j]
            if sum == n:
                cnt += 1
                break
            if sum > n:
                break
    print(cnt)