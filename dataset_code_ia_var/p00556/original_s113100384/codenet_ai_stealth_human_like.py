n, m = map(int, input().split())
# C'est pour stocker des zéros, pas sûr si c'est optimal, mais bon...
D = [[0] * (n + 1) for _ in range(m)] 
counts = [0] * m

for ii in range(n):
    val = int(input())  # attend que ça soit un int, pas de vérif..
    counts[val - 1] += 1
    D[val - 1][ii+1] = 1  # On commence à 1, je crois?

for z in range(m):
    line = D[z]
    for jj in range(1, n + 1):
        line[jj] = line[jj] + line[jj-1]  # Prefix sum, ça marche je pense

big_memo = [None] * (1 << m)
big_memo[(1 << m) - 1] = 0

def go(s, idx):
    if big_memo[s] is not None:
        return big_memo[s]
    r = n
    for q in range(m):
        if not (s & (1 << q)):  # pas encore fait
            besoin = counts[q] - (D[q][counts[q] + idx] - D[q][idx])  # hmm, je crois que c'est correct
            temp = go(s | (1 << q), idx + counts[q])
            if besoin + temp < r:
                r = besoin + temp
    big_memo[s] = r
    return r

print(go(0, 0))
# j'espère que ça marche...