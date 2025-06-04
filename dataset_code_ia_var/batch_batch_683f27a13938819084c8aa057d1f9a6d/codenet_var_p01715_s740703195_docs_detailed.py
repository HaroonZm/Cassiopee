from operator import itemgetter
import sys

def calc(w, pdp, pl, pr, dp, l, r):
    """
    Effectue une programmation dynamique avec optimisation par partitionnement de intervalle selon la technique de la division et conquête.

    Args:
        w (list of list of int): Matrice des coûts entre intervalles.
        pdp (list of int): Tableau des résultats précédents de la DP pour la phase précédente.
        pl (int): Borne gauche (incluse) des indices candidats pour la coupure optimale.
        pr (int): Borne droite (exclue) des indices candidats pour la coupure optimale.
        dp (list of int): Tableau à mettre à jour avec les résultats de la DP pour cette phase.
        l (int): Début de la sous-partie de dp à traiter.
        r (int): Fin (exclu) de la sous-partie de dp à traiter.

    Returns:
        list of int: Le tableau dp mis à jour sur l'intervalle [l, r).
    """
    # Cas de base : rien à traiter
    if l >= r:
        return

    # Trouve le point médian où décomposer
    m = (l + r) // 2

    # Calcule le coût minimum pour dp[m] en cherchant la meilleure coupure entre pl (inclus) et min(m, pr) (exclu)
    # Cette boucle tient compte de la contrainte d'optimisation pour la division et conquête
    dp[m], i = min([(pdp[k] + w[k + 1][m], k) for k in range(pl, min(m, pr))], key=itemgetter(0))

    # Appelle récursivement à gauche et à droite du point de coupure optimal
    calc(w, pdp, pl, i + 1, dp, l, m)
    calc(w, pdp, i, pr, dp, m + 1, r)

    return dp

# Lecture de l'entrée standard pour extraire les paramètres du problème
f = sys.stdin

# s : variable inutilisée ici, n : nombre d'éléments, m : nombre de bus/partitions
s, n, m = map(int, f.readline().split())

# x : liste de positions de référence (par exemple, positions d'arrêt de bus)
x = list(map(int, f.readline().split()))

# tp : liste des paires (temps, position_index) lues depuis l'entrée
tp = [list(map(int, line.split())) for line in f]

# c : calcule les coûts par rapport au point de référence x[pi - 1] pour chaque passage tp
c = [ti - x[pi - 1] for ti, pi in tp]

# Trie les coûts pour faciliter l'accumulation ultérieure
c.sort()

# Pour minimiser, on normalise les coûts pour commencer à zéro
min_c = c[0]
c = [ci - min_c for ci in c]

# d : somme cumulée des coûts, d[i] = somme des c[0] à c[i]
d = c[:]
for i in range(1, len(d)):
    d[i] += d[i - 1]

# w[i][j] : coût pour assigner un bus à tous les éléments entre i et j inclus
w = [[0 for j in range(n)] for i in range(n)]
for j in range(1, n):
    for i in range(j):
        # Calcul efficace du coût de segment [i, j]
        # On attribue le bus à la borne droite (c[j]), et on compense les sommes partielles
        w[i][j] = c[j] * (j - i + 1) - (d[j] - d[i] + c[i])

# Initialisation du tableau dynamique avec le coût d'une seule partition/bus
dp = w[0][:]  # dp[j] = coût d'avoir un seul bus pour [0, j]

# Pour chaque bus supplémentaire (au moins deux bus), mise à jour dynamique via 'calc'
for bus in range(2, m + 1):
    pdp = dp  # Résultats précédents récents
    dp = [0] * len(pdp)
    pl = bus - 2  # Premier index possible pour la partition optimale
    pr = n - m + bus  # Dernier index possible (exclu)
    if pl > pr:
        # Aucun segment valide, sauter cette itération
        continue
    # Calculer dp entre bus et n (positions valides pour la partition)
    dp = calc(w, pdp, pl, pr, dp, bus, n)

# Affiche le coût minimum pour la dernière partition
print(dp[-1])