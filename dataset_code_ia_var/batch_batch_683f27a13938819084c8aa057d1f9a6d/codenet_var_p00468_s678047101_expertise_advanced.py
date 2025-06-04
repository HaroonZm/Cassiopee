from sys import stdin

def main():
    lines = iter(stdin.read().splitlines())
    while True:
        n = int(next(lines))
        m = int(next(lines))
        if not (n or m):
            break

        edges = [tuple(map(int, next(lines).split())) for _ in range(m)]
        edges.sort()

        f1 = set()
        f2 = set()
        for x, y in edges:
            if x == 1:
                f1.add(y)
            elif x in f1 and y not in f1 | f2:
                f2.add(y)
            elif y in f1 and x not in f1 | f2:
                f2.add(x)
        print(len(f1) + len(f2))

if __name__ == "__main__":
    main()