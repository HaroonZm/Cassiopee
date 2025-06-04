from sys import stdin

def main():
    readline = stdin.readline
    n, a, b = map(int, readline().split())
    x = list(map(int, readline().split()))

    ans = sum(
        min(a * d, b)
        for d in map(lambda i: x[i+1] - x[i], range(n-1))
    )

    print(ans)

if __name__ == "__main__":
    main()