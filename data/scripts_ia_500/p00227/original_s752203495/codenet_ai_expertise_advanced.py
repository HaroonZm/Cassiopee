import sys

for line in sys.stdin:
    try:
        n, m = map(int, line.split())
        if n == 0:
            break
        v = sorted(map(int, next(sys.stdin).split()), reverse=True)
        v[m-1:n:m] = [0] * len(v[m-1:n:m])
        print(sum(v))
    except (ValueError, StopIteration):
        continue