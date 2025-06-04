import sys

sys.setrecursionlimit(10**7)

def main():
    input_fn = (line.rstrip() for line in sys.stdin)
    while True:
        n, h = map(int, next(input_fn).split())
        if n == 0:
            break
        marked = set()
        for _ in range(h):
            S, p1, p2 = next(input_fn).split()
            p1, p2 = int(p1), int(p2)
            match S:
                case 'xy':
                    marked.update((p1, p2, i) for i in range(1, n+1))
                case 'xz':
                    marked.update((p1, i, p2) for i in range(1, n+1))
                case 'yz':
                    marked.update((i, p1, p2) for i in range(1, n+1))
        print(n ** 3 - len(marked))

if __name__ == '__main__':
    main()