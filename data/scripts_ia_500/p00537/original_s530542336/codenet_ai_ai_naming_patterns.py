nombre_de_noeuds, nombre_de_deplacements = map(int, input().split())
positions = list(map(int, input().split()))
compteur_de_deplacement = [0] * nombre_de_noeuds
tarifs = []

for _ in range(nombre_de_noeuds - 1):
    tarifs.append(list(map(int, input().split())))

for index_deplacement in range(nombre_de_deplacements - 1):
    position_courante = positions[index_deplacement]
    position_suivante = positions[index_deplacement + 1]
    compteur_de_deplacement[min(position_suivante - 1, position_courante - 1)] += 1
    compteur_de_deplacement[max(position_suivante - 1, position_courante - 1)] -= 1

for index_noeud in range(nombre_de_noeuds - 1):
    compteur_de_deplacement[index_noeud + 1] += compteur_de_deplacement[index_noeud]

resultat_total = 0
for index_tarif in range(nombre_de_noeuds - 1):
    nombre_utilisations = compteur_de_deplacement[index_tarif]
    tarif_papier, tarif_ic, cout_achat_prealable = tarifs[index_tarif]
    resultat_total += min(tarif_papier * nombre_utilisations, tarif_ic * nombre_utilisations + cout_achat_prealable)

print(resultat_total)