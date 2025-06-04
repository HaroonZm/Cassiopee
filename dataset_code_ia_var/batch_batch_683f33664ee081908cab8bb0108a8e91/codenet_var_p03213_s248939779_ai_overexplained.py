import sys  # Importe le module sys pour gérer l'entrée standard (stdin)
from collections import defaultdict  # Importe defaultdict, une structure de données pratique pour les dictionnaires avec valeurs par défaut

input = sys.stdin.readline  # Redéfinit "input" comme une fonction qui lit une ligne depuis l'entrée standard, utile pour lire efficacement de nombreux inputs
INF = float('inf')  # Définit une valeur représentant l'infini, utile dans de nombreux algorithmes, ici non utilisé
MOD = 10 ** 9 + 7  # Définit une grande constante modulaire courante (utilisée dans de nombreux problèmes, mais ici non utilisée)

def inpl():
    # Fonction utilitaire qui lit une ligne, la divise en morceaux par les espaces,
    # convertit chaque morceau en int, et retourne la liste des entiers
    return list(map(int, input().split()))

# Lit la première ligne d'entrée, qui est censée contenir un entier N
N = int(input())

# Crée un dictionnaire qui compte le nombre d'apparitions de chaque facteur premier
# La clé sera le nombre premier, la valeur le nombre d'apparitions dans la décomposition factorielle des entiers de 1 à N
prime_cnt = defaultdict(int)

# Boucle sur tous les entiers n allant de 1 à N (inclus)
for n in range(N):
    n += 1  # Comme range(N) va de 0 à N-1, on ajoute 1 pour obtenir les entiers de 1 à N
    i = 2  # On commence la décomposition en facteurs premiers avec le plus petit nombre premier, 2
    # Tant que i^2 est inférieur ou égal à n, on vérifie si i est un facteur de n
    while i * i <= n:
        # Si i divise n (n % i == 0)
        if n % i == 0:
            cnt = 0  # Initialise le compteur du nombre de fois que i divise n
            # Divise n par i tant que c'est possible
            while n % i == 0:
                cnt += 1  # Incrémente le compteur pour chaque division par i
                n //= i   # Réduit n en le divisant par i (division entière)
            # Après avoir extrait tous les facteurs i de n, on les ajoute au compteur global prime_cnt
            prime_cnt[i] += cnt
        # Passe au nombre premier suivant
        i += 1

    # Si après le processus il reste un n supérieur à 1, cela signifie qu'il s'agit d'un nombre premier
    if n != 1:
        # On incrémente son compteur d'occurrence dans prime_cnt
        prime_cnt[n] += 1

# Définit une fonction utilitaire num qui compte combien de facteurs premiers (parmi ceux présents dans prime_cnt)
# ont une puissance (nombre de fois qu'ils apparaissent dans toutes les décompositions factorielles de 1 à N)
# au moins égale à n-1 (donc >= n-1)
def num(n):
    cnt = 0  # Initialise le compteur à 0
    # Pour chaque clé (c'est-à-dire chaque nombre premier) dans prime_cnt
    for key in prime_cnt.keys():
        # Si la valeur associée à ce nombre premier est supérieure ou égale à n-1
        if prime_cnt[key] >= n - 1:
            cnt += 1  # On augmente le compteur
    return cnt  # Retourne le nombre de facteurs premiers avec puissance suffisante

# Le commentaire décrit différents moyens d'obtenir un nombre avec exactement 75 diviseurs
# Par exemple, 3*5*5, 3*25, 5*15, 75, etc.
# Ceci correspond au nombre de combinaisons possibles de facteurs premiers répondant à ces critères

# Calcule le résultat en suivant la manière standard de trouver combien de nombres dans
# la factorisation de N! (factorielle de N) ont au moins 75 diviseurs.
# Pour cela, on utilise la formule de la fonction du nombre de diviseurs à partir de la décomposition en facteurs premiers :
# - Si l'écriture de N! est p1^a1 * p2^a2 * ... * pk^ak,
#   alors le nombre total de diviseurs est (a1+1)*(a2+1)*...*(ak+1).
#
# Ici, on cherche combien de nombres dans N! admettent précisément des combinaisons
# de facteurs premiers dont les multiplicités permettent d'obtenir au moins 75 diviseurs (selon les patterns mentionnés).
# C'est pourquoi plusieurs termess apparaissent pour différentes répartitions de facteurs ("num(75)", "num(15)*...").

# On affiche le nombre total de manières possibles et valides
print(
    num(75)  # Correspond au cas où un seul facteur premier apparaît au moins 74 fois (et donc donne 75 diviseurs)
    + num(15) * (num(5) - 1)  # Correspond au cas (15,5): un facteur apxi>=14, un autre >=4, ils doivent être distincts
    + num(25) * (num(3) - 1)  # Correspond au cas (25,3): un facteur >=24, un autre >=2, distinct aussi
    + num(5) * (num(5) - 1) * (num(3) - 2) // 2  # Cas (5,5,3): deux facteurs >=4 et un >=2, tous distincts, //2 pour éviter comptage double
)