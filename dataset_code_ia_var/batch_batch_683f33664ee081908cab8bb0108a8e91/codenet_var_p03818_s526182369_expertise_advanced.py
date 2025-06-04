def main():
    from sys import stdin
    N, *A = map(int, stdin.read().split())
    k = len({*A})
    print(k if k & 1 else k - 1)

if __name__ == "__main__":
    main()