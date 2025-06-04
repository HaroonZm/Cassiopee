n, q = map(int, input().split())
A = [0] * n

for _ in range(q):
    query = input().split()
    if query[0] == '0':
        s = int(query[1])
        t = int(query[2])
        x = int(query[3])
        for i in range(s-1, t):
            A[i] += x
    else:
        i = int(query[1])
        print(A[i-1])