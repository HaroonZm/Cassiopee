import sys

def fibonacci(N, M):
    # This function calculates the N-th Fibonacci number modulo M using matrix exponentiation
    # But here, we'll write it in a simple non-recursive way
    a, b = 0, 1
    for _ in range(N):
        a, b = b, (a + b) % M
    return a

def main():
    MOD = 10**9 + 7
    K = int(sys.stdin.readline())

    # Find k0 such that k0^2 + k0 <= K
    k0 = int((1 + 4*K)**0.5)
    k0 = (k0 - 1) // 2

    if k0*k0 + k0 == K:
        k0 -= 1

    kk = k0*k0 + k0

    if K - kk > k0 + 1:
        m0 = 2 * k0 + 1
        b = K - kk - (k0 + 1) - 1
    else:
        m0 = 2 * k0
        b = K - kk - 1

    if k0 // 2 + 1 > b:
        v1 = fibonacci(2 + 2*b, MOD)
        v2 = fibonacci(m0 + 2 - 2*b, MOD)
        v = (v1 * v2) % MOD
    else:
        b1 = k0 + 1 - b - 1
        v1 = fibonacci(3 + 2*b1, MOD)
        v2 = fibonacci(m0 + 1 - 2*b1, MOD)
        v = (v1 * v2) % MOD

    print(v)

main()