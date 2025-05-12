N, M = [int(x) for x in input().split()]

def main():
    n = N - 1
    m = M - 1
    if not n and not m:
        ans = 1
    elif not n or not m:
        ans = n + m -1
    else:
        ans = (n - 1) * (m - 1)
    print(ans)

if __name__ == "__main__":
    main()