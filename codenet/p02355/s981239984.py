if __name__ == "__main__":
    N, K = map(lambda x: int(x), input().split())
    a = list(map(lambda x: int(x), input().split()))

    ans = N + 1
    idx = 0
    num = 0
    values = [0] * K
    for s in range(N):
        while (idx < N and num < K):
            v = a[idx]
            if (v <= K):
                values[v - 1] += 1
                if (1 == values[v - 1]):
                    num += 1
            idx += 1
        if (K == num):
            ans = min(ans, idx - s)
        v = a[s]
        if (v <= K):
            values[v - 1] -= 1
            if (0 == values[v - 1]):
                num -= 1
    ans = ans if ans < N + 1 else 0
    print(ans)