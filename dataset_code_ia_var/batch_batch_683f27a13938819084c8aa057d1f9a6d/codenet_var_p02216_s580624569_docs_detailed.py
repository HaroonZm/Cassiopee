def get_game_result(N, A):
    """
    Détermine le gagnant d'un jeu basé sur la parité de la taille de la liste et de ses éléments.
    
    Arguments:
    N -- int, nombre d'éléments dans la liste A.
    A -- list of int, liste des entiers représentant les objets du jeu.
    
    Retourne:
    "First" ou "Second" selon les règles du jeu décrites.
    """
    # Si N est impair
    if N % 2 == 1:
        # Si la somme de tous les éléments de A est impaire, "First" gagne
        if sum(A) % 2 == 1:
            return "First"
        # Sinon "Second" gagne
        else:
            return "Second"
    # Si N est pair
    else:
        # Si la plus petite valeur dans A est impaire, "First" gagne
        if min(A) % 2 == 1:
            return "First"
        else:
            # Si la somme de A est paire, "Second" gagne
            if sum(A) % 2 == 0:
                return "Second"
            # Sinon, "First" gagne
            else:
                return "First"

def main():
    """
    Fonction principale qui lit les entrées utilisateur, appelle les fonctions de traitement,
    et affiche le résultat.
    """
    # Lecture du nombre d'éléments
    N = int(input())
    # Lecture de la liste d'entiers A
    A = list(map(int, input().split()))
    
    # Calcul et affichage du résultat selon les règles du jeu
    result = get_game_result(N, A)
    print(result)

# Appel du point d'entrée principal du script
if __name__ == "__main__":
    main()