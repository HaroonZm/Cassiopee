def check_three_equal_sets():
    """
    Lit une ligne de l'entrée standard, interprète les valeurs comme des entiers,
    trie la liste des entiers, puis vérifie si les trois segments de 4 éléments consécutifs
    du tableau trié contiennent chacun des éléments identiques (autrement dit, composés d'une seule valeur distincte dans chaque segment).
    
    Affiche "yes" si cette condition est remplie, "no" sinon.
    """
    # Lecture de l'entrée, découpe en éléments, conversion en entiers
    numbers = input().split()          # Lecture de la ligne et découpage selon les espaces
    integer_list = list(map(int, numbers))  # Conversion des éléments en entiers

    # Trie la liste pour regrouper les éléments égaux
    integer_list.sort()

    # Découpe la liste triée en 3 segments de 4 éléments chacun
    first_group = integer_list[:4]
    second_group = integer_list[4:8]
    third_group = integer_list[8:]

    # Vérifie si chacun des groupes contient exactement une valeur unique
    first_unique = len(set(first_group)) == 1
    second_unique = len(set(second_group)) == 1
    third_unique = len(set(third_group)) == 1

    # Si tous les groupes sont identiques, affiche "yes", sinon "no"
    if first_unique and second_unique and third_unique:
        print("yes")
    else:
        print("no")

# Appel de la fonction principale
check_three_equal_sets()