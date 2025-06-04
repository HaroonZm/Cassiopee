import sys  # On importe le module sys qui fournit l'accès à certains objets utilisés ou maintenus par l'interpréteur Python.
from sys import stdin  # On importe stdin (entrée standard) depuis le module sys pour lire l'entrée utilisateur.
input = stdin.readline  # On redéfinit la fonction input pour qu'elle corresponde directement à stdin.readline, ce qui permet de lire une ligne complète depuis l'entrée standard (cela est souvent fait pour lire rapidement les entrées dans des contextes compétitifs).

def solve(board):  # Définition de la fonction 'solve' qui prend un argument 'board' représentant le plateau de jeu sous forme de liste de listes.
    colors = ['b', 'w']  # Liste contenant deux éléments : les couleurs 'b' (noir) et 'w' (blanc), qui sont les seuls jetons possibles dans le jeu.
    for c in colors:  # On parcourt chaque couleur dans la liste colors (d'abord 'b', puis 'w').
        for y in range(3):  # On parcourt les indices de lignes de 0 à 2 (il y a 3 lignes).
            # On compte le nombre de fois où la couleur courante 'c' apparaît dans la ligne 'y'.
            if board[y].count(c) == 3:  # Si la couleur 'c' apparaît exactement 3 fois dans la ligne (cela signifie que la ligne entière contient uniquement des 'c').
                return c  # On retourne la couleur 'c' qui a complété la ligne, ce qui signifie victoire pour cette couleur.
        for x in range(3):  # On parcourt les indices de colonnes de 0 à 2 (il y a 3 colonnes).
            # Cette condition vérifie verticalement : Elle regarde la colonne 'x' dans chaque ligne (board[0][x], board[1][x], board[2][x]).
            if board[0][x] == c and board[1][x] == c and board[2][x] == c:  # Si les trois cases de la colonne 'x' contiennent la couleur 'c'.
                return c  # On retourne la couleur 'c' qui a complété la colonne, donc victoire pour cette couleur.
        # La condition suivante vérifie la diagonale descendante de gauche à droite (de la case en haut à gauche à celle en bas à droite).
        if board[0][0] == c and board[1][1] == c and board[2][2] == c:  # Si toutes les cases de cette diagonale sont de couleur 'c'.
            return c  # On retourne la couleur 'c' qui a complété cette diagonale.
        # Cette condition vérifie la diagonale descendante de droite à gauche (de la case en haut à droite à celle en bas à gauche).
        if board[0][2] == c and board[1][1] == c and board[2][0] == c:  # Si toutes les cases de cette diagonale sont de couleur 'c'.
            return c  # On retourne la couleur 'c' qui a complété cette diagonale.
    return 'NA'  # Si aucune des conditions précédentes n'est remplie, cela signifie qu'il n'y a pas de gagnant, donc on retourne 'NA' (Not Available/None).

def main(args):  # Définition de la fonction 'main' qui prend en paramètre 'args', bien que non utilisé ici (il peut contenir des arguments de la ligne de commande).
    while True:  # On entre dans une boucle infinie pour pouvoir traiter plusieurs tableaux de jeu à la suite.
        temp = input().strip()  # On lit une ligne depuis l'entrée standard, puis on retire les espaces en début et fin avec 'strip()' pour nettoyer l'entrée.
        if temp[0] == '0':  # Si le premier caractère de cette ligne est '0', cela signifie que nous devons arrêter de traiter les entrées (condition d'arrêt).
            break  # On sort de la boucle infinie, ce qui termine l'exécution du programme principal.
        board = []  # On initialise une liste vide qui va recevoir les trois lignes du plateau de jeu.
        board.append(list(temp))  # On sépare chaque caractère de la première ligne (reçue dans temp) et on les place dans une sous-liste, puis on ajoute cette sous-liste à 'board'.
        board.append(list(input().strip()))  # On lit la deuxième ligne, on retire les éventuels espaces en bord, on transforme la chaîne en liste de caractères et on ajoute à 'board'.
        board.append(list(input().strip()))  # Même procédure pour la troisième ligne.
        result = solve(board)  # On appelle la fonction 'solve' avec le plateau 'board' pour déterminer s'il y a un gagnant ('b' ou 'w') ou non ('NA').
        print(result)  # On affiche le résultat retourné par 'solve' à l'écran.

if __name__ == '__main__':  # Cette condition vérifie si ce script est exécuté en tant que programme principal (et pas importé en tant que module depuis un autre script).
    main(sys.argv[1:])  # Si c'est le cas, on appelle la fonction 'main' en lui passant les arguments de la ligne de commande (sauf le premier qui est le nom du script, d'où [1:]), même si non utilisés dans ce cas.