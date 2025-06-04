# Demande à l'utilisateur de saisir trois entiers séparés par des espaces
# Ces entiers seront lus d'un coup sous forme de chaîne de caractères puis convertis en entiers
# 'n' représente le nombre total d'itérations ou le nombre d'éléments à traiter
# 'h' et 'w' sont deux valeurs qui serviront de seuil pour la comparaison
n, h, w = map(int, input().split())

# Initialise la variable 'ans' à 0. Cette variable va servir à compter combien de fois une certaine condition est réalisée.
ans = 0

# Initialise la variable 'chk' à 0. Dans ce code, cette variable n'est pas utilisée ensuite mais elle était probablement prévue pour autre chose.
chk = 0

# Démarre une boucle qui va s'exécuter 'n' fois. 'range(n)' produit une séquence de nombres de 0 à n-1.
for i in range(n):
    # Pour chaque itération, on demande à l'utilisateur de saisir deux entiers séparés par des espaces
    # Ces deux entiers sont attribués respectivement aux variables 'y' et 'x'
    y, x = map(int, input().split())
    
    # On vérifie si 'y' est supérieur ou égal à 'h' ET si 'x' est supérieur ou égal à 'w'
    # Cela revient à vérifier si les dimensions (y, x) satisfont le seuil minimum fixé par (h, w)
    if h <= y and w <= x:
        # Si la condition ci-dessus est remplie, on incrémente la variable 'ans' de 1
        # Cela signifie qu'on a trouvé un élément qui répond au critère défini
        ans += 1

# Affiche la valeur finale de 'ans', c'est-à-dire le nombre total de fois où la condition a été remplie
print(ans)