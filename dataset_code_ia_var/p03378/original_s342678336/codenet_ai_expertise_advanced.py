from collections import Counter

N, M, X = map(int, input().split())
A = set(map(int, input().split()))

right = sum(1 for i in range(X, N) if i in A)
left = sum(1 for i in range(X) if i in A)
print(min(left, right))