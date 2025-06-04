from sys import stdin

def main():
    n = int(stdin.readline())
    a, b = map(int, stdin.readline().split())
    n %= 12

    from itertools import islice, cycle

    ops = [lambda a, b: (a - b, b), lambda a, b: (a, a + b)]
    it = islice(cycle(ops), n)
    for op in it:
        a, b = op(a, b)

    print(a, b)

if __name__ == "__main__":
    main()