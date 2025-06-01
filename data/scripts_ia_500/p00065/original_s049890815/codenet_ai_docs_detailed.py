def process_input():
    """
    Lit des paires d'entiers (n, k) séparés par une virgule depuis l'entrée standard.
    Le processus est divisé en deux phases : avant et après une interruption.
    Pour chaque n lu, compte le nombre d'occurrences et suit un indicateur selon la 
    phase dans laquelle il apparaît.

    Retourne :
        dict : Un dictionnaire où la clé est n et la valeur est une liste [compte, indicateur].
               * compte : nombre d'occurrences de n
               * indicateur : 1 si n est apparu uniquement dans la première phase,
                              2 s'il est réapparu dans la deuxième phase.
    """
    cnt = 0  # Compteur indiquant la phase actuelle de lecture des entrées
    l = {}   # Dictionnaire pour stocker les données sous forme {n: [compte, indicateur]}
    while True:
        try:
            # Lecture d'une ligne, format attendu "n,k" où n et k sont des entiers
            n, k = map(int, raw_input().split(','))
            if n in l:
                # Si n a déjà été rencontré auparavant, incrémenter le compteur d'occurrences
                l[n][0] += 1
                # Si on est dans la deuxième phase (cnt == 1), changer l'indicateur à 2
                if cnt == 1:
                    l[n][1] = 2
            else:
                # Si n n'a pas été rencontré, l'ajouter avec un compteur à 1
                # et un indicateur selon la phase : 1 pour première phase uniquement
                if cnt == 0:
                    l[n] = [1, 1]
        except:
            # En cas d'exception (fin de la première phase ou erreur de lecture)
            cnt += 1
            # Sortir de la boucle après la deuxième phase
            if cnt > 1:
                break
    return l


def filter_and_sort_data(data):
    """
    Filtre les entrées ayant un indicateur égal à 2 (celles présentes dans les deux phases)
    et crée une liste triée de tuples [n, compte].

    Args:
        data (dict): Dictionnaire d'entrée sous la forme {n: [compte, indicateur]}.

    Retourne :
        list : Liste triée de listes [n, compte] où indicateur == 2.
    """
    # Liste pour recueillir les n avec indicateur == 2 et leur nombre d'occurrences
    a = []

    for i in data:
        # Ne conserver que ceux qui ont été vus dans la deuxième phase
        if data[i][1] == 2:
            a.append([i, data[i][0]])
    # Trier la liste selon la valeur n
    a.sort()
    return a


def main():
    """
    Fonction principale qui orchestre la lecture des données, le traitement et l'affichage
    des résultats finaux.
    """
    # Traitement des entrées
    data = process_input()
    # Filtrage et tri des données pertinentes
    filtered_data = filter_and_sort_data(data)
    # Affichage des résultats
    for item in filtered_data:
        print item[0], item[1]


# Exécution de la fonction principale
if __name__ == "__main__":
    main()