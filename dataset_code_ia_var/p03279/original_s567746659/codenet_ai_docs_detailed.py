import sys
from bisect import bisect_left

# Définition de la constante du modulo
MOD = 10**9 + 7

# Préparation du buffer de lecture rapide depuis l'entrée standard (stdin)
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

# Lecture des dimensions : N (taille de X), M (taille de Y)
N, M = map(int, readline().split())
# Lecture du tableau des valeurs X (taille N)
X = list(map(int, readline().split()))
# Lecture du tableau des valeurs Y (taille M)
Y = list(map(int, readline().split()))

# --- Début du prétraitement des intervalles ---
L = []  # Liste des décalages à gauche
R = []  # Liste des décalages à droite (servira pour la coordinate compression)
for x in X:
    # Recherche de la position d'insertion de x dans Y (liste triée)
    i = bisect_left(Y, x)
    # On considère seulement les éléments x strictement encadrés dans Y
    if i in [0, M]:
        continue
    # On récupère les deux bornes d'encadrement entourant x dans Y
    y0, y1 = Y[i-1:i+1]
    # On ajoute la différence (écart) à gauche et à droite dans L et R
    L.append(y0 - x)
    R.append(y1 - x)

# --- Début de la compression des coordonnées (coordinate compression) sur R ---
Rtoi = {val: idx for idx, val in enumerate(sorted(set(R)), 1)}
# Remplacement des valeurs originales de R par leurs indices compressés
R = [Rtoi[r] for r in R]

# Cas particulier : aucun intervalle valide trouvé, on retourne 1 comme résultat
if len(R) == 0:
    print(1)
    exit()

"""
Idée générale :
- On veut compter de combien de façons on peut sélectionner des sous-intervalles selon certains critères.
- Pour cela, on ordonne les intervalles (L, R) et on construit une DP (programmation dynamique) sur R.
- On utilise une Binary Indexed Tree (Fenwick Tree, BIT) pour optimiser le calcul de la DP des sous-intervalles.
"""

class BIT:
    """
    Binary Indexed Tree (Fenwick Tree) permettant de réaliser
    efficacement les opérations de préfixes et d'ajouts.

    Attributs
    ----------
    size : int
        La taille maximale de l'arbre (+1 car l'indice 0 n'est pas utilisé).
    tree : list of int
        L'arbre des préfixes.
    """
    def __init__(self, max_n):
        """
        Initialise l'arbre BIT.

        Paramètres
        -----------
        max_n : int
            L'indice maximal géré par l'arbre (doit correspondre au max des indices compressés sur R).
        """
        self.size = max_n + 1    # taille du tableau BIT (indice 0 non utilisé)
        self.tree = [0] * self.size

    def get_sum(self, i):
        """
        Calcule la somme partielle de 1 à i dans l'arbre.

        Paramètres
        -----------
        i : int
            L'indice jusqu'où on souhaite calculer la somme préfixe.

        Retourne
        --------
        s : int
            La somme totale des éléments de 1 à i.
        """
        s = 0
        while i:
            s += self.tree[i]
            i -= i & -i   # Descend à l'indice parent du BIT
        return s

    def add(self, i, x):
        """
        Incrémente la valeur à l'indice i de l'arbre par x.

        Paramètres
        ----------
        i : int
            Indice auquel ajouter la valeur (doit être >= 1).
        x : int
            Valeur à ajouter.
        """
        while i < self.size:
            self.tree[i] += x
            i += i & -i   # Monte à l'indice suivant du BIT

# Initialisation de la Binary Indexed Tree pour le DP
dp = BIT(max_n=max(R))

# On traite chaque intervalle (L, R) unique, par L décroissant (ordre reverse)
for _, r in sorted(set(zip(L, R)), reverse=True):
    # Calcul du nombre de façons de constituer une suite finissant avant r
    x = dp.get_sum(r - 1) + 1    # +1 pour compter l'intervalle actuel lui-même
    x %= MOD
    dp.add(r, x)                 # On ajoute cette valeur à la position r

# Le résultat final est la somme de toutes les façons de finir (tous les r) + 1
answer = 1 + dp.get_sum(max(R))
answer %= MOD
print(answer)