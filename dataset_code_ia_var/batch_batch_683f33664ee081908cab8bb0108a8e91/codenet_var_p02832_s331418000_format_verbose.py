nombre_d_elements = int(input())

liste_entiers = list(map(int, input().split()))

prochain_element_attendu = 1

compteur_elements_ordonnes = 0

if 1 in liste_entiers:
    
    for element_courant in liste_entiers:
        
        if element_courant == prochain_element_attendu:
            
            compteur_elements_ordonnes += 1
            
            prochain_element_attendu += 1
    
    print(nombre_d_elements - compteur_elements_ordonnes)

else:
    
    print(-1)