nombre_a_calculer = int(input())

valeurs_fibonacci_memoisation = [-1] * (nombre_a_calculer + 1)

valeurs_fibonacci_memoisation[0] = 1
valeurs_fibonacci_memoisation[1] = 1

for indice_calcul_courant in range(2, nombre_a_calculer + 1):

    valeur_precedente = valeurs_fibonacci_memoisation[indice_calcul_courant - 1]
    valeur_avant_precedente = valeurs_fibonacci_memoisation[indice_calcul_courant - 2]

    valeurs_fibonacci_memoisation[indice_calcul_courant] = valeur_precedente + valeur_avant_precedente

print(valeurs_fibonacci_memoisation[nombre_a_calculer])