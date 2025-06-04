def determine_winner():
    """
    Demande à l'utilisateur un entier n, puis lit une liste de n entiers.
    L'algorithme détermine le gagnant ("First" ou "Second") selon :
    - La somme totale de la liste (si impaire, "First" gagne)
    - Si n est pair ET le minimum de la liste est impair, "First" gagne
    - Sinon, "Second" gagne

    Affiche directement le résultat.
    """
    # Lecture du nombre d'éléments dans la liste
    n = int(input())
    
    # Lecture de la liste de n entiers
    # input().split() sépare la ligne en chaînes, map(int, ...) les convertit en entiers, puis list() les regroupe en liste
    a = list(map(int, input().split()))
    
    # Calcul du plus petit élément de la liste a
    t = min(a)
    
    # Calcul de la somme des éléments de la liste
    s = sum(a)
    
    # Vérifie les conditions pour déterminer le gagnant :
    # - Si la somme est impaire (s % 2 == 1), le premier joueur gagne
    # - Sinon, si n est pair (n % 2 == 0) ET le minimum est impair (t % 2 == 1), le premier joueur gagne
    # - Dans tous les autres cas, le second joueur gagne
    if s % 2 == 1 or (n % 2 == 0 and t % 2 == 1):
        print('First')
    else:
        print('Second')


# Appel de la fonction principale pour lancer le programme
determine_winner()