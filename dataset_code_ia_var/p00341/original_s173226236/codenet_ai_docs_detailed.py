def check_triplet_equality():
    """
    Demande à l'utilisateur de saisir une ligne d'entrée, découpe la saisie en une liste,
    trie la liste, puis vérifie si les 12 éléments regroupés en trois groupes de quatre
    sont tous égaux au sein de chaque groupe.
    Affiche 'yes' si la condition est remplie, 'no' sinon.
    """
    # Lire l'entrée utilisateur et couper la chaîne par les espaces en une liste
    input_list = list(input().split())
    
    # Trier la liste pour regrouper les éléments identiques
    input_list.sort()
    
    # Vérifier l'égalité dans les trois groupes de quatre éléments consécutifs
    first_group_equal = input_list[0] == input_list[1] == input_list[2] == input_list[3]
    second_group_equal = input_list[4] == input_list[5] == input_list[6] == input_list[7]
    third_group_equal = input_list[8] == input_list[9] == input_list[10] == input_list[11]
    
    # Si chaque groupe possède quatre éléments identiques, afficher 'yes', sinon 'no'
    if first_group_equal and second_group_equal and third_group_equal:
        print('yes')
    else:
        print('no')

# Appeler la fonction principale
check_triplet_equality()