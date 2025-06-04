import sys

input = sys.stdin.readline

MAX = 10**6
phi = [i for i in range(MAX+1)]
for i in range(2, MAX+1):
    if phi[i] == i:
        for j in range(i, MAX+1, i):
            phi[j] -= phi[j] // i

prefix = [0] * (MAX+1)
for i in range(1, MAX+1):
    prefix[i] = prefix[i-1] + phi[i]

t = int(input())
for _ in range(t):
    n = int(input())
    # nombre de termes dans F_n = 1 + sum_{k=1}^n phi(k)
    print(prefix[n] + 1)