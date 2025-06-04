# Importation du module sys pour manipuler certains aspects du système Python,
# comme la gestion de la sortie et de l'entrée standard, ainsi que le réglage de la limite de récursion
from sys import exit, setrecursionlimit, stderr, stdin

# Importation de la fonction reduce du module functools, qui permet d'appliquer une fonction de façon cumulative à une séquence
from functools import reduce

# Importation de toutes les fonctions et classes du module itertools, utiles pour créer des itérateurs efficaces (non utilisées ici)
from itertools import *

# Importation de defaultdict et Counter depuis le module collections, ces structures sont utiles pour compter ou initialiser des dictionnaires avec des valeurs par défaut
from collections import defaultdict, Counter

# Importation de la fonction bisect du module bisect, permettant de rechercher efficacement des indices pour l'insertion ordonnée dans une liste
from bisect import bisect

# Réimportation du module functools pour s'assurer qu'il est dans l'espace de noms (déjà importé plus haut partiellement)
import functools

# Modification de la limite maximum de récursion pour éviter les erreurs lors des appels récursifs profonds
setrecursionlimit(10**7)

# Redéfinition de la fonction input pour lire une ligne de l'entrée standard et supprimer les espaces en début et fin
def input():
    # Utilise stdin.readline pour lire une ligne brute depuis l'entrée standard
    # Ensuite retire les espaces et le caractère de fin de ligne avec strip()
    return stdin.readline().strip()

# Fonction utilitaire pour lire un entier depuis l'entrée standard
def read():
    # Lit une ligne, la transforme en chaîne de caractères puis la convertit en entier avec int()
    return int(input())

# Fonction utilitaire pour lire une ligne d'entiers séparés par des espaces et la convertir en une liste d'entiers
def reads():
    # input().split() divise la chaîne en éléments individuels, puis map chaque élément en int
    return [int(x) for x in input().split()]

# Définition de la constante MOD (modulo utilisé dans les calculs), typique dans la programmation compétitive pour gérer les grands nombres
MOD = 10**6 + 3

# Initialisation de la liste fact (factorielle), de taille MOD, remplie de 1.
# Cette liste va contenir le pré-calcul de la factorielle de tous les nombres de 0 à MOD-1 modulo MOD.
fact = [1] * MOD

# Boucle pour pré-calculer les valeurs factorielles modulo MOD pour tous les entiers de 1 à MOD-1
for i in range(1, MOD):
    # La factorielle de i est (factorielle de i-1) fois i, le tout en prenant le modulo MOD pour éviter le débordement et respecter les contraintes du problème
    fact[i] = (fact[i-1] * i) % MOD

# Préparation de la liste invfact, de taille MOD, pour stocker les inverses multiplicatifs des factorielles
invfact = [0] * MOD

# Le dernier élément de invfact (l'inverse de fact[MOD-1]) est initialisé avec l'inverse multiplicatif de la dernière factorielle modulo MOD.
# pow(a, b, m) permet de réaliser l'exponentiation rapide a^b mod m.
# Puisque MOD est premier, l'inverse modulo MOD d'un nombre a est pow(a, MOD-2, MOD) selon le petit théorème de Fermat.
invfact[-1] = pow(fact[-1], MOD-2, MOD)

# Calcul des inverses multiplicatifs des factorielles de MOD-2 jusqu'à 0 (remplissage de la table)
for i in range(MOD-2, -1, -1):
    # Invfact[i] = Invfact[i+1] * (i+1) % MOD, ce qui se base sur les propriétés d'inverses modulaires.
    invfact[i] = invfact[i+1] * (i+1) % MOD

# Définition d'une fonction utilitaire pour calculer l'inverse d'un nombre modulo MOD
def inv(n):
    # Utilise pow(n, MOD-2, MOD) pour obtenir l'inverse multiplicatif modulo MOD grâce au petit théorème de Fermat
    return pow(n, MOD-2, MOD)

# Définition de la fonction principale de résolution du problème, qui prend trois paramètres : x, d, n
def solve(x, d, n):
    # Si x vaut 0, le résultat est toujours 0, donc on le retourne immédiatement
    if x == 0:
        return 0
    # Si d vaut 0, on doit simplement renvoyer x à la puissance n modulo MOD,
    # car la suite devient constante (tous les termes sont x)
    if d == 0:
        return pow(x, n, MOD)
    # Calcul de la valeur k, qui est x divisé par d, modulo MOD.
    # L'invocation de inv(d) retourne l'inverse multiplicatif de d modulo MOD,
    # ce qui permet de procéder à la division dans un corps fini.
    k = x * inv(d) % MOD
    # Vérifie s'il serait possible d'accéder à une entrée hors de la gamme de la factorielle pré-calculée
    # Si n + k - 1 >= MOD, retourner 0 car ce cas n'est pas géré (dépassement du tableau factorial)
    if n + k - 1 >= MOD:
        return 0
    # Calcul du résultat à l'aide des valeurs pré-calculées des factorielles et leurs inverses
    # Cette formule peut exprimer le nombre de façons ou résoudre des suites arithmétiques avec combinaison.
    # Multiplication modulaire à chaque étape pour ne jamais dépasser MOD
    result = fact[n + k - 1] * invfact[k-1] % MOD
    result = result * pow(d, n, MOD) % MOD
    return result

# Lecture du nombre de requêtes à effectuer, via la fonction read qui lit un entier depuis l'entrée standard
Q = read()

# Exécution de Q boucles pour traiter chaque requête indépendante
for _ in range(Q):
    # Lecture de trois entiers x, d, n à chaque itération via la fonction reads
    x, d, n = reads()
    # Appel de la fonction solve avec les paramètres lus pour obtenir la réponse
    ans = solve(x, d, n)
    # Affichage du résultat de la requête courante
    print(ans)