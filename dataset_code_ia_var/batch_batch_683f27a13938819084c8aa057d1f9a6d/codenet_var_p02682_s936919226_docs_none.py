A, B, C, K = map(int, input().split())
if A >= K:
    print(K)
elif A+B >= K:
    print(A)
elif A+B+C <= K:
    print(A - C)
else:
    print(A - (K-A-B))