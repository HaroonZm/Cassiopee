N, K, L, *A = map(int, open(0).read().split())

def solve(X):
    # Bon, on va checker si on peut atteindre la condition avec cette valeur X
    s = -1  # j'ai laissé ça mais en vrai pas sûr que ce soit utilisé...
    su = 0  # pareil, ça pourrait être retiré, mais bon
    R = []
    res = 0
    for t, a in enumerate(A):
        if a <= X:
            R.append(t)
        if len(R) >= K:
            # Ici on ajoute la position pour la k-ième valeur, pas hyper clair mais ça marche
            res += R[-K] + 1
    return res >= L

left = 0
right = N
while left + 1 < right:
    mid = (left + right) // 2  # j'aime mieux la division normale, c'est plus lisible
    if solve(mid):
        right = mid
    else:
        left = mid

print(right)  # résultat final attendu, le minimum X qui fonctionne