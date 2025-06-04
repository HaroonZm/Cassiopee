nombre_de_personnes = int(input())
direction_des_personnes = input()

compteur_est_a_gauche = [0] * nombre_de_personnes
compteur_ouest_a_droite = [0] * nombre_de_personnes

for indice_personne in range(nombre_de_personnes):

    if direction_des_personnes[indice_personne] == "E":
        compteur_est_a_gauche[indice_personne] += 1
    else:
        compteur_ouest_a_droite[indice_personne] += 1

for indice_personne in range(1, nombre_de_personnes):
    compteur_est_a_gauche[indice_personne] = (
        compteur_est_a_gauche[indice_personne - 1] + compteur_est_a_gauche[indice_personne]
    )

for indice_personne in range(nombre_de_personnes - 2, -1, -1):
    compteur_ouest_a_droite[indice_personne] = (
        compteur_ouest_a_droite[indice_personne + 1] + compteur_ouest_a_droite[indice_personne]
    )

total_personnes_a_changer = [
    compteur_est_a_gauche[indice] + compteur_ouest_a_droite[indice]
    for indice in range(nombre_de_personnes)
]

nombre_minimal_de_rotation = nombre_de_personnes - max(total_personnes_a_changer)

print(nombre_minimal_de_rotation)