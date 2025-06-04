INITIAL = 2 ** 31 - 1

n, q = map(int, input().split())
V = [INITIAL] * n

sz = len(V)
N = 1
while N < sz:
    N *= 2
node = [INITIAL] * (2 * N - 1)
for i in range(sz):
    node[i + N - 1] = V[i]
for i in range(N - 2, 0, -1):
    node[i] = min(node[2 * i + 1], node[2 * i + 2])

for _ in range(q):
    com, x, y = map(int, input().split())
    if com:
        a = x
        b = y + 1
        stack = [(0, 0, N)]
        res = INITIAL
        while stack:
            k, l, r = stack.pop()
            if r <= a or l >= b:
                continue
            if l >= a and r <= b:
                res = min(res, node[k])
                continue
            mid = (l + r) // 2
            stack.append((2 * k + 2, mid, r))
            stack.append((2 * k + 1, l, mid))
        print(res)
    else:
        x_ = x + (N - 1)
        node[x_] = y
        while x_ > 0:
            x_ = (x_ - 1) // 2
            node[x_] = min(node[2 * x_ + 1], node[2 * x_ + 2])