longueur_totale = int(input())
distance_parcourue_premier_individu = int(input())
distance_parcourue_deuxieme_individu = int(input())
vitesse_premier_individu = int(input())
vitesse_deuxieme_individu = int(input())

temps_premier_individu = distance_parcourue_premier_individu // vitesse_premier_individu
temps_deuxieme_individu = distance_parcourue_deuxieme_individu // vitesse_deuxieme_individu

if temps_premier_individu >= temps_deuxieme_individu:
    
    if distance_parcourue_premier_individu % vitesse_premier_individu == 0:
        
        print(longueur_totale - temps_premier_individu)
        
    else:
        
        print(longueur_totale - temps_premier_individu - 1)
        
else:
    
    if distance_parcourue_deuxieme_individu % vitesse_deuxieme_individu == 0:
        
        print(longueur_totale - temps_deuxieme_individu)
        
    else:
        
        print(longueur_totale - temps_deuxieme_individu - 1)