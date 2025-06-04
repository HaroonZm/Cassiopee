MAX = 10000
SQRT = 100
prime = [True for i in range(MAX)]
for i in range(4, MAX, 2):
    prime[i] = False
i = 3
while i < SQRT:
    if prime[i]:
        j = i * i
        while j < MAX:
            prime[j] = False
            j += i
    i += 2
while True:
    n = int(input())
    if n == 0:
        break
    if n % 2 == 0:
        n -= 1
    while not prime[n] or not prime[n - 2]:
        n -= 2
    print(n - 2, n)