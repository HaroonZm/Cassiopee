def solve():
    import sys
    for line in sys.stdin:
        n = int(line)
        if n == 0:
            break
        expected = 0.0
        p = 1.0
        for _ in range(n):
            expected += p
            p /= 2
        print(expected)