def main():
    # Procédural à l'ancienne
    import sys
    vals = list(map(int, sys.stdin.readline().split()))
    res = lambda x, y: x*y
    product = res(vals[0], vals[1])
    class D:
        def __init__(self, n): self.n = n
        def to_other(self): return self.n/3.305785
    result = D(product).to_other()
    print(f"{result:.6f}")
main()