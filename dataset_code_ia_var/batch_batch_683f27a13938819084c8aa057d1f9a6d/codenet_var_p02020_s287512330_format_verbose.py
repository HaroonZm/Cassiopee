nombre_entiers = int(input())

liste_entiers = [int(valeur) for valeur in input().split()]

liste_entiers.sort()

somme_totale = sum(liste_entiers)

for entier in liste_entiers:
    if somme_totale % 2 == 0 or entier % 2 == 0:
        continue
    somme_totale -= entier

somme_moitie = somme_totale // 2

print(somme_moitie)