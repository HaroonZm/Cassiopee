# Création d'une liste nommée M contenant les entiers de 1 à 30 inclus.
# La fonction range(1, 31) génère une séquence de nombres entiers commençant à 1 (inclus) et se terminant avant 31 (exclus).
# La fonction list() convertit cette séquence en une liste explicite.
M = list(range(1, 31))

# Boucle for qui va itérer 28 fois.
# La fonction range(28) génère une séquence de nombres de 0 à 27.
# La variable i précise l'indice courant de l'itération mais ici, elle n'est pas utilisée dans la boucle.
for i in range(28):
    # Demande à l'utilisateur d'entrer un nombre entier.
    # La fonction input() récupère une chaîne de caractères tapée par l'utilisateur.
    # La fonction int() convertit cette chaîne de caractères en un entier.
    S = int(input())
    
    # Suppression de l'entier S de la liste M.
    # La méthode remove() enlève la première occurrence de la valeur donnée en argument dans la liste.
    # Cela modifie la liste M en place.
    M.remove(S)

# La liste M contient maintenant les nombres de 1 à 30 qui n'ont pas été entrés par l'utilisateur,
# c'est-à-dire les 2 nombres non saisis.

# Affichage du plus petit élément de la liste M.
# La fonction min() retourne la plus petite valeur contenue dans la liste M.
print(min(M))

# Affichage du plus grand élément de la liste M.
# La fonction max() retourne la plus grande valeur contenue dans la liste M.
print(max(M))