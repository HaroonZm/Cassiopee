nombre_elements, decalage = map(int, input().split())

liste_entiers = list(map(int, input().split()))

for indice_depart in range(1, nombre_elements - decalage + 1):

    element_futur = liste_entiers[indice_depart + decalage - 1]
    
    element_precedent = liste_entiers[indice_depart - 1]
    
    if element_futur > element_precedent:
    
        print("Yes")
        
    else:
    
        print("No")