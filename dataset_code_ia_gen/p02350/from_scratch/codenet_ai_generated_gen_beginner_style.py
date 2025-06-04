n, q = map(int, input().split())
A = [2147483647] * n

for _ in range(q):
    query = input().split()
    if query[0] == '0':
        _, s, t, x = query
        s = int(s)
        t = int(t)
        x = int(x)
        for i in range(s, t+1):
            A[i] = x
    else:
        _, s, t = query
        s = int(s)
        t = int(t)
        print(min(A[s:t+1]))