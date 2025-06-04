# Définition des plages de coordonnées pour les déplacements des deux types de pièces
deplacement_cavalier = range(-2, 3)
deplacement_adjacence = range(-1, 2)

# Génération des déplacements possibles pour le cavalier (dans un cercle d'une norme spécifique)
deplacements_possibles_cavalier = [
    (delta_x, delta_y)
    for delta_x in deplacement_cavalier
    for delta_y in deplacement_cavalier
    if 3 < delta_x ** 2 + delta_y ** 2 < 6
]

# Génération des déplacements possibles pour une case adjacente (orthogonal ou diagonal)
deplacements_possibles_adjacents = [
    (delta_x, delta_y)
    for delta_x in deplacement_adjacence
    for delta_y in deplacement_adjacence
]

def lire_entiers_deux_par_deux():
    return map(int, raw_input().split(" "))

def calculer_positions_accessibles(position_courante, indice_type_deplacement):
    position_x, position_y = position_courante
    
    if indice_type_deplacement > 0:
        deplacements_possibles = deplacements_possibles_adjacents
    else:
        deplacements_possibles = deplacements_possibles_cavalier
    
    ensemble_positions_valides = set(
        [
            (position_x + deplacement_x, position_y + deplacement_y)
            for deplacement_x, deplacement_y in deplacements_possibles
            if 0 <= position_x + deplacement_x < 10 and 0 <= position_y + deplacement_y < 10
        ]
    )
    
    return ensemble_positions_valides

while True:
    position_finale_x, position_finale_y = lire_entiers_deux_par_deux()
    if position_finale_x == 0 and position_finale_y == 0:
        break

    input()
    
    positions_entrees = lire_entiers_deux_par_deux()
    pions_a_deplacer = zip(positions_entrees[0::2], positions_entrees[1::2])
    positions_possibles_finales = set([(position_finale_x, position_finale_y)])
    
    for position_pion in pions_a_deplacer:
        positions_accessibles_pion = calculer_positions_accessibles(position_pion, 1)
        nouvel_ensemble_positions = set([])
        for position_finale_possible in positions_possibles_finales:
            nouvel_ensemble_positions |= (
                positions_accessibles_pion 
                & calculer_positions_accessibles(position_finale_possible, 0)
            )
        positions_possibles_finales = nouvel_ensemble_positions
    
    print ["NA", "OK"][len(positions_possibles_finales) > 0]