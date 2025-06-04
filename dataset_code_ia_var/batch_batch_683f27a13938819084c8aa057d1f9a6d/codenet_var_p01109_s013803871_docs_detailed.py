def count_below_average_numbers():
    """
    Lit plusieurs ensembles d'entiers depuis l'entrée standard, 
    calcule la moyenne de chaque ensemble et affiche, pour chaque ensemble, 
    le nombre d'entiers inférieurs ou égaux à la moyenne.

    La lecture se termine lorsqu'un zéro est saisi pour la taille de l'ensemble.
    """
    while True:
        # Lecture du nombre d'éléments dans la séquence à traiter
        n = int(input())
        # Si l'utilisateur saisit 0, arrêter la boucle
        if n == 0:
            break
        # Lecture des éléments de la séquence et conversion en liste d'entiers
        a = list(map(int, input().split()))
        # Calcul de la moyenne arithmétique des éléments
        avg = sum(a) / n
        # Création d'une liste contenant les éléments inférieurs ou égaux à la moyenne
        below_avg = [i for i in a if i <= avg]
        # Affichage du nombre d'éléments inférieurs ou égaux à la moyenne
        print(len(below_avg))

# Appel de la fonction principale
count_below_average_numbers()