# Définition de la fonction récursive 'e' qui prend deux paramètres x et y, représentant des coordonnées sur une grille.
def e(x, y):
    # Ici, 'A' est une variable globale qui représente une grille (une liste de listes).
    # Nous modifions la valeur à la position (y, x) de la grille pour la chaîne de caractères '0'.
    # Cela signifie que la case à la position (x, y) est marquée ou visitée.
    A[y][x] = '0'
    # La boucle parcourt une liste de décalages (dx, dy) qui sont des déplacements horizontaux ou verticaux
    # Soit 3 cases à gauche/droite (x), soit 3 cases en haut/bas (y), sans diagonal.
    for dx, dy in [[-3, 0], [-2, 0], [-1, 0], [1, 0], [2, 0], [3, 0], [0, -3], [0, -2], [0, -1], [0, 1], [0, 2], [0, 3]]:
        # On vérifie que la nouvelle position (x+dx, y+dy) est toujours dans les limites de la grille 8x8.
        # '0 <= x+dx < 8' signifie que (x+dx) est une coordonnée horizontale valide.
        # '0 <= y+dy < 8' signifie que (y+dy) est une coordonnée verticale valide.
        if 0 <= x + dx < 8 and 0 <= y + dy < 8:
            # On vérifie aussi que la case à la nouvelle position contient '1'.
            # Cette condition implique que la case est "active" ou "non visitée" selon le contexte.
            if A[y + dy][x + dx] == '1':
                # Si les conditions sont satisfaites, on appelle récursivement la fonction 'e' sur cette nouvelle case.
                # Cela permet de continuer à explorer la grille depuis cette case.
                e(x + dx, y + dy)

# La boucle principale qui va s'exécuter un certain nombre de fois donné par l'entrée utilisateur.
# 'int(input())' lit une ligne de l'entrée standard, la convertit en entier, et contrôle le nombre d'itérations.
for i in range(int(input())):
    # Affiche un en-tête indiquant le numéro actuel des données traitées.
    print(f'Data {i+1}:')
    # Lit une ligne d'entrée et ne fait rien avec, probablement pour sauter une ligne vide ou un séparateur.
    input()
    # Création de la grille 'A' comme une liste de 8 listes (représentant 8 lignes).
    # Chaque ligne est obtenue en lisant une ligne d'entrée texte avec input() et en transformant cette chaîne en liste de caractères.
    A = [list(input()) for _ in [0] * 8]
    # Appel de la fonction 'e' sur les coordonnées lues en entrée (decrementées de 1 car l'entrée semble être en base 1).
    e(int(input()) - 1, int(input()) - 1)
    # Une fois le processus terminé, on imprime chaque ligne de la grille modifiée.
    # Pour chaque ligne 'r' dans A, on affiche les caractères sans espaces entre eux grâce à 'sep=""'.
    for r in A:
        print(*r, sep='')