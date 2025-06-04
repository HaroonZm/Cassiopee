nombre_elements = int(input())
liste_entiers = [int(element) for element in input().split()]
somme_entiers = sum(liste_entiers)
if somme_entiers % 2 == 0:
    print(somme_entiers // 2)
else:
    premier_impair = 0
    liste_entiers.sort()
    for entier_courant in liste_entiers:
        if entier_courant % 2 == 1:
            premier_impair = entier_courant
            break
    print((somme_entiers - premier_impair) // 2)