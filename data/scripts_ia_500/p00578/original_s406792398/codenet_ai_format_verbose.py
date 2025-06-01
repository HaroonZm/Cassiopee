nombre_elements = int(input())

valeurs_avec_indices = [int(valeur) for valeur in input().split()]

for indice in range(nombre_elements):
    
    valeurs_avec_indices[indice] = (valeurs_avec_indices[indice], indice)

presence_elements = [0] * nombre_elements

compteur_groupes = 0

valeur_maximale = 0

valeurs_avec_indices.sort(reverse=True)

for position in range(nombre_elements):
    
    compteur_groupes += 1
    
    presence_elements[valeurs_avec_indices[position][1]] = 1
    
    if valeurs_avec_indices[position][1] > 0 and presence_elements[valeurs_avec_indices[position][1] - 1] == 1:
        compteur_groupes -= 1
    
    if valeurs_avec_indices[position][1] < nombre_elements - 1 and presence_elements[valeurs_avec_indices[position][1] + 1] == 1:
        compteur_groupes -= 1
    
    if position < nombre_elements - 1 and valeurs_avec_indices[position][0] == valeurs_avec_indices[position + 1][0]:
        continue
    
    if valeurs_avec_indices[position][0] == 0:
        break
    
    valeur_maximale = max(valeur_maximale, compteur_groupes)

print(valeur_maximale)