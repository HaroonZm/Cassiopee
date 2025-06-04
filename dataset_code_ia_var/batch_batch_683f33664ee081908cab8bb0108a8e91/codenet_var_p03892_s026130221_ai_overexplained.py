# Définition d'une fonction nommée 'gcd' qui calcule le plus grand commun diviseur (PGCD) de deux nombres entiers 'a' et 'b'
def gcd(a, b):
    # Vérification si la variable 'b' est égale à 0 (cela permet de savoir si la division euclidienne est terminée)
    if b == 0:
        # Si 'b' est égal à 0, alors 'a' est le PGCD (cas de base de la récursion)
        return a
    # Appel récursif à la fonction 'gcd' en inversant les rôles : 'b' devient le premier argument, et 'a % b' (le reste de la division de 'a' par 'b') devient le second argument
    return gcd(b, a % b)

# Récupération de quatre valeurs entières à partir de la saisie de l'utilisateur
# L'utilisateur doit entrer quatre nombres entiers séparés par des espaces
# La fonction input() lit la ligne en entrée (sous forme de chaîne de caractères)
# La méthode split() divise cette chaîne en une liste de sous-chaînes pour chaque espace
# La fonction map() applique la conversion en entier (int) à chaque sous-chaîne
# L'opérateur d'affectation simultanée décompose les quatre valeurs dans les variables 'a', 'b', 'c', 'd'
a, b, c, d = map(int, input().split())

# Calcul de la différence absolue entre 'c' et 'a'
# 'abs()' renvoie toujours un résultat positif, ce qui garantit des calculs corrects même si 'c' < 'a'
c = abs(c - a)

# Calcul de la différence absolue entre 'd' et 'b', même principe que pour 'c'
d = abs(d - b)

# On détermine le plus grand des deux nombres 'c' et 'd' avec 'max(c, d)'
# On détermine le plus petit avec 'min(c, d)'
# On calcule le PGCD des deux valeurs précédentes à l'aide de la fonction 'gcd'
g = gcd(max(c, d), min(c, d))

# On divise 'c' par 'g' pour obtenir combien de fois le PGCD s'insère dans 'c'
# Le résultat est converti explicitement en entier avec int() pour gérer d'éventuelles divisions flottantes (même si 'c' et 'g' sont normalement entiers)
j = int(c / g)

# Même division mais avec 'd', on veut le nombre de fois que 'g' s'insère dans 'd'
k = int(d / g)

# Calculé selon la formule (j + k - 1) * g
# Cela donne le résultat final qui dépend du PGCD et des divisions précédentes
# On affiche ce résultat à l'aide de print()
print((j + k - 1) * g)