nombre_iterations = int(input())
for iteration_index in range(nombre_iterations):
    resultat_total = 0
    capacite_1, capacite_2, capacite_3 = map(int, input().split())
    utilisation_initiale = min(capacite_3, capacite_2, capacite_1)
    resultat_total = utilisation_initiale
    capacite_1 -= utilisation_initiale
    capacite_2 -= utilisation_initiale

    if capacite_1 >= 2 and capacite_2 >= 1:
        utilisation_combo = min(capacite_1 // 2, capacite_2)
        capacite_1 -= utilisation_combo * 2
        resultat_total += utilisation_combo

    if capacite_1 >= 3:
        utilisation_reste = capacite_1 // 3
        resultat_total += utilisation_reste

    print(resultat_total)