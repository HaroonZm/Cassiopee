nombre_elements = int(input())
liste_entiers = list(map(int, input().split()))

liste_entiers.sort()

somme_totale = sum(liste_entiers)

if somme_totale % 2 == 0:
    print(somme_totale // 2)
else:
    premier_impair = None
    for indice_element in range(nombre_elements):
        if liste_entiers[indice_element] % 2 == 1:
            premier_impair = liste_entiers[indice_element]
            break
    print((somme_totale - premier_impair) // 2)