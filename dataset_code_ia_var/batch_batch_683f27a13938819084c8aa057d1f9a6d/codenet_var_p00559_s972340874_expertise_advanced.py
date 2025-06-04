from sys import stdin
from itertools import islice

def main():
    N, Q, S, T = map(int, stdin.readline().split())
    A = [int(next(stdin)) for _ in range(N + 1)]
    B = [A[i + 1] - A[i] for i in range(N)]

    # Precompute initial C efficiently using a generator expression
    C = sum(((S if B[i] > 0 else T) * abs(B[i])) for i in range(N))

    def delta(k, dx):
        b = B[k]
        b2 = B[k] + dx
        if b > 0:
            if b2 > 0:
                return -S * dx
            else:
                return -S * b + T * b2
        else:
            if b2 > 0:
                return -T * b + S * b2
            else:
                return -T * dx

    result = []
    for _ in range(Q):
        l, r, x = map(int, next(stdin).split())
        l -= 1
        if 0 <= l < N:
            d = delta(l, x)
            C += d
            B[l] += x
        if r < N:
            d = delta(r, -x)
            C += d
            B[r] -= x
        result.append(C)

    print('\n'.join(map(str, result)))

if __name__ == "__main__":
    main()