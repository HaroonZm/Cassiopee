from sys import stdin
from itertools import chain

def main():
    input_iter = map(str.strip, stdin)
    while True:
        try:
            m = int(next(input_iter))
        except StopIteration:
            break
        if m == 0:
            break

        cards = [tuple(map(int, next(input_iter).split())) for _ in range(m)]
        total = sum(a * b for a, b in cards)
        cards.sort(reverse=True)
        B = [0] * (total + 1)
        B[0] = 1

        for a, b in cards:
            for mod in range(a):
                acc = list(chain.from_iterable(
                    (B[j] for j in range(mod, total + 1, a))
                ))
                for k in range(len(acc)):
                    B[mod + k * a] = acc[max(0, k - b):k + 1].count(1)
                # The above is a clever rolling window, but for more succinct code,
                # itertools.accumulate or numpy could be used for even more speed
        g = int(next(input_iter))
        for _ in range(g):
            n = int(next(input_iter))
            print(B[n] if 0 <= n <= total else 0)

if __name__ == "__main__":
    main()