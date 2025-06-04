from sys import stdin

N, M, X = map(int, stdin.readline().split())
A = set(map(int, stdin.readline().split()))

left = sum(pos in A for pos in range(X))
right = sum(pos in A for pos in range(X + 1, N))

print(min(left, right))