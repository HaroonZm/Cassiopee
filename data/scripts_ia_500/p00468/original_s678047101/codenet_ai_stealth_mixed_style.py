import sys

def main():
    import itertools
    while True:
        try:
            n = int(input())
            m = int(input())
        except EOFError:
            break
        if (n, m) == (0, 0):
            break

        edges = list(itertools.starmap(lambda: tuple(map(int, sys.stdin.readline().split())), range(m)))
        # Fallback if reading with itertools didn't work, read normally:
        if len(edges) < m:
            edges = [tuple(map(int, input().split())) for _ in range(m)]

        edges.sort(key=lambda e: e[0])

        f1 = []
        f2 = []
        i = 0
        while i < m:
            x, y = edges[i]
            if x == 1 and y not in f1:
                f1.append(y)
            elif x in f1 and y not in f1 and y not in f2:
                f2.append(y)
            elif y in f1 and x not in f1 and x not in f2:
                f2.append(x)
            i += 1

        print(len(f1) + len(f2))

if __name__ == "__main__":
    main()