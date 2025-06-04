import os
import sys

# Si la variable d'environnement LOCAL est définie, redirige l'entrée standard vers le fichier "_in.txt".
if os.getenv("LOCAL"):
    sys.stdin = open("_in.txt", "r")

# Définit la limite maximale de récursion pour éviter les erreurs de récursion profonde.
sys.setrecursionlimit(2147483647)

# Définition de constantes utiles :
INF = float("inf")      # Valeur représentant l'infini pour les flottants
IINF = 10 ** 18         # Valeur entière très grande
MOD = 10 ** 9 + 7       # Modulo classique pour les problèmes de type "reste de division" en programmation de compétition

def ModInt(mod):
    """
    Classe génératrice de nombres entiers modulaires.

    Cette fonction retourne une classe interne permettant d'exécuter des opérations arithmétiques
    (addition, soustraction, multiplication) sous un module spécifié. Utilisé pour garantir que
    les résultats des calculs ne dépassent jamais 'mod'.

    Paramètres :
        mod (int) : Le modulo à utiliser pour toutes les opérations.

    Retourne :
        type: Classe imbriquée _ModInt avec surcharge des opérateurs +, -, *, /
    """
    class _ModInt:
        def __init__(self, value):
            """
            Initialise l'objet _ModInt avec la valeur donnée, réduite modulo 'mod'.
            """
            self.value = value % mod

        def __add__(self, other):
            """
            Surcharge de l'opérateur d'addition.
            Permet d'additionner deux objets _ModInt, ou un _ModInt et un entier.
            """
            if isinstance(other, _ModInt):
                return _ModInt(self.value + other.value)
            else:
                return _ModInt(self.value + other)

        def __sub__(self, other):
            """
            Surcharge de l'opérateur de soustraction.
            Permet de soustraire deux objets _ModInt, ou un _ModInt et un entier.
            """
            if isinstance(other, _ModInt):
                return _ModInt(self.value - other.value)
            else:
                return _ModInt(self.value - other)

        def __radd__(self, other):
            """
            Surcharge de l'addition inversée (other + self).
            """
            return self.__add__(other)

        def __mul__(self, other):
            """
            Surcharge de l'opérateur de multiplication.
            Permet de multiplier deux objets _ModInt, ou un _ModInt et un entier.
            """
            if isinstance(other, _ModInt):
                return _ModInt(self.value * other.value)
            else:
                return _ModInt(self.value * other)

        def __truediv__(self, other):
            """
            Surcharge de l'opérateur de division réelle (/).
            Non implémenté pour l'instant.
            """
            # TODO: Implémentation de la division modulaire si nécessaire
            raise NotImplementedError("Division is not implemented yet.")

        def __repr__(self):
            """
            Représentation lisible à l'écran de l'objet _ModInt.
            """
            return str(self.value)

    return _ModInt

# Instanciation de la classe ModInt avec le modulo MOD
MI = ModInt(MOD)

# Lecture des entrées :
# N : nombre d'enfants (ou variables)
# C : degré maximal
N, C = list(map(int, sys.stdin.readline().split()))

# A et B : bornes inférieures et supérieures pour chaque variable
A = list(map(int, sys.stdin.readline().split()))
B = list(map(int, sys.stdin.readline().split()))

def solve():
    """
    Fonction principale de résolution.
    Calcule la somme multinomiale sur les plages données, modulo MOD.

    Pour chaque i de 0 à N-1, considère les entiers X[i] allant de A[i] à B[i].
    Pour tout c (degré total jusqu'à C), calcule la somme des puissances multinomiales de type :
    Somme de X[0]^c0 * X[1]^c1 * ... * X[N-1]^c(N-1), somme pour tout (c0+...+c(N-1)=C).

    Retourne :
        ModInt : Le résultat du calcul demandé, modulo MOD.
    """

    # Pré-calcul de P[n][c] = n^c pour tous les n <= max(B), c <= C
    P = [[1] * (C + 1) for _ in range(max(B) + 1)]
    P[0] = [MI(0)] * (C + 1)  # 0^c = 0 pour c > 0, et 0^0 traité séparément si besoin
    for i in range(1, len(P)):
        for c in range(1, C + 1):
            # Calcul en dynamique : n^c = n * n^(c-1)
            P[i][c] = P[i][c - 1] * i

    # Pré-calcul des sommes cumulées cs[n][c] = 0^c + 1^c + ... + n^c
    cs = [[0] * (C + 1) for _ in range(max(B) + 1)]
    for c in range(C + 1):
        s = 0  # Somme cumulée pour la puissance fixe c
        for i in range(len(P)):
            s += P[i][c]
            cs[i][c] = s

    # Calcul de S[i][c] : somme des X[i]^c pour X[i] dans [A[i], B[i]]
    S = [[0] * (C + 1) for _ in range(N)]
    for i in range(N):
        for c in range(C + 1):
            S[i][c] = cs[B[i]][c] - cs[A[i] - 1][c]

    # dp[c] : pour chaque degré total c, valeur totale sur les i premières variables
    dp = S[0][:]
    # Pour chaque variable supplémentaire, on effectue la mise à jour du DP :
    for i in range(1, N):
        # Parcours des degrés totaux du plus grand vers le plus petit
        for c in reversed(range(C + 1)):
            s = 0
            # Découpage en "partages" du degré entre dp et S
            for j in range(c + 1):
                s += dp[c - j] * S[i][j]
            dp[c] = s
    # Le résultat cherché est dp[C] (degré total maximal)
    return dp[-1]

# Exécution du solveur et affichage du résultat
print(solve())