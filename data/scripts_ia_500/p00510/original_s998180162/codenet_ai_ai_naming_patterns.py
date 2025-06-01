nombre_iterations = int(input())

nombre_voitures_courant = nombre_voitures_maximum = int(input())

for indice_iteration in range(nombre_iterations):
    nombre_entrees_voitures, nombre_sorties_voitures = map(int, input().split())
    
    nombre_voitures_courant += nombre_entrees_voitures - nombre_sorties_voitures
    
    if nombre_voitures_courant < 0:
        nombre_voitures_maximum = 0
        break
    else:
        nombre_voitures_maximum = max(nombre_voitures_maximum, nombre_voitures_courant)

print(nombre_voitures_maximum)