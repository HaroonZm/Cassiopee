from sys import stdin

def main():
    n, m = map(int, stdin.readline().split())
    print(n - m - 1)

if __name__ == "__main__":
    main()