import sys

INF = 2**31 - 1
line = sys.stdin.readline()
n, q = map(int, line.split())
tmp = 1
while tmp < n:
    tmp *= 2
size = tmp * 2
A = [INF] * (2 * size - 1)
for _ in range(q):
    line = sys.stdin.readline()
    if line[0] == "0":
        com, s, t, x = map(int, line.split())
        stack = [(0, 0, size, s, t+1, x)]
        while stack:
            k, l, r, a, b, v = stack.pop()
            if r <= a or b <= l:
                continue
            if a <= l and r <= b:
                if v >= 0:
                    A[k] = v
                continue
            if A[k] != INF:
                A[2*k+1] = A[2*k+2] = A[k]
            A[k] = INF
            m = (l + r) // 2
            stack.append((2*k+1, l, m, a, b, v))
            stack.append((2*k+2, m, r, a, b, v))
    else:
        com, i = map(int, line.split())
        stack = [(0, 0, size, i, i+1, -1)]
        while stack:
            k, l, r, a, b, v = stack.pop()
            if r <= a or b <= l:
                continue
            if a <= l and r <= b:
                if v >= 0:
                    A[k] = v
                continue
            if A[k] != INF:
                A[2*k+1] = A[2*k+2] = A[k]
            A[k] = INF
            m = (l + r) // 2
            stack.append((2*k+1, l, m, a, b, v))
            stack.append((2*k+2, m, r, a, b, v))
        print(A[i+size-1])