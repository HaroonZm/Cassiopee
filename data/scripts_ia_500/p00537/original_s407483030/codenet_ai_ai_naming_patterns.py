nombre_elements, nombre_operations = map(int, input().split())
difference_cumulatif = [0] * nombre_elements
valeurs_initiales = list(map(int, input().split()))
indice_precedent = valeurs_initiales[0] - 1

for valeur_courante in valeurs_initiales[1:]:
    valeur_courante -= 1
    difference_cumulatif[max(indice_precedent, valeur_courante)] -= 1
    difference_cumulatif[min(indice_precedent, valeur_courante)] += 1
    indice_precedent = valeur_courante

resultat_total = 0
for index in range(nombre_elements - 1):
    difference_cumulatif[index + 1] += difference_cumulatif[index]
    distance, cout_fixe, cout_variable = map(int, input().split())
    resultat_total += min(distance * difference_cumulatif[index], cout_fixe * difference_cumulatif[index] + cout_variable)

print(resultat_total)