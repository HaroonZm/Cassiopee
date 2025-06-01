nombre_de_joueurs = int(input())

resultats_des_jeux_par_joueur = [
    [int(score) for score in input().split()] 
    for _ in range(nombre_de_joueurs)
]

points_par_joueur = [0] * nombre_de_joueurs

for index_du_jeu in range(3):

    scores_courants = [
        resultat[index_du_jeu] 
        for resultat in resultats_des_jeux_par_joueur
    ]

    occurrence_scores = {}

    for score in scores_courants:
        if score not in occurrence_scores:
            occurrence_scores[score] = 1
        else:
            occurrence_scores[score] += 1

    for index_du_joueur in range(nombre_de_joueurs):
        score_du_joueur = scores_courants[index_du_joueur]

        if occurrence_scores[score_du_joueur] == 1:
            points_par_joueur[index_du_joueur] += score_du_joueur

for points_totaux in points_par_joueur:
    print(points_totaux)