def calculate_minimum_encoding(S):
    """
    Calcule le coût minimum d'encodage d'une chaîne de caractères selon 
    l'algorithme de Huffman modifié, où le coût est la somme pondérée 
    de la profondeur de chaque caractère dans l'arbre.

    Args:
        S (str): La chaîne de caractères à encoder.
    
    Returns:
        int: Le coût d'encodage minimum.
    """
    # Dictionnaire pour compter la fréquence de chaque caractère
    dict_string = {}
    # Dictionnaire pour stocker la profondeur de chaque caractère dans l'arbre de Huffman
    dict_depth = {}

    # Compte la fréquence de chaque caractère et initialise sa profondeur à 0
    for s in S:
        if s in dict_string:
            dict_string[s] += 1
        else:
            dict_string[s] = 1
            dict_depth[s] = 0

    # Copie du dictionnaire des fréquences pour l'algorithme de construction
    dict_string_calc = dict_string.copy()

    # Construction de l'arbre de Huffman simulée
    while len(dict_string_calc) != 1:
        x = None  # Premier caractère/minimum par fréquence
        y = None  # Deuxième caractère/minimum par fréquence

        # Recherche des deux caractères avec la plus petite fréquence
        for k, v in sorted(dict_string_calc.items(), key=lambda item: item[1]):
            if x is None:
                x = k
                x_cnt = v
                continue
            if y is None:
                y = k
                y_cnt = v
                break

        # Incrémente la profondeur de tous les caractères impliqués dans la concaténation
        for s in (x + y):
            if s in dict_depth:
                dict_depth[s] += 1
            else:
                # Un caractère inexistant ne devrait jamais être rencontré ici
                raise Exception("Caractère inattendu dans la fusion de Huffman.")

        # Retire les deux nœuds fusionnés et insère le nouveau nœud concaténé avec la somme de leurs fréquences
        del dict_string_calc[x]
        del dict_string_calc[y]
        dict_string_calc[x + y] = x_cnt + y_cnt

    # Calcule le coût total par somme pondérée des fréquences et profondeurs de chaque caractère
    ans = 0
    for k, v in dict_depth.items():
        ans += dict_string[k] * v

    # Cas limite : si une seule sorte de caractère dans la chaîne, 
    # chaque occurrence est encodée sur un bit
    if len(dict_string) == 1:
        ans = len(S)

    return ans


if __name__ == "__main__":
    # Entrée utilisateur pour la chaîne à encoder
    S = input()
    # Calcul du coût minimal d'encodage
    result = calculate_minimum_encoding(S)
    # Affichage du résultat
    print(result)