import sys

# Préparation de la lecture rapide depuis l'entrée standard
lecture_entree_binaire = sys.stdin.buffer.read
lecture_ligne_binaire = sys.stdin.buffer.readline
lecture_lignes_binaire = sys.stdin.buffer.readlines

# Augmentation de la limite de récursion pour traiter de grands cas de test
sys.setrecursionlimit(10 ** 7)

# Lecture et extraction des données d'entrée
nombre_de_mansions, position_initiale, *positions_et_poids_liste = map(int, lecture_entree_binaire().split())

liste_positions_mansions = positions_et_poids_liste[::2]
liste_poids_mansions = positions_et_poids_liste[1::2]

# Détermination du nombre de mansions à gauche et à droite du point de départ
nombre_mansions_gauche = sum(position < position_initiale for position in liste_positions_mansions)

positions_mansions_gauche = liste_positions_mansions[nombre_mansions_gauche-1::-1]  # Ordre du plus proche au plus éloigné côté gauche
poids_mansions_gauche = liste_poids_mansions[nombre_mansions_gauche-1::-1]          # As above for weights

nombre_mansions_droite = nombre_de_mansions - nombre_mansions_gauche

positions_mansions_droite = liste_positions_mansions[nombre_mansions_gauche:]
poids_mansions_droite = liste_poids_mansions[nombre_mansions_gauche:]

sequence_visite_mansions = []  # Ordre de visite final, construit en partant de l'extérieur vers l'intérieur

# Tri des mansions à visiter en fonction du poids minimal côté gauche/droite
while nombre_mansions_gauche and nombre_mansions_droite:

    poids_gauche = poids_mansions_gauche[-1]
    position_gauche = positions_mansions_gauche[-1]
    
    poids_droite = poids_mansions_droite[-1]
    position_droite = positions_mansions_droite[-1]
    
    if poids_gauche < poids_droite:
        sequence_visite_mansions.append(position_gauche)
        poids_mansions_gauche.pop()
        positions_mansions_gauche.pop()
        nombre_mansions_gauche -= 1
        poids_mansions_droite[-1] = poids_gauche + poids_droite
    else:
        sequence_visite_mansions.append(position_droite)
        poids_mansions_droite.pop()
        positions_mansions_droite.pop()
        nombre_mansions_droite -= 1
        poids_mansions_gauche[-1] = poids_gauche + poids_droite

# Ajout des mansions restants du côté non vide dans l’ordre du plus proche
if nombre_mansions_gauche:
    sequence_visite_mansions += positions_mansions_gauche[::-1]
else:
    sequence_visite_mansions += positions_mansions_droite[::-1]

# Terminaison du parcours par la position initiale
sequence_visite_mansions.append(position_initiale)

# Calcul du coût total du trajet effectué
distance_totale_parcours = sum(
    abs(position_courante - position_suivante)
    for position_courante, position_suivante in zip(sequence_visite_mansions, sequence_visite_mansions[1:])
)

print(distance_totale_parcours)