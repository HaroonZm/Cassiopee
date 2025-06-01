liste_nombres_premiers = []

for nombre in range(10000):
    
    diviseur = 3
    
    compteur_diviseurs = 0
    
    if nombre % 2 == 0:
        compteur_diviseurs += 1
    else:
        while diviseur < int(nombre ** 0.5) + 1:
            if nombre % diviseur != 0:
                diviseur += 2
            else:
                compteur_diviseurs += 1
                break
    
    if compteur_diviseurs == 0:
        liste_nombres_premiers.append(nombre)

liste_nombres_premiers.reverse()

while True:
    
    index_premier_proche = 0

    nombre_input = int(input())
    
    if nombre_input == 0:
        break
    else:
        for indice in range(len(liste_nombres_premiers)):
            if nombre_input >= liste_nombres_premiers[indice]:
                index_premier_proche = indice
                break
        
        while True:
            if liste_nombres_premiers[index_premier_proche] - 2 == liste_nombres_premiers[index_premier_proche + 1]:
                print(liste_nombres_premiers[index_premier_proche + 1], liste_nombres_premiers[index_premier_proche])
                break
            else:
                index_premier_proche += 1