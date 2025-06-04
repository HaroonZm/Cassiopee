# Lecture d'une ligne entrée utilisateur, découpage par espaces, conversion de chaque élément en int,
# puis attribution à 5 variables distinctes : a, b, c, x, y
a, b, c, x, y = map(int, input().split())

# Détermination de la valeur maximale parmi 'a' et 'b' basée sur la comparaison de 'x' et 'y'
# Si x supérieur ou égal à y, mx prend la valeur de a, sinon de b
mx = a if x >= y else b

# Vérification si deux fois 'c' est inférieur ou égal à la somme de 'a' et 'b'
if c * 2 <= (a + b):
    # Vérification si deux fois 'c' est aussi inférieur ou égal à 'mx'
    if c * 2 <= mx:
        # Calcul du minimum entre 'x' et 'y'
        min_xy = min(x, y)
        # Calcul de la valeur absolue de la différence entre 'x' et 'y'
        diff_abs = abs(x - y)
        # Calcul du nombre total d'opérations (min(x, y) + abs(x - y))
        total_ops = min_xy + diff_abs
        # Calcul du coût total en multipliant le nombre total d'opérations par deux fois c
        cost = total_ops * c * 2
        # Affichage du coût total calculé précédemment
        print(cost)
    else:
        # Calcul du minimum entre 'x' et 'y'
        min_xy = min(x, y)
        # Calcul de la valeur absolue de la différence entre 'x' et 'y'
        diff_abs = abs(x - y)
        # Calcul du coût partiel pour la partie commune à 'x' et 'y'
        part1 = min_xy * c * 2
        # Calcul du coût partiel pour la partie restante (différence entre 'x' et 'y') multipliée par 'mx'
        part2 = diff_abs * mx
        # Calcul du coût total en ajoutant les deux parties
        cost = part1 + part2
        # Affichage du coût total calculé précédemment
        print(cost)
else:
    # Dans le cas où deux fois 'c' est supérieur à la somme de 'a' et 'b', calcul direct du coût
    # Multiplication de 'a' par 'x' et ajout du résultat de 'b' multiplié par 'y'
    total_cost = a * x + b * y
    # Affichage du coût total ainsi calculé
    print(total_cost)