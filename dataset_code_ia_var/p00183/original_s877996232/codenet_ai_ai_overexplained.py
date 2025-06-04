# Boucle infinie: le code restera dans cette boucle tant qu'on ne la quitte pas explicitement (par 'break')
while True:
    # Utilisation de raw_input() pour lire une ligne saisie par l'utilisateur sous forme de chaîne de caractères
    # Attribuer cette chaîne à la variable 's'
    s = raw_input()
    
    # Vérification si l'utilisateur a saisi '0' (zéro sous forme de chaîne de caractères)
    # Si c'est le cas, quitter la boucle (grâce au mot-clé 'break')
    if s == "0":
        break
    
    # concaténer à la suite de 's' deux nouvelles chaînes saisies par l'utilisateur
    # La compréhension de liste [raw_input() for i in range(2)] produit une liste de deux entrées utilisateurs
    # "".join(...) assemble ces deux chaînes (listées) en une chaîne unique, sans séparateur.
    s += "".join([raw_input() for i in range(2)])
    
    # Création d'une liste 'L' de tuples, chaque tuple contenant 3 indices d'une grille 3x3 plat, de 0 à 8
    # Les tuples représentent les indices des lignes, des colonnes et des deux diagonales :
    # (i, i+1, i+2) pour les lignes (0-1-2, 3-4-5, 6-7-8)
    # (i, i+3, i+6) pour les colonnes (0-3-6, 1-4-7, 2-5-8)
    # (0,4,8) et (2,4,6) pour les deux diagonales
    L = [
        (i, i + 1, i + 2) for i in range(0, 9, 3)  # lignes
    ] + [
        (i, i + 3, i + 6) for i in range(3)        # colonnes
    ] + [
        (0, 4, 8),                                 # diagonale descendante gauche->droite
        (2, 4, 6)                                  # diagonale descendante droite->gauche
    ]
    
    # Parcourir chaque tuple de trois indices (i, j, k) dans la liste 'L'
    for i, j, k in L:
        # Test : est-ce que les trois cases de la grille référencées contiennent EXACTEMENT LA MÊME VALEUR
        # ET cette valeur est différente de "+" ?
        # Cette syntaxe équivaut à (s[i] == s[j]) and (s[j] == s[k]) and (s[i] != "+")
        if s[i] == s[j] == s[k] != "+":
            # Si la condition précédente est vraie, alors on a une ligne (ou colonne, ou diagonale) gagnante
            # Affichage du résultat selon que le symbole gagnant est "b" ou "w"
            # Si s[i] vaut "b", alors afficher "b"
            # Sinon (c'est-à-dire s[i] vaut "w"), afficher "w"
            print "b" if s[i] == "b" else "w"
            # Sortir de la boucle for, donc ignorer les autres lignes à tester
            break
    else:
        # Cette clause 'else' associée à la boucle 'for' ne s'exécute que si le 'break' n'a PAS été déclenché
        # Donc aucun gagnant trouvé, il faut afficher "NA" (Non Applicable ou Aucun)
        print "NA"