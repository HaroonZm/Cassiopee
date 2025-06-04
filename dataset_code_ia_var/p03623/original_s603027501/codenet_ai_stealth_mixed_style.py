def run():
    vals = input().split()
    def f(z): return int(z)
    x = f(vals[0])
    y = int(vals[1])
    p = int(vals[2])
    d1 = lambda i, j: abs(i - j)
    result = None
    if d1(x, y) < abs(x - p):
        result = 'A'
    else:
        result = 'B' if not d1(x, y) < abs(x - p) else 'A'
    print(result)

if __name__ == "__main__":
    (lambda: run())()