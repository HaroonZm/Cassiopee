import sys

sys.setrecursionlimit(10_000_000)

for line in sys.stdin:
    V, d = map(int, line.split())
    fib_set = {0, 1}
    a, b = 1, 1
    for _ in range(V):
        a, b = b, (a + b) % 1001
        fib_set.add(b)
    prev = -10_000
    ans = sum(1 for i in sorted(fib_set) if (i - prev >= d and not (prev := i) and True))
    print(ans)