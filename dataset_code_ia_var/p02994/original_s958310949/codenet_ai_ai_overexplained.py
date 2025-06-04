# Importation du module 'sys' pour accéder à stdin, qui permet de lire les entrées standards.
from sys import stdin
# Importation de la fonction deepcopy depuis le module copy, pour effectuer des copies profondes d'objets (non utilisé ici, mais présent dans le code original).
from copy import deepcopy
# Importation de la fonction reduce depuis functools, utilisée pour appliquer une fonction de façon cumulative (non utilisé ici, mais présent dans le code original).
from functools import reduce
# Importation de la fonction gcd du module fractions, pour calculer le plus grand commun diviseur (obsolète à partir de Python 3.5, préférer math.gcd ; pas utilisé ici).
from fractions import gcd
# Importation du module math, qui fournit des fonctions mathématiques de base (non utilisé ici).
import math
# Importation du module itertools, qui propose des fonctions pour la manipulation d’itérateurs (non utilisé directement ici).
import itertools
# Importation de la classe Counter pour le comptage rapide d’éléments (non utilisée ici).
from collections import Counter
# Importation de la fonction chain depuis itertools, utile pour aplatir des listes imbriquées (non utilisé ici).
from itertools import chain
# Importation de heappush et heappop depuis heapq, pour manipuler des files de priorité (non utilisés ici).
from heapq import heappush, heappop

"""
Ce bloc de texte multi-lignes contient des exemples de diverses opérations d'entrée fréquemment utilisées dans les concours de programmation, telles que :
- lecture d'un entier ;
- lecture de deux entiers sur une seule ligne ;
- lecture d'une liste d'entiers d'une entrée unique ;
- lecture d'une liste d'entiers à partir de plusieurs entrées ;
- lecture d'une liste bi-dimensionnelle.
Il n’est pas exécuté : il sert d’aide-mémoire/commentaire.
"""

# Lecture des deux entiers N et L depuis l'entrée standard (souvent la première ligne), séparés par un espace.
N, L = map(int, input().split())

# Calcul de la somme totale de la suite d'entiers allant de L à L+N-1, 
# c'est-à-dire N entiers consécutifs commençant à L.
# Afin d'alléger le calcul, la formule suivante est utilisée :
# Somme = N * (premier élément + dernier élément) // 2
# premier élément = L
# dernier élément = L + N - 1
# donc Somme = N * (L + (L + N - 1)) // 2 = N * (2L + N - 1) // 2
Sum = N * (N + 2 * L - 1) // 2

# On va chercher à supprimer du total l'élément dont la valeur absolue est minimale (le plus petit en valeur absolue).
# Cela correspond à la consigne typique de certains problèmes de programmation, où on doit retirer, par exemple, le "fruit" au goût le plus neutre.

# Si L > 0, alors tous les éléments sont strictement positifs (par exemple : [L, L+1, ..., L+N-1]).
if L > 0:
    # Dans ce cas, le nombre le plus proche de 0 est L (le plus petit de la suite).
    # Donc on soustrait L à la somme totale.
    ans = Sum - L
# Sinon, si L+N-1 < 0 (c’est-à-dire, le dernier élément est encore négatif), alors tous les nombres sont strictement négatifs.
elif L + N - 1 < 0:
    # Ici, l'élément le plus proche de zéro est le dernier élément de la suite, soit L+N-1 (le moins négatif).
    # On retire cet élément de la somme totale.
    ans = Sum - (L + N - 1)
else:
    # Dans tous les autres cas, la suite d'entiers contient 0, ou des entiers positifs et négatifs de part et d'autre de 0.
    # Dans ce cas, celui dont la valeur absolue est minimale est 0 lui-même, donc on retire 0, ce qui est inutile.
    ans = Sum

# Affichage du résultat calculé. Cette commande print affiche le nombre 'ans' à la sortie standard.
print(ans)