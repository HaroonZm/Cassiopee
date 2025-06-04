# Début de la définition de la fonction gcd (Greatest Common Divisor) qui calcule le Plus Grand Commun Diviseur de deux entiers x et y
def gcd(x, y):
    # Si x est strictement inférieur à y, alors nous permutons les valeurs de x et de y.
    # Cela permet de s'assurer que x >= y pour simplifier les calculs suivants.
    if x < y:
        x, y = y, x  # Échange les valeurs de x et y.

    # On vérifie ensuite si le reste de la division de x par y est égal à zéro (c'est-à-dire si y divise x).
    if x % y == 0:
        # Si le reste est zéro alors y est le pgcd des deux nombres car il divise parfaitement x.
        return y  # Retourne y comme résultat de la fonction.
    else:
        # Sinon (le reste n'est pas zéro), nous appelons récursivement la fonction gcd.
        # On applique l'algorithme d'Euclide : on cherche le pgcd de y et le reste de x divisé par y.
        return gcd(y, x % y)  # Appel récursif avec de nouveaux paramètres.

# Lecture d'un entier depuis l'entrée standard (l'utilisateur doit entrer la valeur puis appuyer sur Entrée).
n = int(input())  # Convertit la chaîne lue en entier, qui sera le nombre d'éléments du tableau.

# Lecture d'une ligne de nombres entiers séparés par des espaces, puis conversion en liste d'entiers.
# 'input()' lit une ligne de texte (par exemple : "2 3 4"), 'split()' décompose cette chaîne en une liste de chaînes ['2', '3', '4']
# 'map(int, ...)' convertit chaque élément en entier, et 'list(...)' construit une liste à partir du résultat.
A = list(map(int, input().split()))

# On souhaite calculer le Plus Petit Multiple Commun (PPCM) de tous les nombres de la liste A.
# Pour cela, on utilise progressivement la formule : PPCM(a, b) = (a * b) / pgcd(a, b)

# Initialise la variable l avec le premier élément du tableau A.
l = A[0]

# Utilisation d'une boucle for pour parcourir les éléments restants de la liste A.
# Commence à l'indice 1 (c'est-à-dire le deuxième élément), jusqu'à n-1 (car l'indice commence à 0).
for i in range(1, n):
    # À chaque itération, on met à jour l avec le PPCM de l'actuel l et le prochain élément du tableau A.
    # La multiplication 'l * A[i]' calcule le produit des deux nombres.
    # 'gcd(l, A[i])' calcule leur pgcd.
    # Le PPCM est donc ce produit divisé par leur pgcd (on s'assure ainsi que le résultat est le plus petit multiple commun).
    l = l * A[i] / gcd(l, A[i])  # Division flottante.

# Après la boucle, la variable l contient le PPCM de tous les éléments de la liste A.

# Comme l'opération précédente peut donner un nombre flottant (virgule flottante) alors qu'on veut un entier,
# on convertit l en entier avec 'int()' lors de l'affichage final. Cela enlève toute partie décimale.
print(int(l))  # Affiche le PPCM au format entier.