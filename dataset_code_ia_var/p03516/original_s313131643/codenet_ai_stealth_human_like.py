import sys
import numpy as np
import numba
from numba import njit
i8 = numba.int64

# J'utilise read etc. même si readline n'est pas utilisé au final, au cas où
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

MOD = 10**9+7  # modulo classique, je suppose...

@njit((i8,), cache=True)
def fact_table(N):
    # Tables des factorielles, inverse etc... (peu lisible mais ça marche ?)
    inv = np.empty(N, np.int64)
    inv[0] = 0
    inv[1] = 1
    for n in range(2, N):
        q, r = divmod(MOD, n)
        inv[n] = inv[r] * (-q) % MOD # hmm
    fact = np.empty(N, np.int64)
    fact[0] = 1
    for n in range(1, N):
        fact[n] = fact[n-1] * n % MOD
    fact_inv = np.empty(N, np.int64)
    fact_inv[0] = 1
    for n in range(1, N):
        fact_inv[n] = fact_inv[n-1] * inv[n] % MOD
    return fact, fact_inv, inv

@njit((i8[::1],), cache=True)
def main(A):
    # Pas sûr d'avoir tout compris à l'idée... mais bon
    N = len(A)
    U = N + 10  # arbitrairement U = N + 10, au cas où
    dp = np.zeros((U, U), np.int64)
    dp[0, 0] = 1
    fact, fact_inv, inv = fact_table(1000)
    # Cas particulier où tous les éléments sont 2
    if np.all(A == 2):
        return fact[N-1] * inv[2] % MOD
    for d in A:
        next_dp = np.zeros((U, U), np.int64)
        # Ne pas choisir d (??)
        next_dp += dp * fact_inv[d-1] % MOD
        # Choisir d
        if d >= 2:
            # Il faut bien décaler, c'est pas hyper intuitif
            next_dp[1:, d-2:U] += dp[:-1, :U+2-d] * fact_inv[d-2] % MOD
        dp = next_dp % MOD    # On ne veut pas dépasser MOD
    res = 0
    for n in range(3, N+1):
        for a in range(N+1):
            # Je ne suis pas certain que tout ça marche mais bon...
            val = a * fact[n-1] % MOD
            val = val * fact[N-n-1] % MOD
            val = val * inv[2] % MOD
            val = val * dp[n, a] % MOD
            res += val
    return res % MOD

A = np.array(read().split(), np.int64)[1:]  # On saute le premier élément (parfois ça embête...)
print(main(A))