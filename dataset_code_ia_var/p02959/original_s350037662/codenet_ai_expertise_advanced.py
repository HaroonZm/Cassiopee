from sys import stdin

N = int(stdin.readline())
A = list(map(int, stdin.readline().split()))
B = list(map(int, stdin.readline().split()))

from itertools import islice

def calc_total(N, A, B):
    total = 0
    for i in range(N):
        delta = A[i] - B[i]
        if delta >= 0:
            total += B[i]
        else:
            total += A[i]
            rem = B[i] - A[i]
            avail = min(A[i+1], rem)
            total += avail
            A[i+1] -= avail
    return total

print(calc_total(N, A, B))