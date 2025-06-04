nombre_entrees = int(input())

liste_nombres = list(map(int, input().split()))

liste_nombres.sort()

pair_trouvee = False

for indice_premier_nombre in range(nombre_entrees):
    
    if pair_trouvee:
        break

    for decalage in range(1, nombre_entrees - indice_premier_nombre):
        
        if pair_trouvee:
            break

        difference = liste_nombres[indice_premier_nombre + decalage] - liste_nombres[indice_premier_nombre]
        
        if difference % (nombre_entrees - 1) == 0:
            
            print(liste_nombres[indice_premier_nombre], liste_nombres[indice_premier_nombre + decalage])
            pair_trouvee = True