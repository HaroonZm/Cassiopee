if __name__ == "__main__":
    n, k = map(lambda x: int(x), input().split())
    ans = 0
    if n <= k:
        ans = 1
    print(ans)