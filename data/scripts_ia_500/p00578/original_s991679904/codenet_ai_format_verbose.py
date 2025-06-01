from collections import defaultdict

nombre_elements = int(input())

liste_elements = list(map(int, input().split()))

if all(element == 0 for element in liste_elements):
    
    print(0)
    
    exit()

positions_par_valeur = defaultdict(list)

for index, valeur in enumerate(liste_elements):
    
    positions_par_valeur[valeur].append(index)

valeur_maximale_obtenue = 0

nombre_elements_utilises = 0

nombre_liens = 0

for valeur_courante in sorted(set(liste_elements), reverse=True):
    
    nombre_elements_utilises += len(positions_par_valeur[valeur_courante])
    
    for position_courante in positions_par_valeur[valeur_courante]:
        
        if position_courante > 0 and liste_elements[position_courante] < liste_elements[position_courante - 1]:
            
            nombre_liens += 1
        
        if position_courante < nombre_elements - 1 and liste_elements[position_courante] <= liste_elements[position_courante + 1]:
            
            nombre_liens += 1
    
    valeur_maximale_obtenue = max(valeur_maximale_obtenue, nombre_elements_utilises - nombre_liens)

print(valeur_maximale_obtenue)