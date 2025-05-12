import math
N = int(input())
A = sorted([int(X) for X in input().split()])
GCDA = A[0]
for T in range(1,N):
    GCDA = math.gcd(GCDA,A[T])
    if GCDA==1: break
print(GCDA)