# Importation de la fonction lru_cache depuis le module functools. 
# lru_cache est un décorateur qui mémorise les valeurs de retour des appels de fonction,
# ce qui permet d'éviter les recomputations inutiles (mémoïsation).
from functools import lru_cache

# Importation du module sys permettant notamment la gestion de l'entrée et de la sortie standard.
import sys

# Définition (redéfinition ici) de la fonction input.
# Cette version lit une ligne à partir de l'entrée standard (sys.stdin),
# puis enlève le dernier caractère (généralement '\n' pour le saut de ligne).
def input():
    return sys.stdin.readline()[:-1]

# Définition de la fonction solve qui calcule le coût minimal pour réduire 
# un nombre N à 0 avec des opérations évoluées.
# Les paramètres sont :
# N : nombre à réduire.
# A : coût d'une opération de division par 2.
# B : coût d'une opération de division par 3.
# C : coût d'une opération de division par 5.
# D : coût pour soustraire ou ajouter 1 au nombre.
def solve(N, A, B, C, D):
    # Utilisation du mémoïsation grâce au décorateur lru_cache afin d'éviter des recalculs inutiles.
    @lru_cache(None)
    def f(N):
        # Cas de base 1 : si N vaut 0, il n'y a rien à faire donc coût total = 0.
        if N == 0:
            return 0
        # Cas de base 2 : si N vaut 1, il suffit de faire une seule opération coûteuse D pour arriver à 0.
        if N == 1:
            return D
        # Si on réduit N à 0 uniquement en faisant des opérations de "-1" successives.
        # Cela coûte D pour chaque décrément, donc un total de D * N.
        ret = D * N

        # Aller plus loin : essayer les autres opérations en optimisant le nombre d'opérations et leurs coûts.

        #=== ESSAI AVEC LA DIVISION PAR 2 ===#
        # divmod retourne le quotient (q) et le reste (r) de la division de N par 2.
        q, r = divmod(N, 2)
        if r == 0:
            # Si N est exactement divisible par 2, on réduit N à q via f(q), puis on paie le prix A pour la division.
            ret = min(ret, f(q) + A)
        else:
            # Si N n'est pas divisible par 2, on considère deux options :
            # (1) On décrémente N de 1 (coût D), puis on divise (q = (N-1)//2), paie coût A.
            # (2) On incrémente N de 1 (coût D), puis on divise (q = (N+1)//2), paie coût A.
            ret = min(ret, f(q) + A + D, f(q+1) + A + D)

        #=== ESSAI AVEC LA DIVISION PAR 3 ===#
        # Même logique : q = N // 3, r = N % 3
        q, r = divmod(N, 3)
        if r == 0:
            # Si divisible exactement, on paie seulement le coût de la division.
            ret = min(ret, f(q) + B)
        elif r == 1:
            # Décrémentation (-1) avant de diviser, puis paie coût additionnel D.
            ret = min(ret, f(q) + B + D)
        else:
            # r == 2 : On peut soit ajouter 1 pour rendre N divisible (N+1), soit rien, ici on force l'option incrément.
            # On paie coût D pour +1, puis fait la division.
            ret = min(ret, f(q+1) + B + D)

        #=== ESSAI AVEC LA DIVISION PAR 5 ===#
        # Même procédure pour la division par 5.
        q, r = divmod(N, 5)
        if r == 0:
            # Division directe par 5.
            ret = min(ret, f(q) + C)
        elif r == 1:
            # Décrémentation de 1 avant division.
            ret = min(ret, f(q) + C + D)
        elif r == 2:
            # Décrémentation de 2 avant division (chaque décrément coûte D).
            ret = min(ret, f(q) + C + D + D)
        elif r == 3:
            # Incrémentation de 2 avant la division.
            ret = min(ret, f(q+1) + C + D + D)
        else:
            # r == 4 : Incrémentation de 1 avant division.
            ret = min(ret, f(q+1) + C + D)
        # Après avoir testé toutes les façons d'arriver à N=0 de manière plus efficace que la simple décrémentation,
        # on retourne la meilleure solution trouvée pour ce N.
        return ret
    # Lancement du calcul pour le N donné.
    return f(N)

# Lecture du nombre de cas de test T.
T = int(input())

# Boucle sur chaque cas de test à traiter.
for _ in range(T):
    # Lecture d'une ligne, découpage en 5 entiers correspondant à n, a, b, c, d.
    n, a, b, c, d = map(int, input().split())
    # Appel de la fonction solve pour chaque jeu de paramètres, affichage du résultat.
    print(solve(n, a, b, c, d))