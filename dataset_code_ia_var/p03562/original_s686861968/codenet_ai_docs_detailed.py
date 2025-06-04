import sys
from functools import reduce

# Redéfinition des fonctions d'entrée pour lire en binaire depuis l'entrée standard
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

MOD = 998244353  # Modulo utilisé pour la réponse finale

def gcd(a, b):
    """
    Calcule le PGCD (polynôme GCD sur F_2) de deux nombres entiers interprétés comme des polynômes binaires.

    Args:
        a (int): Un polynôme binaire sous forme d'entier.
        b (int): Un polynôme binaire sous forme d'entier.

    Returns:
        int: Le PGCD des deux polynômes binaires sous forme d'entier.
    """
    # S'assurer que a >= b au début de l'algorithme
    if a < b:
        a, b = b, a
    # Algorithme du PGCD bitwise adapté pour les polynômes sur F_2
    while b:
        LA = a.bit_length()
        LB = b.bit_length()
        # XOR shift : simule la division sur F_2
        a ^= b << (LA - LB)
        # Maintenir l'invariant a >= b
        if a < b:
            a, b = b, a
    return a

# Lecture et traitement de l'entrée
# Première ligne : récupère la valeur X (borne supérieure), convertie depuis une chaîne binaire.
X = int(readline().split()[1], 2)

# Lecture de toutes les autres lignes : chaque ligne représente un polynôme sous forme binaire
A = [int(x, 2) for x in readlines()]

# Calcul du PGCD de tous les polynômes de A avec la fonction gcd définie ci-dessus
g = reduce(gcd, A)

# Étape suivante : compter le nombre de multiples de g qui ne dépassent pas X
# On raisonne en fixant les chiffres de poids fort et en se servant des propriétés
# des polynômes binaires pour construire toutes les solutions valides.

# Nombre de bits (longueur) de X et de g
LX = X.bit_length()
Lg = g.bit_length()

# Base du calcul : combien de multiples entiers de g rentrent dans X, en comparant les bits de poids fort
answer = X >> (Lg - 1)

# Calcul pour vérifier si le multiple courant est <= X lorsque les chiffres de poids fort coïncident avec X
prod = 0
x = X
Lx = LX

# Utilise le même algorithme que le PGCD pour réduire x modulo g tout en retenant le multiple partiel construit
while Lx >= Lg:
    # Ajouter le terme correspondant au multiple actuel (g << (Lx - Lg)) au produit en construction via XOR
    prod ^= g << (Lx - Lg)
    # Réduire x modulo ce terme
    x ^= g << (Lx - Lg)
    # On travaille sur la partie restante
    Lx = x.bit_length()

# Si le multiple construit (prod) ne dépasse pas X, il s'agit d'une solution valide supplémentaire
if prod <= X:
    answer += 1

# Prendre la réponse modulo MOD pour respecter la contrainte de l'énoncé
answer %= MOD

# Affichage du résultat final
print(answer)