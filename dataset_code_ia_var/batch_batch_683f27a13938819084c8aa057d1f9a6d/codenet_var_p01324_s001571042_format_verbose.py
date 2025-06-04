valeur_defaut = 999999999

def parser_ligne_equation(ligne_entree):
    (
        coefficient_str, 
        nom_gauche, 
        signe_egal, 
        facteur_scale, 
        nom_droite
    ) = ligne_entree.split()
    
    exposant_entier = int(facteur_scale.split("^")[-1])
    return nom_gauche, exposant_entier, nom_droite

while True:
    nombre_equations = int(raw_input())
    
    if nombre_equations == 0:
        break
    
    liste_equations = []
    liste_noms_variables = []
    
    for index_equation in range(nombre_equations):
        nom_gauche, exposant, nom_droite = parser_ligne_equation(raw_input())
        liste_noms_variables += [nom_gauche, nom_droite]
        liste_equations.append([nom_gauche, nom_droite, exposant])
    
    liste_variable_uniques = sorted(set(liste_noms_variables))
    nombre_variables = len(liste_variable_uniques)
    
    matrice_exposants = [
        [
            0 if indice_ligne == indice_colonne else valeur_defaut
            for indice_colonne in range(nombre_variables)
        ]
        for indice_ligne in range(nombre_variables)
    ]
    
    reponse = "Yes"
    
    for equation in liste_equations:
        indice_gauche, indice_droite = [
            liste_variable_uniques.index(variable)
            for variable in equation[:2]
        ]
        exposant_rel = equation[2]
        
        if matrice_exposants[indice_gauche][indice_droite] == valeur_defaut:
            # Ajout nouvelle relation
            matrice_exposants[indice_gauche][indice_droite] = exposant_rel
            matrice_exposants[indice_droite][indice_gauche] = -exposant_rel
            
            # Propagation des relations existantes
            for couple_indices in [[indice_gauche, indice_droite], [indice_droite, indice_gauche]]:
                indice_a, indice_b = couple_indices
                for indice_depart in range(nombre_variables):
                    for indice_arrivee in range(nombre_variables):
                        if (
                            matrice_exposants[indice_depart][indice_a] != valeur_defaut
                            and matrice_exposants[indice_b][indice_arrivee] != valeur_defaut
                        ):
                            nouvelle_valeur = (
                                matrice_exposants[indice_depart][indice_a]
                                + matrice_exposants[indice_a][indice_b]
                                + matrice_exposants[indice_b][indice_arrivee]
                            )
                            matrice_exposants[indice_depart][indice_arrivee] = nouvelle_valeur
                            matrice_exposants[indice_arrivee][indice_depart] = -nouvelle_valeur
        else:
            if matrice_exposants[indice_gauche][indice_droite] != exposant_rel:
                reponse = "No"
                break
    
    print reponse