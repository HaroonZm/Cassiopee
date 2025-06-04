# On commence par lire une ligne d'entrée utilisateur via la fonction input()
# Cette entrée contient plusieurs valeurs séparées par des espaces, que l'on souhaite convertir en entiers.
# On utilise la fonction map pour appliquer int à chaque élément de l'entrée séparée avec split()
I, O, _, J, L, _, _ = map(int, input().split())

# On calcule la première possibilité (ans1) selon la logique suivante :
# O : nombre d'éléments de type O, ajoutés directement.
# I-I%2 : on retire le modulo 2 de I à I pour obtenir le plus grand pair <= I.
# J-J%2 : de même pour J, le plus grand pair <= J.
# L-L%2 : de même pour L, le plus grand pair <= L.
# On additionne le tout pour obtenir ans1.
ans1 = O + I - I % 2 + J - J % 2 + L - L % 2

# Initialisation d'une variable ans2 à 0, elle va stocker la seconde possibilité de résultat.
ans2 = 0

# On vérifie si I, J et L sont tous positifs (différents de zéro).
# Cela signifie qu'il y a au moins un de chaque type (I, J, L).
if I and J and L:
    # Si c'est le cas, on retire 1 à chacun pour représenter la sélection d'un de chaque (I, J, L).
    I, J, L = I - 1, J - 1, L - 1
    # On ajoute 3 pour les trois éléments sélectionnés, plus O, plus le plus grand pair dans les restes.
    ans2 = 3 + O + I - I % 2 + J - J % 2 + L - L % 2

# On affiche la valeur maximale obtenue entre ans1 et ans2 à l'aide de la fonction max
print(max(ans1, ans2))