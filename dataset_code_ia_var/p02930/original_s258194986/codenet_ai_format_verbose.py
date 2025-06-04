obtenir_entree_utilisateur = raw_input

nombre_total_sommets = int(obtenir_entree_utilisateur())

distance_niveaux_graphe = [[0 for indice_colonne in range(501)] for indice_ligne in range(501)]

distance_maximale_partition = [0 for indice_partition in range(501)]
distance_maximale_partition[2] = 1
distance_maximale_partition[3] = 2

liste_graphes = [None for indice_graphe in range(501)]

graphe_base_deux = [[None, None, None], [None, None, 1], [None, 1, None]]
liste_graphes[2] = graphe_base_deux

graphe_base_trois = [[None for indice_colonne in range(3+1)] for indice_ligne in range(3+1)]
graphe_base_trois[1][2] = 2
graphe_base_trois[1][3] = 1
graphe_base_trois[2][1] = 2
graphe_base_trois[2][3] = 1
graphe_base_trois[3][1] = 1
graphe_base_trois[3][2] = 1
liste_graphes[3] = graphe_base_trois

def transferer_distances_sous_graphe(nouveau_graphe, noeuds_a_mapper):
    nombre_noeuds_a_mapper = len(noeuds_a_mapper)
    ancien_graphe = liste_graphes[nombre_noeuds_a_mapper]
    anciens_indices_noeuds = list(range(1, nombre_noeuds_a_mapper + 1))
    nouveaux_indices_noeuds = noeuds_a_mapper

    for indice_noeud_premier, nouvel_noeud_1 in enumerate(nouveaux_indices_noeuds):
        ancien_noeud_1 = indice_noeud_premier + 1
        for decalage, nouvel_noeud_2 in enumerate(nouveaux_indices_noeuds[indice_noeud_premier + 1:]):
            indice_noeud_deuxieme = indice_noeud_premier + decalage + 1
            ancien_noeud_2 = indice_noeud_deuxieme + 1
            nouveau_graphe[nouvel_noeud_1][nouvel_noeud_2] = ancien_graphe[ancien_noeud_1][ancien_noeud_2] + 1

    return nouveau_graphe

for nombre_sommets_actuel in range(4, nombre_total_sommets + 1):

    taille_premiere_partition = nombre_sommets_actuel // 2
    taille_seconde_partition = taille_premiere_partition

    if nombre_sommets_actuel % 2 == 1:
        taille_premiere_partition += 1

    liste_noeuds_partition_1 = [indice for indice in range(1, taille_premiere_partition + 1)]
    liste_noeuds_partition_2 = [indice for indice in range(taille_premiere_partition + 1, nombre_sommets_actuel + 1)]

    graphe_courant = [[None for indice_colonne in range(nombre_sommets_actuel + 1)] for indice_ligne in range(nombre_sommets_actuel + 1)]

    for noeud_1 in liste_noeuds_partition_1:
        for noeud_2 in liste_noeuds_partition_2:
            graphe_courant[noeud_1][noeud_2] = 1
            graphe_courant[noeud_2][noeud_1] = 1

    distance_maximale_partition[nombre_sommets_actuel] = 1 + max(
        distance_maximale_partition[taille_premiere_partition],
        distance_maximale_partition[taille_seconde_partition]
    )

    graphe_courant = transferer_distances_sous_graphe(graphe_courant, liste_noeuds_partition_1)
    graphe_courant = transferer_distances_sous_graphe(graphe_courant, liste_noeuds_partition_2)

    liste_graphes[nombre_sommets_actuel] = graphe_courant

graphe_final = liste_graphes[nombre_total_sommets]

for indice_ligne in range(1, nombre_total_sommets + 1):
    ligne_a_afficher = " ".join([
        str(graphe_final[indice_ligne][indice_colonne]) 
        for indice_colonne in range(indice_ligne + 1, nombre_total_sommets + 1)
    ])
    print(ligne_a_afficher)