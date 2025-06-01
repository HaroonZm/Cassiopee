nombre_elements_liste_X = int(input())

valeurs_liste_X = list(map(int, input().split()))

nombre_elements_liste_A = int(input())

indices_liste_A = list(map(int, input().split()))

for index in indices_liste_A:

    valeur_courante = valeurs_liste_X[index - 1]

    if (valeur_courante + 1) in valeurs_liste_X or valeur_courante == 2019:

        continue

    else:

        valeurs_liste_X[index - 1] = valeur_courante + 1

for position in range(nombre_elements_liste_X):

    print(valeurs_liste_X[position])