import sys  # Le module sys permet d’accéder à certaines fonctions système et manipuler des paramètres relatifs à l’interpréteur Python
sys.setrecursionlimit(10**6)  # On augmente la limite de récursion permise de Python à 1 000 000 (par défaut, elle est bien plus basse)
# Cela est utile si vous travaillez avec des fonctions récursives profondes, comme pour certaines algorithmes sur les arbres

input = sys.stdin.readline  # On redéfinit la fonction input pour lire plus vite les entrées standard, utile si beaucoup d’entrées à traiter

# On importe diverses fonctions mathématiques depuis le module math
from math import floor, sqrt, factorial, hypot, log  # floor: partie entière, sqrt: racine carrée, factorial: factorielle, hypot: hypoténuse, log: logarithme népérien

# On importe plusieurs fonctions utiles pour gérer des files de priorité (heapq)
from heapq import heappop, heappush, heappushpop  # heappop: retire le plus petit, heappush: ajoute un élément, heappushpop: ajoute puis retire le petit

# On importe des structures de données spéciales pour compter/ordonner/gérer des collections d’objets
from collections import Counter, defaultdict, deque  # Counter: compteur d’occurrence, defaultdict: dictionnaire avec valeur par défaut, deque: liste double terminaison rapide

# On importe plusieurs générateurs combinatoires et outils d’itération
from itertools import accumulate, permutations, combinations, product, combinations_with_replacement
# accumulate: accumulation partielle, permutations: toutes les permutations, combinations: toutes les combinaisons sans remise, product: produit cartésien, combinations_with_replacement: combinaisons avec remise

# On importe deux fonctions du module bisect pour faire de la recherche dichotomique/insertion en listes triées
from bisect import bisect_left, bisect_right  # bisect_left: index insertion à gauche, bisect_right: index insertion à droite

# On importe deepcopy pour faire des copies profondes d’objets complexes (sinon une copie est juste une référence)
from copy import deepcopy

# On importe la fonction gcd (plus grand commun diviseur) du module fractions
from fractions import gcd  # gcd: greatest common divisor (NB: dans Python 3.5+, il vaut mieux utiliser math.gcd)

# On importe randint pour tirer au hasard un entier dans un intervalle fermé
from random import randint

# On définit une fonction utilitaire 'ceil' pour le calcul du plafond d'une division entière
def ceil(a, b):
    # Cette fonction retourne l’entier supérieur du résultat de la division de a par b
    # Cela correspond à math.ceil(a/b) mais fonctionne pour des entiers sans utiliser la division flottante
    # Exemple: ceil(5, 2) -> 3
    return (a + b - 1) // b

# On définit la constante "inf" pour représenter l’infini (float positif infini en Python)
inf = float('inf')

# On définit la constante "mod" pour les calculs modulo (souvent utilisé en programmation compétitive)
mod = 10**9 + 7  # Modulo fréquemment utilisé pour éviter les débordements d'entier

# On définit une fonction d'affichage personnalisée pprint qui affiche chaque élément de la séquence, ligne par ligne
def pprint(*A):
    # Pour chaque paramètre a dans A (A peut contenir plusieurs listes/tableaux à afficher)
    for a in A:
        # On affiche chaque élément de la liste a sur une nouvelle ligne
        print(*a, sep='\n')

# Fonction pour transformer une chaîne en int puis soustraire 1 (décalage d’index, utile pour passer d’index 1-based à 0-based)
def INT_(n):
    # Convertit n en entier puis enlève 1, utile pour gérer des indexages sur 0
    return int(n) - 1

# Fonction pour lire plusieurs entiers sur une ligne, séparés par des espaces
def MI():
    # map applique int à chaque entrée de input().split(), retournant un itérable d’entiers
    return map(int, input().split())

# Fonction pour lire plusieurs flottants sur une ligne, séparés par des espaces
def MF():
    return map(float, input().split())

# Fonction pour lire plusieurs entiers, mais chaque entier est décrémenté de 1 (décalage d’index)
def MI_():
    return map(INT_, input().split())

# Fonction pour lire une ligne composée de plusieurs entiers et retourner une liste
def LI():
    # Convertit l’itérable de MI() en liste d’entiers
    return list(MI())

# Fonction pour lire une ligne composée de plusieurs entiers, chacun décrémenté de 1 (index 0-based), retourne une liste
def LI_():
    return [int(x) - 1 for x in input().split()]

# Fonction pour lire une ligne avec plusieurs flottants et retourner une liste
def LF():
    return list(MF())

# Fonction pour lire n entiers, chaque entier est entré sur une ligne séparée ; retourne une liste d’entiers
def LIN(n: int):
    return [I() for _ in range(n)]  # I() lit et convertit chaque ligne en int (voir plus bas)

# Fonction pour lire n lignes, où chaque ligne contient plusieurs entiers ; retourne une liste de listes d’entiers
def LLIN(n: int):
    return [LI() for _ in range(n)]

# Fonction pour lire n lignes, chaque ligne ayant plusieurs entiers, chacun décrémenté de 1 (index 0-based)
def LLIN_(n: int):
    return [LI_() for _ in range(n)]

# Fonction pour lire une séquence de lignes, chaque ligne étant une liste d’entiers (chaque ligne est splittée selon les espaces)
def LLI():
    return [list(map(int, l.split())) for l in input()]  # Attention: Itère sur input(), c'est une chaîne avec des lignes!

# Fonction pour lire un entier à partir de l’entrée standard
def I():
    return int(input())

# Fonction pour lire un nombre flottant à partir de l’entrée standard
def F():
    return float(input())

# Fonction pour lire une chaîne à partir de l’entrée, en supprimant les retours à la ligne
def ST():
    # On utilise la méthode replace pour enlever les retours chariot "\n"
    return input().replace('\n', '')

# Fonction principale de ce script Python
def main():
    # On lit la chaîne de caractères d’entrée S, sans saut de ligne de fin
    S = ST()

    # ----- DOCUMENTATION / EXPLICATION -----
    # Le commentaire ci-dessous explique la logique du problème traité par ce main()
    """
        ababababa
        bababba
        のどちらかで終わる
        両端が同じなら上
        そうでないなら下のようになる
        
        つまり両端が同じなら奇数長になり
        そうでないなら偶数長になる

        Traduction du japonais :
        - La chaîne se termine forcément par l’un des deux motifs (ababababa ou bababba)
        - Si les deux extrémités (premier caractère et dernier caractère) sont identiques, le motif est comme le premier
        - Sinon, comme le deuxième
        - Donc : si les deux extrémités sont identiques, la longueur est impaire ; sinon, elle est paire
    """

    # ------ LOGIQUE DE DÉCISION ------
    # len(S) & 1 vérifie si la longueur de S est impaire (==1) ou paire (==0)
    # S[0] == S[-1] vérifie si le premier caractère de S est égal au dernier
    # En faisant (len(S) & 1) == (S[0]==S[-1]), on retourne True si les deux sont de même parité (soit les deux sont True, soit les deux sont False)
    # Si c'est le cas, afficher "Second". Sinon "First"
    if (len(S) & 1) == (S[0] == S[-1]):
        # Affiche "Second" si les conditions sont remplies (voir ci-dessus pour logique)
        print("Second")
    else:
        # Sinon, affiche "First"
        print("First")

# Point d’entrée principal du script, ne s’exécute que si le fichier est appelé directement (et non importé comme module)
if __name__ == '__main__':
    main()  # On appelle la fonction principale pour exécuter le script