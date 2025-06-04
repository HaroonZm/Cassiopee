import sys

sys.setrecursionlimit(10 ** 8)

input = sys.stdin.readline

N = int(input())
A = [int(x) for x in input().split()]

ans = A[0]
for a in A[1:]:
    ans ^= a

for a in A:
    print(a ^ ans, end=" ")