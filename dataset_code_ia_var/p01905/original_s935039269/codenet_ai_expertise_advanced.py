from sys import stdin

def main():
    n, m, *rest = map(int, stdin.read().split())
    print(n - m - 1)

if __name__ == "__main__":
    main()