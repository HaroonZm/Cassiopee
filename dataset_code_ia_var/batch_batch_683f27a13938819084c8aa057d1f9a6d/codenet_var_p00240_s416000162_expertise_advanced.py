from sys import stdin
from itertools import islice

def main():
    input_iter = map(str.rstrip, stdin)
    while True:
        n = int(next(input_iter))
        if not n:
            break
        y = float(next(input_iter))
        banks = (tuple(map(int, ln.split())) for ln in islice(input_iter, n))
        def calc(b, r, t):
            r_ = r / 100
            return y * r_ + 1 if t == 1 else (r_ + 1) ** y
        best = max(banks, key=lambda args: (calc(*args), args[0]))
        print(best[0])

if __name__ == "__main__":
    main()