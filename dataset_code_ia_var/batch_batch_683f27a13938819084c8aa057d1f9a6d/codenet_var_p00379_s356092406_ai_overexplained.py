# Définition d'une fonction nommée 'val' qui prend un paramètre 'x'
def val(x):
    # Création d'une variable locale nommée 'sum' pour garder la somme des chiffres de x, initialisée à 0
    sum = 0
    # Boucle while : continue tant que la valeur de 'x' est strictement supérieure à 0
    while x > 0:
        # Ajoute à 'sum' le dernier chiffre à droite de 'x' (obtenu via 'x % 10')
        sum += x % 10
        # Modifie la valeur de 'x' en supprimant son dernier chiffre (division entière par 10)
        x //= 10
    # Retourne la somme calculée des chiffres de 'x'
    return sum

# Lit une ligne depuis l'entrée standard, la sépare en sous-chaînes sur chaque espace,
# convertit chaque sous-chaîne en entier puis les assigne aux variables 'a', 'n' et 'm'
a, n, m = map(int, input().split())

# Crée une variable 'cnt' pour compter combien de fois une condition est remplie, initialisée à 0
cnt = 0

# Boucle 'for' pour faire varier 'y' de 1 jusqu'à 72 inclus (la fonction range s'arrête avant la valeur supérieure)
for y in range(1, 73):
    # À chaque itération de 'y', initialiser une variable 'x' avec la valeur 1, pour débuter une multiplication
    x = 1
    # Boucle imbriquée 'for' pour faire varier 't' de 1 à 'n' inclus (c'est-à-dire effectuer n multiplications)
    for t in range(1, n + 1):
        # À chaque tour, multiplier l'actuel 'x' par la valeur '(y + a)'
        x *= (y + a)
    # Maintenant, 'x' est égal à (y + a) élevé à la puissance n
    # Vérifie si deux conditions sont remplies en même temps :
    # 1. 'x' est inférieur ou égal à 'm'
    # 2. la somme des chiffres de 'x' (obtenue avec val(x)) est exactement égale à 'y'
    if x <= m and val(x) == y:
        # Si les deux conditions sont vérifiées, incrémente le compteur 'cnt' de 1
        cnt += 1

# Affiche la valeur finale du compteur 'cnt', soit le nombre total de 'y' satisfaisant les deux conditions précédentes
print(cnt)