nombre_elements = int(input())
ligne_elements = input().split(" ")
liste_entiers = [int(ligne_elements[index]) for index in range(nombre_elements)]

valeur_maximale = 0
compteur_succession = 0
for index_element in range(nombre_elements):
    if liste_entiers[index_element] == 1:
        compteur_succession += 1
        if valeur_maximale < compteur_succession:
            valeur_maximale = compteur_succession
    else:
        compteur_succession = 0
print(valeur_maximale + 1)