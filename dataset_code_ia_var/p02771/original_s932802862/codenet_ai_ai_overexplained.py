# Demande à l'utilisateur de saisir une ligne de texte. La fonction input() attend une entrée utilisateur sous forme de chaîne de caractères.
ligne = input()

# Utilise la méthode split() sur la chaîne obtenue pour diviser la chaîne là où il y a des espaces.
# Cela produit une liste de sous-chaînes, chacune représentant un nombre entré par l'utilisateur en tant que chaîne de caractères.
valeurs = ligne.split()

# Utilise une compréhension de liste pour parcourir chaque élément, c'est-à-dire chaque chaîne de caractères dans la liste 'valeurs'.
# Transforme chaque chaîne de caractères représentant un nombre en un entier avec la fonction int().
# Construit une nouvelle liste 'a' qui contient tous ces entiers.
a = [int(i) for i in valeurs]

# Trie la liste 'a' en ordre croissant.
# L'appel à la méthode sort() réorganise les éléments dans la liste de façon à ce qu'ils soient du plus petit au plus grand.
a.sort()

# Vérifie une condition complexe pour savoir si exactement deux des trois entiers sont égaux et le troisième est différent.
# 'a[0]' correspond au premier élément (le plus petit après tri), 'a[1]' au deuxième, 'a[2]' au troisième (le plus grand après tri).

# Première partie de la condition : (a[0] == a[1] and a[1] != a[2])
# Vérifie si les deux premiers éléments sont égaux (c'est-à-dire au moins un doublon au début)
# et si ces deux-là sont différents du troisième.

# Seconde partie de la condition : (a[0] != a[1] and a[1] == a[2])
# Vérifie si le premier est différent du deuxième, mais le deuxième est égal au troisième (doublon en fin de liste triée).

# L'opérateur 'or' signifie que si une des deux conditions est vraie, la réponse globale est vraie.
if (a[0] == a[1] and a[1] != a[2]) or (a[0] != a[1] and a[1] == a[2]):
    # Si la condition ci-dessus est vraie, affiche la chaîne "Yes" à l'écran pour indiquer que deux éléments sont identiques.
    print("Yes")
else:
    # Sinon, affiche "No" pour signifier que la condition n'était pas satisfaite.
    print("No")