# AOJ 0066 Tic Tac Toe
# Python3 2018.6.15 bal4u (version commentée et documentée)

def check(board):
    """
    Détermine le gagnant d'une partie de Tic Tac Toe.

    Args:
        board (list): Une liste de 9 caractères représentant le plateau de jeu,
                      chaque case étant 'o', 'x', ou un caractère quelconque pour une case vide.

    Returns:
        str: 'o' si les 'o' gagnent, 'x' si les 'x' gagnent, 'd' si la partie est nulle.
    """
    # Parcourt chaque joueur possible ('o', 'x')
    for player in ['o', 'x']:
        # Vérifie les trois colonnes et les trois lignes
        for i in range(3):
            # Vérifie la colonne i (i, i+3, i+6)
            if board[i:9:3].count(player) == 3:
                return player
            # Vérifie la ligne i (3*i, 3*i+1, 3*i+2)
            if board[3*i:3*i+3].count(player) == 3:
                return player
        # Vérifie la diagonale principale (positions 0,4,8)
        if board[0:9:4].count(player) == 3:
            return player
        # Vérifie la diagonale secondaire (positions 2,4,6)
        if board[2:7:2].count(player) == 3:
            return player
    # Aucun gagnant trouvé, retourne 'd' pour "draw"
    return 'd'

# Boucle principale qui attend une entrée de l'utilisateur ligne par ligne
while True:
    try:
        # Lit la saisie utilisateur, la transforme en liste et affiche le résultat du check
        print(check(list(input())))
    except EOFError:
        # Sort de la boucle si le flux d'entrée est terminé (fin de fichier)
        break