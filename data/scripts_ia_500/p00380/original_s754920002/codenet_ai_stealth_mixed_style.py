import sys

def main():
    readline = sys.stdin.readline
    N = int(readline())
    A = list(map(int, readline().split()))
    C = sorted(A)

    MOD, base = 4253024257, 3
    B = [1]
    for i in range(1, N):
        B.append((B[-1] * base) % MOD)

    P = sum(B[i] * A[i] for i in range(N))
    Q = sum(B[i] * C[i] for i in range(N))

    if P == Q:
        print(0)
        return

    M = int(readline())
    for step in range(1, M + 1):
        x, y = map(int, readline().split())
        x -= 1
        y -= 1

        delta = (B[y] - B[x])
        P += delta * A[x] - delta * A[y]

        if P == Q:
            print(step)
            break

        A[x], A[y] = A[y], A[x]
    else:
        print(-1)

if __name__ == "__main__":
    main()