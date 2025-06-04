import math

def main():
    # Lecture des entrées
    N_K = input().split()
    N = int(N_K[0])
    K = int(N_K[1])

    mod = 10**9 + 7

    if N < K:
        print(0)
        return
    elif N == K:
        print(math.factorial(N) % mod)
        return

    ans = 0
    cm = 1
    for i in range(K):
        # (-1)**i * cm * (K-i)^N % mod
        term = ((-1)**i) * cm * pow(K - i, N, mod)
        ans += term
        ans %= mod
        # Mise à jour du coefficient binomial
        cm = cm * (K - i) // (i + 1)

    print(ans)

main()