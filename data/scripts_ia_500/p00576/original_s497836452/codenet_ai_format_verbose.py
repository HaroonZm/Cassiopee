nombre_elements = int(input())

valeurs_liste = list(map(int, input().split()))

nombre_indices = int(input())

indices_a_modifier = list(map(int, input().split()))

indices_zero_based = [indice - 1 for indice in indices_a_modifier]

for indice in indices_zero_based:
    
    valeur_courante = valeurs_liste[indice]
    
    if (valeur_courante + 1) not in valeurs_liste and valeur_courante != 2019:
        
        valeurs_liste[indice] += 1

print("\n".join(map(str, valeurs_liste)))