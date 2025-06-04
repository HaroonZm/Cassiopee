# Demande à l'utilisateur de saisir des valeurs, les sépare par des espaces, les convertit en entiers, puis les affecte aux variables a, b, et c
a, b, c = map(int, input().split())  # 'input()' lit toute la ligne comme une chaîne, 'split()' la divise en morceaux, 'map(int, ...)' transforme chaque morceau en entier

# Initialisation d'un compteur à zéro. Cette variable servira à compter combien de fois une certaine condition sera vérifiée dans la boucle suivante
count = 0

# Utilisation d'une boucle 'for' pour itérer sur une séquence de nombres entiers commençant à 'a' et finissant à 'b' inclus (car 'range' s'arrête avant le second argument, donc on écrit 'b+1')
# 'i' prendra successivement toutes les valeurs de 'a' à 'b' inclusivement
for i in range(a, b + 1):
    # Vérification si 'c' est exactement divisible par 'i'.
    # L'opérateur modulo '%' retourne le reste de la division de 'c' par 'i'.
    # Si ce reste est égal à zéro, cela signifie que 'c' est divisible par 'i' sans reste.
    if c % i == 0:
        # Si la condition au-dessus est vraie, on incrémente la variable 'count' de 1.
        # C'est-à-dire qu'on augmente 'count' de 1 chaque fois que 'c' est divisible par 'i'
        count += 1

# Affichage de la variable 'count', qui contient le nombre total d'entiers 'i' pour lesquels 'c' est divisible sans reste dans l'intervalle demandé.
print(count)