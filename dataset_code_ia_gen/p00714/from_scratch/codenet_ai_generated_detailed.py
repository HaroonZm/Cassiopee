import sys

# Constantes du problème
TANK_WIDTH = 100    # largeur en cm
TANK_HEIGHT = 50    # hauteur en cm
TANK_DEPTH = 30     # profondeur en cm (perp. aux planches)

def simulate_water_level(N, boards, M, faucets, L, observations):
    """
    Simule le niveau d'eau dans la cuve au fil du temps selon
    l'écoulement d'eau par les robinets et les compartiments
    formés par les planches.

    boards : list of (position, height)
    faucets : list of (position, débit)
    observations : list of (position, temps)
    """

    # Étape 1 : Déterminer les zones compartimentées par les planches et les positions limites
    # Le tank va être découpé en zones entre les planches (et jusqu'aux bords 0 et 100)
    # On construit une liste triée des positions avec 0, positions des planches et 100.
    positions = [0]
    for b, _ in boards:
        positions.append(b)
    positions.append(TANK_WIDTH)
    positions.sort()

    # Étape 2 : Définir la hauteur maximale de chaque zone
    # Chaque zone i est entre positions[i] et positions[i+1].
    # La hauteur maximale est le minimum des hauteurs des panneaux limitant la zone.
    #
    # Pour zones extrêmes:
    # - Au bord gauche, pas de planche à gauche, donc pas de limitation à gauche, hauteur max = TANK_HEIGHT
    # - Pareil au bord droit.
    #
    # Pour zones intérieures, la hauteur max est le minimum des hauteurs des planches de gauche et droite
    # Ex: zone entre B_i et B_{i+1} limité par hauteur des 2 planches.

    # construire un dict hauteur_bords : position -> hauteur planche
    hauteur_bords = {pos: 0 for pos in positions}
    for b, h in boards:
        hauteur_bords[b] = h

    max_heights = []
    for i in range(len(positions)-1):
        left = positions[i]
        right = positions[i+1]

        # hauteur gauche
        h_left = hauteur_bords.get(left, 0)
        # hauteur droite
        h_right = hauteur_bords.get(right, 0)

        # Si bord extrême (0 ou 100)
        if left == 0:
            h_left = TANK_HEIGHT
        if right == TANK_WIDTH:
            h_right = TANK_HEIGHT

        max_h = min(h_left, h_right)
        max_heights.append(max_h)

    # Étape 3 : Pour chaque robinet, trouver la zone dans laquelle il se trouve
    # On considère que chaque robinet remplit la zone dans laquelle il est situé.
    # On va additionner les débits par zone.

    # Fonction utile pour trouver l'index de la zone contenant une position x
    # zones sont des intervalles [positions[i], positions[i+1])
    def zone_index(x):
        for i in range(len(positions)-1):
            if positions[i] < x < positions[i+1]:
                return i
        # Pas censé arriver car faucet ne peut être sur planche, et est dans [0,100]
        return -1

    # somme des débits par zone
    flow_by_zone = [0]* (len(positions)-1)
    for f_pos, amount in faucets:
        idx = zone_index(f_pos)
        flow_by_zone[idx] += amount

    # Étape 4 : Calcul de volume maximal (volume remplissage complet de chaque zone)
    # volume max par zone = largeur_zone * profondeur * hauteur_max_zone
    max_volumes = []
    for i in range(len(positions)-1):
        largeur_zone = positions[i+1] - positions[i]
        volume_zone = largeur_zone * TANK_DEPTH * max_heights[i]
        max_volumes.append(volume_zone)

    # Étape 5 : À partir du flux total d'entrée dans chaque zone, déterminer à l'instant t
    # le volume d'eau et donc la hauteur d'eau (volume / (largeur*profondeur)) dans cette zone.
    # Hauteur max est max_heights[i]

    # Pour optimisation on peut calculer 
    # accumuler vol d'eau dans chaque zone = temps * débit_zone
    # mais si volume dépasse le max_volumes => hauteur = hauteur max

    # Étape 6 : Pour chaque observation (position, t), retourner la hauteur d'eau dans la zone correspondante

    results = []
    for p, t in observations:
        idx = zone_index(p)
        # volume d'eau accumulé
        v = flow_by_zone[idx] * t
        # borne max
        if v > max_volumes[idx]:
            hauteur = max_heights[idx]
        else:
            largeur_zone = positions[idx+1] - positions[idx]
            hauteur = v / (largeur_zone * TANK_DEPTH)
        # On s'assure qu'on ne dépasse pas la hauteur max (même si volume max gère ça)
        hauteur = min(hauteur, max_heights[idx])
        results.append(hauteur)
    return results


def main():
    input=sys.stdin.read().strip().split()
    D = int(input[0])
    index = 1
    for _ in range(D):
        N = int(input[index]); index+=1
        boards = []
        for __ in range(N):
            B = int(input[index]); H = int(input[index+1])
            index+=2
            boards.append((B,H))
        M = int(input[index]); index+=1
        faucets = []
        for __ in range(M):
            F = int(input[index]); A = int(input[index+1])
            index+=2
            faucets.append((F,A))
        L = int(input[index]); index+=1
        observations = []
        for __ in range(L):
            P = int(input[index]); Tt = int(input[index+1])
            index+=2
            observations.append((P,Tt))

        results = simulate_water_level(N, boards, M, faucets, L, observations)
        for r in results:
            # Affiche avec précision maximale 0.001
            print("%.6f" % r)

if __name__ == "__main__":
    main()