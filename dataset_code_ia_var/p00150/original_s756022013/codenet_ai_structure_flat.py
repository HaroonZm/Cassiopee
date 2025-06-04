MAX = 10001
SQRT = 100
prime = [True] * MAX
for i in range(4, MAX, 2):
    prime[i] = False
for i in range(3, SQRT, 2):
    if prime[i]:
        j = i * i
        while j < MAX:
            prime[j] = False
            j += i
tbl = [0] * MAX
ans = 0
i = 5
while i < MAX:
    if prime[i] and prime[i-2]:
        ans = i
    tbl[i] = ans
    i += 2
while True:
    n = int(input())
    if n == 0:
        break
    if n % 2 == 0:
        n -= 1
    print(tbl[n] - 2, tbl[n])