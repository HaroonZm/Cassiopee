# Solution complète au problème "すごろくと駒" (Sugoroku and Pieces)
# - On simule les déplacements des pièces sur un plateau de 2019 cases
# - Chaque pièce peut avancer d'une case sauf si elle est déjà au but (case 2019)
#   ou si la case cible est occupée par une autre pièce.
# - On maintient la position de chaque pièce et met à jour après chaque opération.

def main():
    # Lecture du nombre de pièces
    N = int(input())
    # Positions initiales des pièces i (1-indexé)
    positions = list(map(int, input().split()))
    # Lecture du nombre d'opérations
    M = int(input())
    # Liste des opérations, chaque élément est l'indice de la pièce à déplacer
    moves = list(map(int, input().split()))
    
    # Pour faciliter la recherche, on peut maintenir un ensemble (ou dictionnaire) 
    # des positions occupées, ou on peut vérifier dans la liste positions directement.
    # Vu que N est petit, une recherche linéaire est efficace.
    
    for move in moves:
        piece_index = move - 1  # conversion en indice 0-based
        current_pos = positions[piece_index]
        # Si la pièce est déjà sur la case finale, on ne peut pas avancer
        if current_pos == 2019:
            continue
        next_pos = current_pos + 1
        # Vérifier si la case suivante est occupée par une autre pièce
        # On vérifie dans la liste des positions sauf la pièce en cours.
        if next_pos in positions:
            # Case occupée, donc on ne déplace pas la pièce
            continue
        # Sinon, la pièce avance d'une case
        positions[piece_index] = next_pos
    
    # Après toutes les opérations, on affiche la position finale de chaque pièce
    for pos in positions:
        print(pos)

if __name__ == "__main__":
    main()