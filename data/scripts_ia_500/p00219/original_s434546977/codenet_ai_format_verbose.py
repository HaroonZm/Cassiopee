while True:
    
    nombre_entrees = int(input())
    
    if nombre_entrees == 0:
        break

    frequences_chiffres = [0 for index_chiffre in range(10)]
    
    for compteur_entree in range(nombre_entrees):
        chiffre_entree = int(input())
        frequences_chiffres[chiffre_entree] += 1

    for chiffre_courant in range(10):
        etoiles_pour_chiffre = '*' * frequences_chiffres[chiffre_courant]
        
        if len(etoiles_pour_chiffre) == 0:
            print("-")
        else:
            print(etoiles_pour_chiffre)