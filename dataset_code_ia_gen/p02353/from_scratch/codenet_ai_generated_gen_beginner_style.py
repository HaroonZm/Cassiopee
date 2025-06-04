n, q = map(int, input().split())
A = [0] * n

for _ in range(q):
    query = list(map(int, input().split()))
    if query[0] == 0:
        _, s, t, x = query
        for i in range(s, t+1):
            A[i] = x
    else:
        _, s, t = query
        total = 0
        for i in range(s, t+1):
            total += A[i]
        print(total)