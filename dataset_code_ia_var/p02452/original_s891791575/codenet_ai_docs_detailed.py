def is_subset():
    """
    Demande à l'utilisateur deux ensembles d'entiers et vérifie 
    si le second ensemble est un sous-ensemble du premier.
    Affiche 1 si c'est le cas, sinon affiche 0.
    """
    # Lecture du nombre d'éléments dans le premier ensemble
    n = int(input())
    # Lecture des éléments du premier ensemble et conversion en set d'entiers
    a = set(map(int, input().split()))
    # Lecture du nombre d'éléments dans le second ensemble
    m = int(input())
    # Lecture des éléments du second ensemble et conversion en set d'entiers
    b = set(map(int, input().split()))
    
    # On vérifie si tous les éléments de b sont dans a.
    # Cela revient à vérifier que la différence d'ensemble b-a est vide.
    if b - a:
        # b contient des éléments qui ne sont pas dans a : ce n'est pas un sous-ensemble
        print(0)
    else:
        # Tous les éléments de b sont dans a : c'est un sous-ensemble
        print(1)

# Appel de la fonction principale pour exécuter le programme
is_subset()