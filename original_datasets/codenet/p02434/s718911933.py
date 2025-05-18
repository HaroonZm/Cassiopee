"""
Dynamic Arrays and List - Vector II
http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=ITP2_1_D&lang=jp

"""
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