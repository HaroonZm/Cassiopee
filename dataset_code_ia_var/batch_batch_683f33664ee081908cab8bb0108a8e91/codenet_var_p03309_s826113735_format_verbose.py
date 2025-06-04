nombre_elements = int(input())

elements_lus = list(map(int, input().split()))

elements_ajustes = [
    elements_lus[index - 1] - index
    for index in range(1, nombre_elements + 1)
]

elements_ajustes.sort()

if nombre_elements % 2 == 1:
    valeur_mediane = elements_ajustes[(nombre_elements - 1) // 2]
else:
    valeur_gauche = elements_ajustes[nombre_elements // 2 - 1]
    valeur_droite = elements_ajustes[nombre_elements // 2]
    valeur_mediane = round(valeur_gauche + valeur_droite) // 2

somme_ecarts = sum(
    abs(elements_ajustes[index] - valeur_mediane)
    for index in range(nombre_elements)
)

print(somme_ecarts)