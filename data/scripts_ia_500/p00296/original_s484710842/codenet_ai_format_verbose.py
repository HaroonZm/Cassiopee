nombre_elements = list(map(int, input().split()))[0]

liste_indices = [indice for indice in range(nombre_elements)]

deplacements = tuple(map(int, input().split()))

position_courante = 0

for deplacement in deplacements:

    if deplacement % 2 == 1:
        position_courante = (position_courante - deplacement) % len(liste_indices)
        liste_indices.pop(position_courante)
    else:
        position_courante = (position_courante + deplacement) % len(liste_indices)
        liste_indices.pop(position_courante)

requete_indices = tuple(map(int, input().split()))

for requete in requete_indices:
    print(1 if requete in liste_indices else 0)