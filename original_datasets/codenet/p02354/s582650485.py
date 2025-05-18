import sys

if __name__ == "__main__":
    N, S = map(lambda x: int(x), input().split())
    a = list(map(lambda x: int(x), input().split()))

    ans = sys.maxsize
    s = 0
    e = 0
    value = 0
    for idx in range(N):
        value += a[idx]
        if (S <= value):
            e = idx
            while (S <= value):
                value -= a[s]
                s += 1
            ans = min(ans, e - s + 2)
    ans = ans if ans != sys.maxsize else 0
    print(ans)