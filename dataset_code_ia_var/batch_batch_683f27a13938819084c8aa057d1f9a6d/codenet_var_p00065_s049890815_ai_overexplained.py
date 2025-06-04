# Initialisation d'un compteur qui servira à savoir si une erreur (par exemple une fin d'entrée) est survenue.
cnt = 0

# Création de deux listes vides 'a' et 'b' qui serviront plus tard dans le programme.
a, b = [], []

# Création d'un dictionnaire vide 'l'. Ce dictionnaire servira à stocker des clés (ici, les valeurs de 'n') associées à des listes de deux entiers.
l = {}

# Démarrage d'une boucle infinie pour permettre la lecture continue d'entrées utilisateur.
while 1:
    try:
        # Lecture d'une ligne d'entrée utilisateur par raw_input().
        # La ligne attendue doit contenir deux nombres séparés par une virgule, comme '5,7'.
        n, k = map(int, raw_input().split(',')) # Conversion des valeurs lues en entiers.

        # On vérifie si le dictionnaire 'l' contient déjà la clé 'n' avec l.has_key(n).
        if l.has_key(n):
            # Si 'n' existe déjà dans 'l', on incrémente le premier élément de la liste associée à la clé 'n' de 1. 
            # Cela compte le nombre d'occurrences de 'n'.
            l[n][0] += 1

            # Si 'cnt' vaut 1, on force la mise à 2 du deuxième élément de la liste associée à la clé 'n'.
            # Cette ligne marque que cette clé 'n' a été rencontrée après la première erreur d'entrée.
            if cnt == 1:
                l[n][1] = 2
        # Si on n'a pas encore fait d'erreur de lecture ('cnt' vaut 0) ET que 'n' n'est pas déjà dans le dictionnaire :
        elif cnt == 0:
            # On insère une nouvelle entrée avec comme valeur une liste [1,1].
            # 1er élément = compteur d'apparitions, 2e élément = statut/propriété (toujours 1 à l'initialisation)
            l[n] = [1, 1]
    except:
        # Si une erreur se produit pendant la lecture/traitement de l'entrée (ex : EOF, syntaxe invalide),
        # on incrémente le compteur d'erreur 'cnt' de 1.
        cnt += 1

        # Si c'est au moins la deuxième erreur (autrement dit, le flux d'entrée est bien terminé),
        # on sort de la boucle avec break.
        if cnt > 1:
            break

# Parcours de toutes les clés du dictionnaire l
for i in l:
    # On regarde si le deuxième élément de la valeur associée à la clé 'i' vaut 2.
    # Cela indique que la clé 'i' a été remarquée après la première erreur d'entrée.
    if l[i][1] == 2:
        # On ajoute une sous-liste [i, l[i][0]] à la liste 'a'.
        # [i, l[i][0]] = numéro lu, nombre d'occurrences après interruption
        a.append([i, l[i][0]])

# Tri de la liste 'a' par ordre croissant des valeurs de 'i', c'est-à-dire des numéros enregistrés.
a.sort()

# Parcours de tous les éléments de la liste triée 'a'
for i in a:
    # Affichage des éléments, chaque ligne contient le numéro 'i[0]' et son compteur d'occurrences 'i[1]', séparés par un espace
    print i[0], i[1]