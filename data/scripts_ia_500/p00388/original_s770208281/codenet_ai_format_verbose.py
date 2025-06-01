heure_actuelle, borne_inferieure, borne_superieure = map(int, input().split())

nombre_de_diviseurs_exacts = 0

for nombre_courant in range(borne_inferieure, borne_superieure + 1):
    
    if heure_actuelle % nombre_courant == 0:
        
        nombre_de_diviseurs_exacts += 1

print(nombre_de_diviseurs_exacts)