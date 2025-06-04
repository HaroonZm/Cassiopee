# Importation des modules et fonctions nécessaires pour ce script
from itertools import product, accumulate  # Importation de fonctions pour les produits cartésiens et les sommes cumulées
from math import gcd  # Importation de la fonction gcd pour calculer le plus grand commun diviseur, bien que non utilisée ici
from bisect import bisect  # Importation de la fonction bisect pour faire des recherches de position dans des listes triées
import sys  # Importation du module système pour gérer l'entrée et la sortie standard
from sys import setrecursionlimit  # Importation spécifique de la fonction pour changer la limite de récursion

# Changement de la limite de récursion maximale autorisée afin d'éviter des erreurs de récursion profonde ;
# ici on fixe la limite à 10**9, ce qui est une valeur très élevée.
setrecursionlimit(10**9)

# Redéfinition de la fonction d'entrée pour gagner en rapidité :
# sys.stdin.readline permet de lire une ligne depuis l'entrée standard plus rapidement que input()
input = sys.stdin.readline

# Définition d'une fonction utilitaire prenant une ligne d'entrée, la découpant selon les espaces, 
# transformant chaque morceau en entier, et renvoyant le tout sous forme de liste d'entiers.
def inpl():
    return list(map(int, input().split()))

# Définition d'une fonction permettant de générer la liste de tous les nombres premiers jusqu'à N inclus.
def primes(N):
    # Création d'une "sieve" (tableau de booléens codés sur des entiers) pour marquer primalité
    sieve = [1] * (N + 1)  # Tous les nombres sont initialement considérés premiers (True), sauf 0 et 1
    sieve[:2] = [0, 0]     # 0 et 1 ne sont pas des nombres premiers
    P = []                 # Liste vide pour stocker les nombres premiers
    # Boucle pour parcourir tous les nombres de 2 à N inclus
    for i in range(2, N + 1):
        if sieve[i]:        # Si le nombre i est encore marqué comme premier
            P.append(i)     # Ajouter ce nombre à la liste des nombres premiers
            # Marquer tous les multiples de i (commençant à 2*i) comme non-premiers
            for j in range(2 * i, N + 1, i):
                sieve[j] = 0
    # Retourner la liste complète des nombres premiers trouvés jusqu'à N
    return P

# Création d'un tableau C de taille 100001 (indices de 0 à 100000), rempli initialement de 1.
# Ce tableau va servir à marquer certains entiers comme étant valides ou non selon différents critères.
C = [1] * (10**5 + 1)
# On place à 0 les indices 0 et 1 car ils ne sont pas considérés par la suite.
C[0] = 0
C[1] = 0

# Génération de la liste des nombres premiers jusqu'à 10^5 inclus, à l'aide de la fonction 'primes' définie plus haut.
P = primes(10**5)

# Boucle pour marquer tous les indices correspondant à un nombre premier comme non valides
# On place 0 à la position de chaque nombre premier dans le tableau C
for p in P:
    C[p] = 0

# Deuxième boucle pour marquer comme non valides tous les cubes parfaits de nombres premiers,
# à condition que leur cube ne dépasse pas 100000.
for p in P:
    if p**3 > 100000:  # On s'arrête si le cube du nombre premier dépasse la borne supérieure de C
        break
    C[p**3] = 0        # Marquer la case correspondante à ce cube comme non valide

# Boucle double pour marquer comme non valides tous les produits "premier * premier",
# avec la règle que p_i <= p_j et que le produit n'excède pas la borne maximale.
for i in range(len(P)):  # Pour chaque nombre premier d'indice i
    # La fonction bisect(P, 10**5 // P[i]) retourne l'index jusqu'où P[j] * P[i] <= 10^5
    for j in range(i, bisect(P, 10**5 // P[i])):
        # Produit de deux nombres premiers, ne dépassant pas 10^5,
        # On marque cette case comme non valide
        C[P[i] * P[j]] = 0

# Construction de la somme cumulée de C : S[k] == somme de C[0] à C[k]
# La fonction accumulate renvoie un itérable : on le convertit en liste.
S = list(accumulate(C))

# Pour chaque requête de l'utilisateur (première entrée = nombre de requêtes)
for _ in range(int(input())):
    # Lecture d'une valeur, la convertit en entier et affiche la valeur de la somme cumulée correspondante S[n]
    print(S[int(input())])