def count_students_below_or_equal_average(n, scores):
    """
    Compte le nombre d'étudiants dont le score est inférieur 
    ou égal à la moyenne de la classe.

    Args:
        n (int): Nombre d'étudiants.
        scores (list of int): Liste des scores des étudiants.

    Returns:
        int: Nombre d'étudiants avec un score inférieur ou égal à la moyenne.
    """
    # Calcul de la moyenne arithmétique des scores
    average = sum(scores) / n
    # Initialisation du compteur pour suivre les scores <= moyenne
    count = 0
    for score in scores:
        if score <= average:
            count += 1
    return count

def main():
    """
    Fonction principale.
    Elle lit un nombre indéterminé de cas test sur l'entrée standard, 
    où chaque cas commence par un entier n (nombre d'étudiants) suivi d'une ligne
    contenant n entiers (les scores des étudiants).
    Pour chaque cas, tant que n != 0, elle affiche le nombre d'étudiants
    ayant un score inférieur ou égal à la moyenne.
    """
    try:
        while True:
            # Lecture du nombre d'étudiants
            n = int(input())
            # Si n est 0, fin du programme
            if n == 0:
                break
            # Lecture de la liste des scores pour n étudiants
            scores = list(map(int, input().split()))
            # Appel à la fonction de comptage et affichage du résultat
            result = count_students_below_or_equal_average(n, scores)
            print(result)
    except EOFError:
        # Sortie propre en cas de fin du flux d'entrée
        pass

if __name__ == "__main__":
    main()