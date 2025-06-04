import sys

input = sys.stdin.readline

N = int(input())
A = [int(a) for a in input().split()]
total = 0
for a in A:
    total ^= a
Ans = [-1] * N
for i in range(N):
    Ans[i] = total ^ A[i]
print(*Ans, sep=" ")