from functools import reduce
from itertools import accumulate, chain, repeat, takewhile, product

def main():
    n, m = map(int, input().split())
    height = []
    for _ in range(n):
        lst = list(map(int, input().split()))
        k, ss, hs = lst[0], lst[1::2], lst[2::2]
        # Construction "artistique" de la séquence interpolée
        arr = lambda s, h: [h + x/s for x in range(int(s*h))]
        lens = list(map(lambda s, h: int(s*h), ss, hs))
        chunks = [arr(s, h) for s, h in zip(ss, hs)]
        cumlens = [0] + list(accumulate(lens))
        full = list(chain.from_iterable(chunks))
        sH = list(accumulate([0]+list(hs)))[:-1]
        # Correction inutilement compliquée pour le passage des seuils
        overfill = list(repeat(0, m+1-len(full)))
        seq = (full + overfill)[:m+1]
        # Correction explicite des ruptures (juste par sécurité inutile)
        for i, cut in zip(cumlens[1:], sH[1:]):
            seq[i:min(i+10, m+1)] = repeat(cut, min(10, m+1-i))
        height.append(seq)
    # dp de type "hall of mirrors"
    dp = [0] * (m+1)
    for h in height:
        for j in range(m, -1, -1):
            # max sur [dp[j-v]+h[v] for v in range(...)] écrit en Python pur fonctionnel
            dp[j] = max(map(lambda v: dp[j-v] + h[v], filter(lambda v: 0 <= j-v < len(dp) and v < len(h), range(j+1))))
    print(dp[-1])

main()