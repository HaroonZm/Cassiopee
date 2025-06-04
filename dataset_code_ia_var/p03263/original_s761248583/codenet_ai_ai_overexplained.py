# Demander à l'utilisateur de saisir deux entiers séparés par un espace, ce qui représente la hauteur (H) et la largeur (W) de la grille
# input() prend tout ce qui est entré par l'utilisateur au clavier, et .split() divise cette chaîne autour des espaces pour obtenir une liste de deux éléments
# map(int, ...) applique la fonction int à chaque élément de cette liste, transformant les chaînes de caractères en entiers
# Les deux entiers sont ensuite respectivement stockés dans les variables H et W
H, W = map(int, input().split())

# Créer une liste vide 'a' qui va contenir les lignes de la grille
a = []

# Utiliser une boucle for pour parcourir chaque ligne de la grille. La variable 'i' prend les valeurs de 0 jusqu'à H-1 inclus
for i in range(H):
    # Pour chaque itération, lire une ligne d'entrée contenant W entiers séparés par des espaces
    # input() obtient la chaîne, .split() la divise autour des espaces
    # map(int, ...) convertit chaque valeur en entier
    # list(...) transforme le résultat en une liste d'entiers
    # Cette liste de W entiers est ajoutée à la liste 'a', qui devient une liste de listes (matrice)
    a.append(list(map(int, input().split())))

# Créer une liste vide 'move' qui va enregistrer les mouvements effectués
move = []

# Parcourir chaque case de la matrice 'a' à l'aide de deux boucles imbriquées
# La première boucle parcourt les lignes avec l'indice 'i', de 0 à H-1
for i in range(H):
    # La seconde boucle parcourt les colonnes avec l'indice 'j', de 0 à W-1
    for j in range(W):
        # Vérifier si la valeur actuelle a[i][j] est impaire
        # Le nombre est impair si le reste de la division par 2 (modulo) est égal à 1
        if a[i][j] % 2 == 1:
            # Si la colonne actuelle n'est pas la dernière colonne (colonne d'indice W-1)
            if j < W-1:
                # Ajouter à la liste 'move' le mouvement sous forme de liste [i, j, i, j+1],
                # c'est-à-dire un déplacement d'une pièce de (i, j) à (i, j+1)
                move.append([i, j, i, j+1])
                # Incrémenter la valeur de la case à droite (a[i][j+1]) de 1
                # Cela simule le transfert de l'objet impair vers la case de droite
                a[i][j+1] += 1
            # Si nous sommes dans la dernière colonne et que nous ne sommes pas à la dernière ligne
            elif i < H-1:
                # Ajouter à la liste 'move' un mouvement vers la case du dessous ([i, j, i+1, j])
                move.append([i, j, i+1, j])
                # Incrémenter la valeur de la case du dessous (a[i+1][j]) de 1
                a[i+1][j] += 1
        # Si la case a[i][j] est paire ou qu'aucun déplacement n'est possible, rien n'est fait

# Afficher le nombre total de mouvements réalisés
# len(move) donne la longueur de la liste 'move', soit le nombre de déplacements enregistrés
print(len(move))

# Parcourir tous les mouvements enregistrés dans la liste 'move'
# Pour chaque mouvement, décomposer les coordonnées stockées dans la liste en quatre variables : x, y, x2, y2
for x, y, x2, y2 in move:
    # Ajouter 1 à chaque coordonnée pour convertir de l'indexation à partir de 0 (commune en Python)
    # vers l'indexation à partir de 1 (souvent demandée dans les problèmes d'entrée/sortie ou pour être plus lisible)
    # Afficher les quatre valeurs correspondantes à ce déplacement
    print(x+1, y+1, x2+1, y2+1)