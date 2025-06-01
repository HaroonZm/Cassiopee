nombre_lignes, nombre_colonnes, nombre_cartes = map(int, input().split())

nombre_cartes_restantes = nombre_cartes - (nombre_lignes * nombre_colonnes)

if nombre_cartes_restantes < 0:
    
    print(0)

else:
    
    from math import factorial as fact
    
    nombre_de_combinations = fact(nombre_lignes + nombre_cartes_restantes - 1) // (fact(nombre_cartes_restantes) * fact(nombre_lignes - 1))
    
    print(nombre_de_combinations)