import sys

MOD = 10 ** 9 + 7

n, k = map(int, raw_input().split())

def fact(N):
    result = 1
    for i in range(2, N + 1):
        result *= i
    return result

def power(N):
    result = 1
    for i in range(n):
        result = (result * N) % MOD
    return result

C = 0
i = k - 1
while i > 0:
    numerator = fact(k)
    denominator = fact(i) * fact(k - i)
    combination = numerator // denominator
    total = combination * power(i)
    if (i - k) % 2 == 1:
        total = -total
    C += total
    i -= 1

answer = (power(k) + C) % MOD
print(answer)