nombre_total_noeuds, capacite_par_couche = map(int, input().split())

poids_courant_couche = 1
noeuds_restants = nombre_total_noeuds - 1
nombre_couches = 1

while True:

    noeuds_ajoutes = poids_courant_couche // capacite_par_couche + bool(poids_courant_couche % capacite_par_couche)

    if noeuds_ajoutes <= noeuds_restants:
        noeuds_restants -= noeuds_ajoutes
        poids_courant_couche += noeuds_ajoutes
        nombre_couches += 1
    else:
        break

print(nombre_couches)