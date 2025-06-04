from functools import lru_cache

def g(x):
    A = [380, 550, 850]
    B = [0.2, 0.15, 0.12]
    C = [5, 4, 3]
    return sum(a * (xi - (xi // c) * c * b)
               for a, b, c, xi in zip(A, B, C, x))

@lru_cache(maxsize=None)
def f(w1):
    m = float('inf')
    for i1 in range(w1 // 500 + 1):
        w2 = w1 - i1 * 500
        for i2 in range(w2 // 300 + 1):
            w3 = w2 - i2 * 300
            if w3 % 200 == 0:
                m = min(m, g((w3 // 200, i2, i1)))
    return m

def main():
    import sys
    for line in sys.stdin:
        w = int(line)
        if w == 0:
            break
        print(int(f(w)))

if __name__ == "__main__":
    main()