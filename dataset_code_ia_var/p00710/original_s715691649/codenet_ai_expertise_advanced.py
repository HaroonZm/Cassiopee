from sys import stdin

def main():
    lines = iter(stdin.read().splitlines())
    while True:
        n, r = map(int, next(lines).split())
        if n == 0 and r == 0:
            break
        yama = list(range(n, 0, -1))
        for _ in range(r):
            p, c = map(int, next(lines).split())
            # Use slice assignment for efficient in-place update
            yama = yama[p-1:p-1+c] + yama[:p-1] + yama[p-1+c:]
        print(yama[0])

if __name__ == '__main__':
    main()