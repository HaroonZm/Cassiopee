# Lire l'entrée utilisateur sous forme d'une chaîne de caractères, puis la diviser en une liste de chaînes
# Chaque sous-chaîne est convertie en entier grâce à 'map(int, ...)', puis les trois valeurs sont affectées respectivement à a, b, x
a, b, x = map(int, input().split())

# Comparer la moitié entière de a (division entière par 2) avec la valeur de b
if a // 2 < b:
    # Calculer combien de fois 1000 est contenu en entier dans x. '//' renvoie la partie entière.
    num_a = x // 1000

    # Vérifier si x est exactement un multiple de 1000 (le reste de x / 1000 donne 0)
    if x % 1000 == 0:
        # Si oui, multiplier a par le nombre de lots (num_a) pour avoir le résultat, puis afficher ce résultat
        print(a * num_a)
    # Si x n'est PAS un multiple de 1000, vérifier si a est inférieur à b
    elif a < b:
        # Si a < b, alors on affiche a multiplié par (num_a + 1): on arrondit le nombre de lots de 1000 vers le haut
        print(a * (num_a + 1))
    # Si a n'est pas inférieur à b, vérifier si le reste de x lors de la division par 1000 est strictement supérieur à 500
    elif x % 1000 > 500:
        # Si le reste est supérieur à 500, effectuer le même calcul que précédemment: a multiplié par (num_a + 1)
        print(a * (num_a + 1))
    else:
        # Dans tous les autres cas, multiplier a par num_a et ajouter b au résultat, puis afficher la somme obtenue
        print(a * num_a + b)
# Si la première condition n'est PAS vérifiée (a // 2 >= b), on effectue l'alternative ci-dessous
else:
    # Calculer combien de fois 500 est contenu en entier dans x, stocker le résultat dans num_b
    num_b = x // 500

    # Si x est exactement un multiple de 500 (le reste de la division de x par 500 est zéro)
    if x % 500 == 0:
        # Multiplier b par le nombre de lots de 500 et afficher le résultat
        print(b * num_b)
    else:
        # Sinon, il reste des éléments après le dernier lot de 500, donc on arrondit le nombre de lots de 500 vers le haut
        # Multiplier b par (num_b + 1) et afficher le résultat
        print(b * (num_b + 1))