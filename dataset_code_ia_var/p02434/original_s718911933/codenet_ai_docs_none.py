n, q = map(int, input().split())
A = [[] for _ in range(n)]
for _ in range(q):
    op, t, x = (input() + ' 1').split()[:3]
    if op == '0':
        A[int(t)].append(x)
    elif op == '1':
        print(*A[int(t)])
    else:
        A[int(t)] = []