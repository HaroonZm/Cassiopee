# Demande à l'utilisateur de saisir un nombre entier qui sera stocké dans la variable 'n'.
# Cette variable représente le nombre d'éléments que nous allons traiter ensuite.
n = int(input())

# Récupère les éléments d'entrée de l'utilisateur sous forme de chaîne de caractères,
# les divise en sous-chaînes et les convertit chacune en entier.
# L'ensemble est stocké dans la liste 'h'.
h = list(map(int, input().split()))

# Initialise une variable booléenne nommée 'judge' à True.
# Cette variable servira de drapeau pour indiquer si la condition du problème est remplie.
judge = True

# Démarre une boucle qui s'exécute pour chaque indice 'i' allant de 0 à n-2 (inclus),
# ce qui signifie qu'on s'arrête avant le dernier élément de la liste 'h' car on va comparer des paires consécutives.
for i in range(n - 1):
    # Vérifie si l'élément courant dans la liste 'h' est strictement supérieur à l'élément suivant.
    if h[i] > h[i + 1]:
        # Si c'est le cas, la condition attendue n'est pas respectée.
        # On attribue la valeur False à la variable 'judge' pour signaler que la séquence ne répond pas à la contrainte.
        judge = False
        # Utilise 'break' pour arrêter immédiatement la boucle car il est inutile d'effectuer d'autres vérifications.
        break
    # Si l'élément courant n'est pas supérieur mais qu'il est différent du suivant,
    # cela signifie qu'il est inférieur, donc nous procédons à l'étape suivante.
    elif h[i] != h[i + 1]:
        # On décrémente l'élément suivant de la liste 'h' de 1 unité.
        # Cela ajuste la séquence pour la comparer de nouveau lors du prochain passage dans la boucle,
        # dans le but de satisfaire une certaine condition de non-décroissance permise par décrément.
        h[i + 1] = h[i + 1] - 1
        # Cette opération modifie directement la liste d'origine.

# Après la boucle, on vérifie si le drapeau 'judge' est resté à True,
# ce qui signifierait que la séquence respecte la contrainte demandée dans le problème.
if judge:
    # Affiche "Yes" pour indiquer le succès.
    print("Yes")
else:
    # Affiche "No" si au moins une des comparaisons dans la boucle n'a pas respecté la règle.
    print("No")