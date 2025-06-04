import math

N = int(input())
P = list(map(int, input().split()))
Q = list(map(int, input().split()))

p = 0
q = 0

i = 0
while i < N:
    n = P[i] - 1
    j = 0
    while j < i:
        if P[j] < P[i]:
            n -= 1
        j += 1
    p += n * math.factorial(N - (i + 1))
    i += 1

i = 0
while i < N:
    n = Q[i] - 1
    j = 0
    while j < i:
        if Q[j] < Q[i]:
            n -= 1
        j += 1
    q += n * math.factorial(N - (i + 1))
    i += 1

print(abs(p - q))