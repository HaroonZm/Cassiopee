import sys
import math
input = sys.stdin.readline

N = int(input())
t = [int(input()) for _ in range(N)]
max_t = max(t)
freq = [0]*(max_t+1)
for x in t:
    freq[x] += 1

# Pré-calcul des fréquences cumulées des multiples pour chaque k
cumulative = [0]*(max_t+1)
for k in range(1, max_t+1):
    s = 0
    for multiple in range(k, max_t+1, k):
        s += freq[multiple]
    cumulative[k] = s

min_sum = float('inf')
for k in range(1, max_t+1):
    if cumulative[k] == N:
        total_inc = 0
        for x in t:
            rem = (x + k -1)//k * k - x
            total_inc += rem
            if total_inc >= min_sum:
                break
        if total_inc < min_sum:
            min_sum = total_inc
print(min_sum)