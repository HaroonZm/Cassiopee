# Demander à l'utilisateur d'entrer un nombre entier et stocker la valeur dans la variable N
# La fonction input() affiche une invite à l'utilisateur pour qu'il saisisse une valeur au clavier
# int() convertit la chaîne de caractères saisie en un nombre entier
N = int(input())

# Pareil que précédemment, demander à l'utilisateur de saisir la valeur pour la variable K et la convertir en entier
K = int(input())

# Demander à l'utilisateur la valeur pour la variable X, en la convertissant elle aussi en entier
X = int(input())

# Enfin, demander la valeur pour la variable Y et la convertir en entier
Y = int(input())

# Vérifier si la valeur de N est strictement supérieure à la valeur de K
if N > K:
    # Si la condition est vraie, alors:
    # Multiplier la valeur de X par la valeur de K, et stocker le résultat dans la variable x
    x = X * K  # x contient le coût pour les K premiers éléments à un tarif X

    # Calculer la différence entre N et K pour trouver combien il y a d'éléments supplémentaires après les K premiers
    # Multiplier cette différence par Y afin de connaître le coût de ces éléments restants à un tarif Y
    y = (N - K) * Y  # y contient le coût pour les éléments restants à un tarif Y

    # Additionner les coûts x et y pour obtenir le coût total puis l'afficher avec print()
    print(x + y)
else:
    # Si la condition N > K n'est pas satisfaite (donc N <= K):
    # Multiplier N par X pour obtenir le coût total, puisque le tarif X s'applique à tous les N éléments
    print(N * X)  # Afficher le résultat

# Fin du programme. Toutes les instructions ci-dessus s'exécutent dans l'ordre où elles apparaissent.