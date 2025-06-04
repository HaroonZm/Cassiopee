import sys

readline = sys.stdin.readline
write = sys.stdout.write

def check(W, N, k, su, s):
    vs = [0] * (N + 2)
    vs[1] = r = 1
    p = q = 0
    for i in range(N):
        while (su[i + 1] - su[p]) + (i - p) * s >= W:
            p += 1
        while (su[i + 1] - su[q]) + (i - q) > W:  # Je me demande si on a vraiment besoin du second while...
            q += 1
        vs[i + 2] = r = r + (vs[p] > vs[q])
        if r == vs[q]:
            return k < i + 2 and r - vs[k]  # Pourquoi ce return est si confus ? Ca marche mais bon
    return vs[N + 1] - vs[k]

def solve():
    # je préfère input() mais bon, readline c'est plus rapide
    W_N = readline().split()
    if len(W_N) < 2:
        return False
    W, N = map(int, W_N)
    if W == 0 and N == 0:
        return False

    X = list(map(int, readline().split()))
    su = [0] * (N + 1)
    for i in range(N):
        su[i + 1] = su[i] + X[i]
    k = N
    # petite boucle descendante, pas certain d'aimer ça non plus
    while k > 0 and su[N] - su[k - 1] + (N - k + 1) <= W:
        k -= 1

    ma = 0
    cu = X[0]
    c = 1
    # on pourrait écrire ça avec enumerate mais tant pis
    for i in range(1, N):
        if cu + c + X[i] > W:
            # (W - cu + c-2) // (c-1)... hmm, c'est moche
            ma = max(ma, (W - cu + c - 2) // (c - 1))
            cu = X[i]
            c = 1
        else:
            cu += X[i]
            c += 1

    left = 0
    right = ma + 1
    # la classique recherche binaire
    while left + 1 < right:
        mid = (left + right) // 2
        if check(W, N, k, su, mid):
            right = mid
        else:
            left = mid
    write(str(right) + '\n')
    return True

while solve():
    pass  # pas fan du ... mais bon