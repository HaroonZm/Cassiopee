# Demande à l'utilisateur de saisir trois entiers séparés par des espaces, puis attribue les valeurs respectives à A, B et C
# La fonction input() lit la saisie utilisateur sous forme de chaîne de caractères
# La méthode split() découpe la chaîne d'entrée en une liste de sous-chaînes, en les séparant par des espaces
# La fonction map(int, ...) convertit chaque élément de la liste en un entier (int)
# Enfin, les trois entiers extraits sont affectés aux variables A, B et C, respectivement
A, B, C = map(int, input().split())

# Vérifie si la première condition suivante est vraie :
# - A est égal à B (A == B) : cela signifie que les deux premières valeurs sont identiques
# - A est différent de C (A != C) : cela signifie que la première et la troisième valeur sont différentes
if A == B and A != C:
    # Si la condition ci-dessus est remplie, affiche "Yes" à l'écran
    print("Yes")

# Si la condition précédente n'est pas satisfaite, vérifie la condition suivante :
# - A est égal à C (A == C) : la première et la troisième valeur sont identiques
# - B est différent de C (B != C) : la deuxième et la troisième valeur sont différentes
elif A == C and B != C:
    # Si cette condition est remplie, affiche "Yes" à l'écran
    print("Yes")

# Si aucune des précédentes conditions n'est satisfaite, vérifie la condition suivante :
# - C est égal à B (C == B) : la deuxième et la troisième valeur sont identiques
# - A est différent de C (A != C) : la première et la troisième valeur sont différentes
elif C == B and A != C:
    # Si cette condition est remplie, affiche "Yes"
    print("Yes")

# Si aucune des conditions précédentes n'est remplie, alors aucune paire de valeurs ne satisfait exactement les contraintes
# Cela veut dire soit que toutes les valeurs sont différentes, soit que toutes sont égales
else:
    # Affiche "No" à l'écran car aucune combinaison n'a été trouvée où deux valeurs sont identiques et la troisième est différente
    print("No")