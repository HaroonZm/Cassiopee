from sys import stdin
from operator import itemgetter

def main():
    lines = iter(stdin.read().splitlines())
    while True:
        try:
            n = int(next(lines))
            if n == 0:
                break
            y = float(next(lines))
            choix = (
                (b,
                 (y * (r / 100) + 1) if t == 1 else (r / 100 + 1) ** y)
                for b, r, t in (map(int, next(lines).split()) for _ in range(n))
            )
            print(max(choix, key=itemgetter(1))[0])
        except StopIteration:
            break

if __name__ == "__main__":
    main()