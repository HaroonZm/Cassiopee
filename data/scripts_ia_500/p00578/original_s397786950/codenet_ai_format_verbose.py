def main():
    
    nombre_elements = int(input())
    
    liste_entiers = list(map(int, input().split()))
    
    liste_entiers.append(-1)
    
    liste_filtrees = [element_courant for element_courant, element_suivant in zip(liste_entiers, liste_entiers[1:]) if element_courant != element_suivant]
    
    liste_filtrees.insert(0, -1)
    liste_filtrees.append(-1)
    
    liste_alternances = [element_milieu for element_precedent, element_milieu, element_suivant in zip(liste_filtrees, liste_filtrees[1:], liste_filtrees[2:]) if (element_precedent < element_milieu) != (element_milieu < element_suivant)]
    
    liste_alternances.append(-1)
    
    liste_paires_avec_signe = sorted(
        (element_courant, (1 if element_courant < element_suivant else -1))
        for element_courant, element_suivant in zip(liste_alternances, liste_alternances[1:])
    )
    
    longueur_courante = 1
    longueur_maximale = 0
    valeur_precedente = 0
    
    for valeur_courante, signe in liste_paires_avec_signe:
        
        if valeur_precedente < valeur_courante:
            
            if longueur_maximale < longueur_courante:
                longueur_maximale = longueur_courante
                
            valeur_precedente = valeur_courante
        
        longueur_courante += signe
    
    print(longueur_maximale)
    

main()