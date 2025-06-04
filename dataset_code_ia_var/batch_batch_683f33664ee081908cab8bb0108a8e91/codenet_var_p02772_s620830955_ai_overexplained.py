# Demande à l'utilisateur de saisir un entier, puis convertit la chaîne de caractères saisie en entier avec la fonction int().
N = int(input())

# Demande à l'utilisateur de saisir plusieurs entiers séparés par des espaces sur une ligne.
# La fonction input() lit la saisie utilisateur sous forme de chaîne de caractères.
# La méthode split() découpe cette chaîne de caractères en une liste de sous-chaînes selon les espaces.
# La fonction map(int, ...) applique la fonction int() à chaque sous-chaîne pour convertir chaque élément en entier.
# Les résultats sont ensuite transformés en liste entière à l'aide de list().
A = list(map(int, input().split()))

# Initialise une variable flag dont la valeur servira à indiquer si un nombre ne respecte pas la condition.
# Initialement, aucune violation n'a été trouvée, donc flag est 0.
flag = 0

# Parcourt chaque élément 'i' de la liste A à l'aide d'une boucle for.
for i in A:
    # Vérifie si 'i' est divisible par 2, c'est-à-dire si c'est un nombre pair.
    # L'opérateur % calcule le reste de la division de i par 2.
    # Si le reste est 0, alors i est pair.
    if i % 2 == 0:
        # Si 'i' est pair, on s'assure qu'il est divisible soit par 3, soit par 5.
        # On vérifie d'abord qu'il N'EST PAS divisible par 5 en vérifiant que i % 5 != 0.
        # Similairement, on vérifie qu'il N'EST PAS divisible par 3 avec i % 3 != 0.
        # Si les deux conditions sont vraies, alors le nombre pair ne satisfait pas la règle.
        if i % 5 != 0 and i % 3 != 0:
            # On signale que la règle n'est pas respectée en positionnant flag à 1.
            flag = 1
            # On quitte la boucle for immédiatement car il n'est pas nécessaire de vérifier la suite.
            break

# Après la boucle, on vérifie la valeur de flag pour décider du message à afficher.
if flag == 0:
    # Cela signifie que tous les nombres pairs étaient divisibles par 3 ou par 5.
    print('APPROVED')
else:
    # flag est égal à 1, ce qui veut dire qu'au moins un nombre pair ne respecte pas la condition.
    print('DENIED')