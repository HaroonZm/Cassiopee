hauteur_totale, limite_inferieure, limite_superieure = map(int, input().split())

nombre_diviseurs = 0

for diviseur_courant in range(limite_inferieure, limite_superieure + 1):
    
    if hauteur_totale % diviseur_courant == 0:
        
        nombre_diviseurs += 1

print(nombre_diviseurs)