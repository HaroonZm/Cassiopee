def solve():
    N, M = map(int, input().split())

    if N == 1 and M == 1:
        print(1)
        return

    if N == 1:
        print(M-2)
        return

    if M == 1:
        print(N-2)
        return

    print((N-2) * (M-2))

if __name__ == "__main__":
    solve()