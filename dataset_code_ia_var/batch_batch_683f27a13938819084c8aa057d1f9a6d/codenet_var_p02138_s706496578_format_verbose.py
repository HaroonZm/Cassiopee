nombre_joueurs_niveau_un, nombre_joueurs_niveau_deux = map(int, input().split())

points_niveau_un_restants = nombre_joueurs_niveau_un * 2
points_niveau_deux_restants = nombre_joueurs_niveau_deux * 2
nombre_tours_possibilite_une = 0

while True:
    points_utilisables_niveau_un = min(nombre_joueurs_niveau_un, points_niveau_un_restants)
    points_niveau_deux_restants -= points_utilisables_niveau_un

    if points_niveau_deux_restants <= 0:
        break

    nombre_tours_possibilite_une += 1

    points_utilisables_niveau_deux = (points_niveau_deux_restants + 1) // 2
    points_niveau_un_restants -= points_utilisables_niveau_deux

    if points_niveau_un_restants <= 0:
        break

    nombre_tours_possibilite_une += 1

points_niveau_un_restants = nombre_joueurs_niveau_un * 2
points_niveau_deux_restants = nombre_joueurs_niveau_deux * 2
nombre_tours_possibilite_deux = 0

while True:
    points_utilisables_niveau_un = (points_niveau_un_restants + 1) // 2
    points_niveau_deux_restants -= points_utilisables_niveau_un

    if points_niveau_deux_restants <= 0:
        break

    nombre_tours_possibilite_deux += 1

    points_utilisables_niveau_deux = min(nombre_joueurs_niveau_deux, points_niveau_deux_restants)
    points_niveau_un_restants -= points_utilisables_niveau_deux

    if points_niveau_un_restants <= 0:
        break

    nombre_tours_possibilite_deux += 1

print(min(nombre_tours_possibilite_une, nombre_tours_possibilite_deux))