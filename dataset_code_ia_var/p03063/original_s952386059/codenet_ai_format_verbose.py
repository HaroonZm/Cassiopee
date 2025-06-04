nombre_de_caracteres = int(input())
sequence_de_caracteres = input()

nombre_de_caracteres_blancs = 0
for indice_caractere in range(nombre_de_caracteres):
    if sequence_de_caracteres[indice_caractere] != '#':
        nombre_de_caracteres_blancs += 1

nombre_operations_minimum = nombre_de_caracteres_blancs
compteur_caracteres_blancs_restants = nombre_de_caracteres_blancs
compteur_caracteres_noirs = 0

for indice_caractere in range(nombre_de_caracteres):
    if sequence_de_caracteres[indice_caractere] == '.':
        compteur_caracteres_blancs_restants -= 1
    else:
        compteur_caracteres_noirs += 1

    nombre_operations = compteur_caracteres_noirs + compteur_caracteres_blancs_restants
    nombre_operations_minimum = min(nombre_operations_minimum, nombre_operations)

print(nombre_operations_minimum)