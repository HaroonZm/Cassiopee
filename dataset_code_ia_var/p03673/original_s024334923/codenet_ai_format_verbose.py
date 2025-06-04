nombre_elements = int(input())

liste_entiers = list(map(int, input().split()))

elements_indices_pairs = []
elements_indices_impairs = []

for indice_element in range(nombre_elements):
    
    if indice_element % 2 == 0:
        elements_indices_pairs.append(liste_entiers[indice_element])
    else:
        elements_indices_impairs.append(liste_entiers[indice_element])

if nombre_elements % 2 == 0:
    liste_resultat = elements_indices_impairs[::-1] + elements_indices_pairs
else:
    liste_resultat = elements_indices_pairs[::-1] + elements_indices_impairs

print(*liste_resultat)