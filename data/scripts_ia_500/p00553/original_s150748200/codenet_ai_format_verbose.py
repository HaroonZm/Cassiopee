nombre_elements = 5

entiers_saisis = [int(input()) for index_element in range(nombre_elements)]

premier_nombre = entiers_saisis[0]
deuxieme_nombre = entiers_saisis[1]
troisieme_nombre = entiers_saisis[2]
quatrieme_nombre = entiers_saisis[3]
cinquieme_nombre = entiers_saisis[4]

if premier_nombre > 0:
    
    resultat_multiplication = cinquieme_nombre * (deuxieme_nombre - premier_nombre)
    
    print(int(resultat_multiplication))
    
else:
    
    valeur_absolue_premier_nombre = abs(premier_nombre)
    
    calcul_intermediaire = valeur_absolue_premier_nombre * troisieme_nombre
    
    valeur_finale = calcul_intermediaire + quatrieme_nombre + (deuxieme_nombre * cinquieme_nombre)
    
    print(valeur_finale)