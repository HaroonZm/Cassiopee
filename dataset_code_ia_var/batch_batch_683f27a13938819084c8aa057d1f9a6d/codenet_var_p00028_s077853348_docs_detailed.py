def read_integers_from_input():
    """
    Lit des entiers depuis l'entrée standard jusqu'à la fin du flux (EOF).
    
    Retourne:
        list: Une liste des entiers lus.
        
    Comportement:
        Lit chaque ligne saisie, la convertit en entier et l'ajoute à la liste.
        Arrête la lecture lorsque l'entrée standard est terminée (EOFError).
    """
    a = []
    try:
        while True:
            # Lit une ligne de l'entrée, la convertit en entier et l'ajoute à la liste
            a.append(int(input()))
    except EOFError:
        # Fin de l'entrée : on quitte la boucle
        pass
    return a

def compter_occurrences(liste_entiers):
    """
    Compte le nombre d'occurrences de chaque entier dans la liste (bornée à 0-100).
    
    Args:
        liste_entiers (list): Liste d'entiers compris entre 0 et 100.
        
    Retourne:
        list: Une liste de taille 101 où chaque index i correspond au nombre d'occurrences de l'entier i.
    """
    # Initialiser une liste de 101 zéros pour compter les entiers de 0 à 100
    counts = [0] * 101
    for n in liste_entiers:
        # Incrémenter le compteur pour la valeur lue n
        counts[n] += 1
    return counts

def afficher_entiers_max_occurrence(liste_entiers, occurrences):
    """
    Affiche chaque entier apparaissant le plus souvent dans la liste d'entrée (0-100).
    
    Args:
        liste_entiers (list): La liste des entiers d'origine.
        occurrences (list): Liste des occurrences des entiers, où occurrences[i] est le nombre d'apparitions de i.
        
    Comportement:
        Parcourt la position et, pour chaque entier rencontré en entrée, affiche sa valeur s'il
        correspond au nombre maximal d'occurrences.
        (Note: Le code original affiche plusieurs fois un même entier
        s'il figure plusieurs fois dans la liste d'origine et est majoritaire.)
    """
    # Recherche du nombre d'occurrences maximal pour tous les entiers
    max_occ = max(occurrences)
    # Parcours des indices correspondants à chaque élément de la liste saisie
    for n in range(len(liste_entiers)):
        # Si l'occurrence de la valeur courante est maximale, l'afficher
        if occurrences[liste_entiers[n]] == max_occ:
            print(liste_entiers[n])

def main():
    """
    Fonction principale orchestrant la lecture, le comptage et l'affichage
    des éléments les plus fréquents dans la liste d'entrée.
    """
    # Étape 1 : Lecture des entiers depuis l'entrée
    a = read_integers_from_input()
    # Étape 2 : Comptage des occurrences de chaque entier (supposé dans [0, 100])
    counts = compter_occurrences(a)
    # Étape 3 : Affichage des valeurs les plus fréquentes (selon la logique originale)
    afficher_entiers_max_occurrence(a, counts)

if __name__ == "__main__":
    main()