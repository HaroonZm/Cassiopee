# Création d'une liste appelée 'n' qui va contenir 28 éléments.
# Chaque élément de la liste est un entier saisi par l'utilisateur via la fonction input().
# La fonction int() convertit la chaîne de caractères reçue par input() en un nombre entier.
# La boucle for i in range(28) s'assure que cette opération est répétée 28 fois,
# c'est-à-dire que 28 nombres entiers seront demandés à l'utilisateur.
n=[int(input()) for i in range(28)]

# Boucle for qui va prendre successivement des valeurs de j allant de 1 à 30 inclus.
# range(1,31) génère une séquence de nombres entiers allant de 1 (inclus) à 31 (exclus),
# donc de 1 à 30.
for j in range(1,31):
    # Condition qui vérifie si la valeur courante de j n'est pas dans la liste n.
    # L'opérateur 'not in' renvoie True si j n'appartient pas à la liste n.
    if j not in n:
        # Si la condition est vraie, afficher la valeur de j à l'écran.
        # La fonction print() affiche le contenu de j sur la sortie standard (console).
        print(j)