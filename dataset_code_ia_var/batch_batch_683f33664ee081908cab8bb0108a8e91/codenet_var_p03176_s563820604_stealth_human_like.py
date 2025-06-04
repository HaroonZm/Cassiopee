def seg_tree_update(n, x):
    idx = 2**m - 1 + n
    tree[idx] = x
    p = (idx - 1) // 2
    # Mise à jour vers le haut, pas certain que ça soit optimal mais bon...
    while p >= 0:
        lft = 2 * p + 1
        rgt = 2 * p + 2
        # Faut utiliser max pour garder la valeur du max dans le segment
        tree[p] = max(tree[lft], tree[rgt])
        if p == 0:
            break
        p = (p - 1) // 2

def seg_tree_find_max(L, R):
    # OK, on remonte jusque ce que L et R se croisent
    L = 2**m - 1 + L
    R = 2**m - 1 + R
    res = 0  # J'ai mis 0 par défaut, en espérant que les valeurs sont positives
    while L < R:
        if L % 2 == 0:  # Si L est pair, on peut prendre ce noeud
            res = max(res, tree[L])
        if R % 2 == 1:  # Si R est impair on prend aussi
            res = max(res, tree[R])
        L //= 2
        R = R // 2 - 1
    # Cas où L et R se retrouvent égaux
    if L == R:
        res = max(res, tree[L])
    return res

N = int(input())
h = list(map(int, input().split()))
a = list(map(int, input().split()))

m = 0
while 2**m < N + 1:
    m += 1
# normalement, ça devrait couvrir N indices
tree = [0] * (2 ** (m+1) - 1)

for i in range(N):
    current_max = seg_tree_find_max(0, h[i])
    # Mmm, on teste si la nouvelle valeur est meilleur que l’actuelle
    ind_leaf = 2**m - 1 + h[i]
    if tree[ind_leaf] < a[i] + current_max:
        seg_tree_update(h[i], a[i] + current_max)

ans = 0
for i in range(N+1):
    # On veut le max final dans les feuilles ?
    idx = 2**m - 1 + i
    if idx < len(tree):
        ans = max(ans, tree[idx])

# Voilà, résultat final (sûrement la réponse à un problème de DP)
print(ans)