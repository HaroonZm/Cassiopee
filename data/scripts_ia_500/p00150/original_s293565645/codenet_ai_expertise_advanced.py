MAX = 10_000
prime = [False, False] + [True] * (MAX - 2)

for i in range(4, MAX, 2):
    prime[i] = False
for i in range(3, int(MAX**0.5) + 1, 2):
    if prime[i]:
        prime[i*i:MAX:i] = [False] * len(prime[i*i:MAX:i])

while (n := int(input())) != 0:
    n -= n % 2 == 0
    while not (prime[n] and prime[n - 2]):
        n -= 2
    print(n - 2, n)