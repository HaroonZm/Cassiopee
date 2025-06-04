import sys

sys.setrecursionlimit(10000000)
input = lambda: sys.stdin.readline().rstrip()

def eratosthenes(n):
    prime_table = [False, False, True] + [False if i % 2 != 0 else True for i in range(n - 2)]
    i = 3
    primes = []
    while i * i <= n:
        if prime_table[i]:
            j = i * i
            while j <= n:
                prime_table[j] = False
                j += i
        i += 2
    for i in range(len(prime_table)):
        if prime_table[i]:
            primes.append(i)
    return primes

prime_table = eratosthenes(50001)
while True:
    m, a, b = map(int, input().split())
    if m == a == b == 0:
        break
    l = 0
    mx = (0, 0, 0)
    for r in range(len(prime_table)):
        while True:
            if mx[0] < prime_table[l] * prime_table[r] <= m and prime_table[l] / prime_table[r] >= a / b:
                mx = (prime_table[l] * prime_table[r], l, r)
            if prime_table[l] * prime_table[r] > m and l - 1 >= 0:
                l -= 1
            elif l + 1 <= r and (prime_table[l + 1]) * prime_table[r] <= m:
                l += 1
            else:
                break
    print(prime_table[mx[1]], prime_table[mx[2]])