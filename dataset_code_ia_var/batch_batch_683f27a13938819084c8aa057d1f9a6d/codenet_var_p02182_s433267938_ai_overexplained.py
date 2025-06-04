# Demande à l'utilisateur d'entrer deux entiers séparés par un espace, les convertit en entier et les assigne à n et m respectivement.
# n représente le nombre de lignes et m le nombre de colonnes pour les grilles suivantes.
n, m = map(int, input().split())

# Initialise la liste 'a' qui représentera la première grille de caractères.
# Utilise une compréhension de liste pour construire une liste de n éléments, où chaque élément est une liste de listes de caractères correspondant à une ligne.
# 'list(input())' convertit la chaîne saisie en une liste de caractères, de sorte que chaque élément de la liste interne est un caractère de la ligne.
# 'list(list(input()))' est redondant, car 'list(input())' est déjà suffisant, mais cela n'affecte pas le résultat.
a = [list(list(input())) for i in range(n)]

# Initialise la liste 'b' qui représentera la deuxième grille de caractères, selon le même procédé que pour 'a'.
b = [list(list(input())) for i in range(n)]

# Initialise un compteur 'cout' à zéro. Ce compteur va garder le nombre de différences entre les deux grilles.
cout = 0

# Parcourt chaque ligne des deux grilles à l'aide d'une boucle for, 'i' prend les valeurs de 0 à n-1 (inclus).
for i in range(n):
    # Parcourt chaque colonne de la ligne en cours pour comparer chaque caractère, 'j' prend les valeurs de 0 à m-1 (inclus).
    for j in range(m):
        # Compare le caractère correspondant dans la grille 'a' et la grille 'b' à la position (i, j).
        # Si les caractères sont différents, cela signifie qu'il y a une différence à cet emplacement.
        if a[i][j] != b[i][j]:
            # Incrémente le compteur 'cout' de 1 pour signaler une différence trouvée.
            cout += 1

# Affiche le nombre total de différences trouvées entre les deux grilles.
print(cout)