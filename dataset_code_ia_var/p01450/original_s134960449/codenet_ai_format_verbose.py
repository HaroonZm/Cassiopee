nombre_objets, capacite_maximale = map(int, input().split())

poids_objets = []

for indice_objet in range(nombre_objets):
    poids_objets.append(int(input()))

poids_objets.sort()

somme_poids_traitee = 0
nombre_solutions = 0

for indice_poids_actuel, poids_actuel in enumerate(poids_objets):
    
    if indice_poids_actuel == nombre_objets - 1:
        somme_poids_sauf_dernier = sum(poids_objets) - poids_objets[-1]
        poids_dernier = poids_objets[-1]
        if somme_poids_sauf_dernier <= capacite_maximale and capacite_maximale - somme_poids_sauf_dernier < poids_dernier:
            nombre_solutions += 1
        break
    
    taille_table = nombre_objets - indice_poids_actuel
    table_dynamiques = [[0] * (capacite_maximale + 1) for _ in range(taille_table)]
    table_dynamiques[0][0] = 1
    
    for sous_ensemble_index in range(taille_table - 1):
        dp_suivant = table_dynamiques[sous_ensemble_index + 1]
        dp_actuel = table_dynamiques[sous_ensemble_index]
        
        for capacite_courante in range(capacite_maximale + 1):
            poids_suivant = poids_objets[indice_poids_actuel + sous_ensemble_index + 1]
            if capacite_courante - poids_suivant >= 0:
                dp_suivant[capacite_courante] = dp_actuel[capacite_courante] + dp_actuel[capacite_courante - poids_suivant]
            else:
                dp_suivant[capacite_courante] = dp_actuel[capacite_courante]
    
    borne_inferieure = max(capacite_maximale - somme_poids_traitee - poids_actuel + 1, 0)
    borne_superieure = capacite_maximale - somme_poids_traitee
    
    for valeur_capacite in range(borne_inferieure, borne_superieure + 1):
        nombre_solutions += table_dynamiques[-1][valeur_capacite]
        nombre_solutions %= 10 ** 9 + 7
    
    somme_poids_traitee += poids_actuel
    
    if capacite_maximale < somme_poids_traitee:
        break

print(nombre_solutions % (10 ** 9 + 7))