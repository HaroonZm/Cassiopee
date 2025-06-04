import sys  # Importe le module sys pour accéder à stdin et readline (lecture rapide des entrées standard)
from collections import deque  # Importe deque permettant de créer des files efficaces (non utilisé ici mais importé)
from heapq import heapify, heappop, heappush  # Fonctions pour manipuler des files de priorité (non utilisées mais importées)
from itertools import combinations, permutations  # Fonctions pour générer combinaisons et permutations (non utilisées)
from bisect import bisect, bisect_left  # Fonctions de recherche dichotomique (non utilisées)

# Définition d'une fonction pour calculer le plus grand commun diviseur (gcd = greatest common divisor)
def gcd(a, b):
    # Prend deux nombres 'a' et 'b' et va placer le plus grand dans a et le plus petit dans b
    a, b = max(a, b), min(a, b)
    # Multiplie a et b, valeur non utilisée dans le calcul ici (var 'c' redondante)
    c = a * b  
    # Boucle tant que le reste de la division de a par b n'est pas nul (méthode d'Euclide)
    while a % b > 0:
        # Met à jour a avec la valeur de b, met à jour b avec le reste de la division a par b
        a, b = b, a % b
    # Une fois que le reste est nul, b contient le pgcd
    return b

# Définition de la fonction principale appelée solve
def solve():
    # Assigne la fonction sys.stdin.readline à 'input' pour des lectures de lignes plus rapides
    input = sys.stdin.readline
    # Définit une constante 'mod' qui sera utilisée pour les opérations modulo (très utile pour éviter les grands nombres)
    mod = 7 + 10 ** 9  # mod vaut 1000000007, un grand nombre premier courant pour le modulo dans les concours de programmation
    # Lit une ligne de l'entrée standard, la convertit en entier, et l'assigne à N (taille de la liste)
    N = int(input())
    # Lit une autre ligne, la découpe selon les espaces, convertit chaque élément en entier et construit une liste A
    A = [int(a) for a in input().split()]
    # Si N vaut 1 (la liste n'a qu'un seul élément), on affiche simplement 1 (cas particulier)
    if N == 1:
        print(1)
    else:
        # On commence par définir lcm égale au premier élément de la liste A
        lcm = A[0]
        # Parcourt la liste à partir du deuxième élément (indice 1) jusqu'à la fin
        for i in range(1, N):
            # Calcule le pgcd entre lcm courant et A[i] en appelant la fonction gcd
            gcd_a = gcd(lcm, A[i])
            # Met à jour le ppcm (lcm = lowest common multiple) en utilisant la propriété : 
            # ppcm(a, b) = (a * b) // pgcd(a, b)
            lcm = lcm * A[i] // gcd_a
        # Applique le modulo à lcm (pour réduire la taille des nombres)
        lcm %= mod
        # Initialise la variable sumB à 0 (cette variable gardera le total recherché)
        sumB = 0
        # Parcourt avec la fonction enumerate la liste A (récupère à la fois l'indice et la valeur mais l'indice n'est pas utilisé)
        for i, a in enumerate(A):
            # Utilise pow pour calculer l'inverse modulaire de a modulo mod. pow(a, mod-2, mod) n'est valable que si mod est premier.
            # Multiplie lcm par cet inverse, puis l'additionne à sumB
            sumB += lcm * pow(a, mod - 2, mod)
            # Applique le modulo à sumB pour éviter qu'il ne devienne trop grand
            sumB %= mod
        # Après avoir parcouru tous les éléments, affiche la valeur finale de sumB
        print(sumB)
    # Retourne 0 (pas utile ici mais inclus tout de même, bonne pratique dans certaines fonctions principales)
    return 0

# Ceci vérifie si ce fichier est exécuté en tant que script principal
if __name__ == "__main__":
    # Appelle la fonction solve pour exécuter le programme
    solve()