# Lecture de deux entiers depuis l'entrée standard (par exemple : '3 4'), 
# puis conversion des chaînes de caractères en entiers grâce à map(int, ...)
# et assignation à H (hauteur) et W (largeur)
H, W = map(int, input().split())

# Création d'une liste S qui va contenir H éléments.
# Chacun de ces éléments est une liste résultant de l'appel input().split().
# Par exemple, si H vaut 2 et les entrées suivantes sont :
# 'apple orange snuke banana'
# 'peach snuke grape apple'
# alors S = [['apple', 'orange', 'snuke', 'banana'], ['peach', 'snuke', 'grape', 'apple']]
S = [input().split() for _ in range(H)]

# Boucle extérieure sur la variable de ligne i, qui prend les valeurs de 0 à H-1 (inclus)
for i in range(H):
    # Boucle intérieure sur la variable de colonne j, qui prend les valeurs de 0 à W-1 (inclus)
    for j in range(W):
        # Vérifier si l'élément de S à la position ligne i et colonne j est égal à la chaîne 'snuke'
        if S[i][j] == 'snuke':
            # Si la condition précédente est satisfaite, on effectue la suite des opérations suivantes :

            # Pour convertir l'indice de colonne j en une lettre majuscule :
            # 1. La fonction ord('A') retourne le code ASCII du caractère 'A', soit 65
            # 2. En additionnant j, cela nous permet de passer à la lettre correspondante
            #    exemple : j = 0 donne 65 + 0 = 65 --> chr(65) = 'A'
            #    exemple : j = 3 donne 65 + 3 = 68 --> chr(68) = 'D'
            # 3. chr(...) convertit ce code numérique en lettre majuscule
            letter = chr(ord('A') + j)

            # Les lignes sont numérotées à partir de 1 (alors que i commence à 0)
            # Donc on ajoute 1 à i, puis on convertit en chaîne de caractères via str(...)
            number = str(i + 1)

            # On concatène la lettre de colonne avec le numéro de ligne pour afficher la position
            # Exemple : Colonne j = 2, ligne i = 0 --> 'C1'
            print(letter + number)