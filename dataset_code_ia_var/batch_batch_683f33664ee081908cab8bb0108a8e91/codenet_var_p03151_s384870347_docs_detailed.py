def minimum_operations_to_balance_lists():
    """
    Lit les entrées utilisateurs, calcule et affiche le nombre minimal d'opérations nécessaires
    pour rendre la somme des éléments de a_list supérieure ou égale à la somme de b_list,
    en utilisant les surplus des éléments positifs de a_list par rapport à b_list
    pour compenser les déficits.

    Entrée :
        - Un entier n indiquant la taille des listes.
        - Deux listes d'entiers a_list et b_list de longueur n.

    Sortie :
        - Affiche -1 si la somme de a_list < somme de b_list.
        - Sinon, affiche le nombre minimal d'opérations nécessaires.
    """

    # Lecture du nombre d'éléments dans les listes
    n = int(input())

    # Lecture de la première liste et conversion en entiers
    a_list = list(map(int, input().split()))

    # Lecture de la seconde liste et conversion en entiers
    b_list = list(map(int, input().split()))

    # Si la somme de a_list est inférieure à celle de b_list, impossible de compenser
    if sum(a_list) < sum(b_list):
        print(-1)
        return

    # Calcul de la différence élément par élément entre a_list et b_list
    diff_list = [a_list[i] - b_list[i] for i in range(n)]

    # Liste pour stocker les excédents (différences positives)
    posi_list = []
    # Compteur de cas déficitaires et somme totale des déficits
    cnt, diff_sum = 0, 0

    # Parcours de chaque différence pour classer excédents et déficits
    for diff in diff_list:
        if diff < 0:
            # Cas d'un déficit : on incrémente le compteur et ajoute au déficit total
            cnt += 1
            diff_sum += diff
        elif diff > 0:
            # Cas d'un excédent : on ajoute à la liste des excédents
            posi_list.append(diff)

    # La somme totale à compenser doit être positive
    diff_sum *= -1

    # Tri des excédents par ordre décroissant pour combler au mieux les déficits
    posi_list.sort(reverse=True)

    # Initialisation de l'indice et de la somme cumulée des excédents pris
    i, S = 0, 0
    # On ajoute les plus gros excédents successivement jusqu'à compenser le déficit total
    while S < diff_sum:
        S += posi_list[i]
        i += 1

    # Impression du nombre minimal d'opérations nécessaires (cas déficitaires + compensations)
    print(i + cnt)