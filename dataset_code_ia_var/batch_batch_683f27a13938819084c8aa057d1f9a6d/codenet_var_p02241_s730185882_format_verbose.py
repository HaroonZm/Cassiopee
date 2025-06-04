nombre_de_sommets = int(input())

matrice_d_adjacence = [
    list(map(int, input().split()))
    for _ in range(nombre_de_sommets)
]

liste_des_aretes_ponderees = []

for indice_ligne in range(nombre_de_sommets):
    for indice_colonne in range(indice_ligne, nombre_de_sommets):
        poids_arete = matrice_d_adjacence[indice_ligne][indice_colonne]
        if poids_arete >= 0:
            liste_des_aretes_ponderees.append(
                (indice_ligne, indice_colonne, poids_arete)
            )

liste_des_aretes_ponderees.sort(key=lambda arete: arete[2])

ponderation_totale_arbre_couvrant = 0

parent_de_sommet = [
    indice_sommet
    for indice_sommet in range(nombre_de_sommets)
]

def trouver_racine(sommet):
    chemin_vers_racine = []
    while parent_de_sommet[sommet] != sommet:
        chemin_vers_racine.append(sommet)
        sommet = parent_de_sommet[sommet]
    for sommet_parcouru in chemin_vers_racine:
        parent_de_sommet[sommet_parcouru] = sommet
    return sommet

def appartiennent_au_meme_ensemble(sommet_1, sommet_2):
    return trouver_racine(sommet_1) == trouver_racine(sommet_2)

def fusionner_ensembles(sommet_1, sommet_2):
    parent_de_sommet[trouver_racine(sommet_1)] = trouver_racine(sommet_2)

for depart, arrivee, poids in liste_des_aretes_ponderees:
    if not appartiennent_au_meme_ensemble(depart, arrivee):
        fusionner_ensembles(depart, arrivee)
        ponderation_totale_arbre_couvrant += poids

print(ponderation_totale_arbre_couvrant)