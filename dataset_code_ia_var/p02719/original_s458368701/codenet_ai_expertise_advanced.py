from sys import stdin

def main():
    n, k = map(int, stdin.readline().split())
    mod = n % k
    print(min(n, mod, k - mod))

if __name__ == "__main__":
    main()