def main():
    n, k = map(int, input().split())
    if n > k:
        print(0)
        return
    mod = 10 ** 9 + 7
    ans = 1
    for i in range(n):
        ans *= k - i
        ans %= mod
    print(ans)

if __name__ == '__main__':
    main()