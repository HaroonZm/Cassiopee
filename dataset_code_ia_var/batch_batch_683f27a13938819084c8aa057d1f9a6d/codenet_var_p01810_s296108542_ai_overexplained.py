#!/usr/bin/env python3

# Demande à l'utilisateur d'entrer deux entiers sur la même ligne, séparés par un espace (ex : "5 3").
# La fonction input() lit cette ligne sous forme de chaîne de caractères.
# La méthode split() sépare cette chaîne en une liste de deux petites chaînes selon l'espace.
# La fonction map(int, ...) convertit chaque sous-chaîne en un entier (int).
# Enfin, l'affectation n, k = ... place les deux entiers respectivement dans les variables n et k.
n, k = map(int, input().split())

# On initialise la variable entière a à 0.
# Cette variable servira pour le calcul dans la boucle suivante.
a = 0

# On utilise une boucle for pour répéter un bloc d'instructions plusieurs fois.
# La fonction range(n-1) va générer une séquence de nombres entiers allant de 0 jusqu'à n-2 inclus.
# Donc, la boucle va s'exécuter exactement (n-1) fois.
for i in range(n-1):
    # La variable a subit une mise à jour lors de chaque itération de la boucle.
    # On commence par multiplier a par k.
    # Puis on divise le résultat par (k - 1) en utilisant // pour effectuer une division entière,
    # c'est-à-dire que le résultat sera un entier (la partie entière du quotient, aucun arrondi flottant).
    # Ensuite, on ajoute 1 au résultat obtenu.
    # Enfin, cette toute nouvelle valeur est assignée à a, ré-écrasant la valeur précédente.
    a = a * k // (k - 1) + 1

# Après la fin de la boucle, on utilise la fonction print() pour afficher la valeur finale de a à l'écran.
print(a)