def check_winner(a):
    """
    Analyse une chaîne représentant l'état d'une grille de jeu (ex : Tic-Tac-Toe)
    et détermine si le joueur 'o' ou 'x' gagne, ou si la partie est un match nul ('d').

    Args:
        a (str): Chaîne de 9 caractères représentant la grille de jeu.

    Returns:
        str: 'o' si le joueur 'o' gagne, 'x' si le joueur 'x' gagne, sinon 'd' pour match nul.
    """

    # Vérifie les deux diagonales principales
    # La première diagonale est accessible via a[::4] (indices 0, 4, 8)
    # La seconde via a[2:8:2] (indices 2, 4, 6)
    if a[::4] == "ooo" or a[2:8:2] == "ooo":
        return "o"
    elif a[::4] == "xxx" or a[2:8:2] == "xxx":
        return "x"
    else:
        # Vérifie les lignes et les colonnes
        for i in range(3):
            # Vérifie la ligne i (ex: 0-2, 3-5, 6-8)
            if a[3*i:3*(i+1)] == "ooo" or a[i::3] == "ooo":
                return "o"
            # Vérifie pour 'x' aussi dans la ligne i ou la colonne i
            elif a[3*i:3*(i+1)] == "xxx" or a[i::3] == "xxx":
                return "x"
            # Si c'est la dernière itération et aucun gagnant détecté, renvoie 'd' pour match nul
            elif i == 2:
                return "d"

def main():
    """
    Boucle principale qui attend l'entrée utilisateur, vérifie le gagnant pour chaque ligne,
    et affiche le résultat approprié.
    La boucle se termine lorsqu'une exception se produit (ex : fin de fichier).
    """
    while True:
        try:
            # Récupère l'entrée utilisateur (doit être une chaîne de 9 caractères)
            a = raw_input()
            # Appelle la fonction de vérification et imprime le résultat
            print(check_winner(a))
        except:
            # Quitte la boucle en cas d'exception (ex : EOFError)
            break

# Lance le programme principal
main()