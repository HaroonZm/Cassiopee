while True:
    
    nombre_de_valeurs = int(input())
    
    if nombre_de_valeurs == 0:
        break

    compteurs_frequences = [0 for _ in range(10)]

    for _ in range(nombre_de_valeurs):
        valeur = int(input())
        compteurs_frequences[valeur] += 1

    for chiffre in range(10):
        if compteurs_frequences[chiffre] == 0:
            print("-")
        else:
            print("*" * compteurs_frequences[chiffre])