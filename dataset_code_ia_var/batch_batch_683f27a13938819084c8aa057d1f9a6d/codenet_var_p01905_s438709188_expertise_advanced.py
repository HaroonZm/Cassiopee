from functools import lru_cache

def main():
    N, M = map(int, input().split())
    if M == 0:
        print(N - 1)
        return

    a = {int(input()) for _ in range(M)}

    @lru_cache(maxsize=None)
    def calc(l, n):
        if n == 2:
            has1, has2 = l in a, (l + 1) in a
            if has1 and has2:
                return 0, True
            if has1 or has2:
                return 0, False
            return 1, False

        m = n // 2
        c1, f1 = calc(l, m)
        c2, f2 = calc(l + m, m)
        if f1 and f2:
            return c1 + c2, True
        if f1 or f2:
            return c1 + c2, False
        return c1 + c2 + 1, False

    print(calc(0, N)[0])

if __name__ == "__main__":
    main()