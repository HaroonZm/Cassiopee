# Solution en Python pour le problème "D - 権力"
# Approche :
# - Il s'agit d'un problème de couverture d'intervalle minimal.
# - Nous avons un segment de 1 à N (les chambres).
# - Chaque professeur couvre un intervalle [a_i, b_i].
# - Le but est de couvrir tous les indices de 1 à N avec le moins de professeurs possible.
# - Si ce n'est pas possible, on affiche "Impossible".
#
# Approche détaillée :
# 1) Trier les professeurs par leur début d'intervalle (a_i).
# 2) On parcourt de manière "gloutonne" depuis la chambre 1 jusqu'à la chambre N :
#    - À l'étape courante, on cherche parmi tous les professeurs dont l'intervalle commence avant ou à la position actuelle
#      celui qui couvre le plus loin à droite (b_i maximal).
#    - On sélectionne ce professeur pour couvrir l'intervalle le plus loin possible.
#    - On avance la position à la limite droite du professeur choisi + 1.
# 3) Si à un moment aucun professeur ne peut étendre la couverture, on est dans le cas "Impossible".
# 4) Sinon, on compte le nombre de professeurs sélectionnés pour couvrir tout N.
#
# Cette méthode est efficace avec les contraintes N, M <= 100.

import sys

def main():
    input = sys.stdin.readline
    N, M = map(int, input().split())
    intervals = []
    for _ in range(M):
        a, b = map(int, input().split())
        intervals.append((a, b))
    # Trier par début d'intervalle
    intervals.sort(key=lambda x: x[0])

    result = []
    current_coverage = 1  # prochaine chambre à couvrir
    i = 0  # index dans intervals
    max_right = -1
    selected_professor = -1

    while current_coverage <= N:
        # Chercher intervalle qui commence <= current_coverage et avec b maximal
        found = False
        max_b = -1
        while i < M and intervals[i][0] <= current_coverage:
            if intervals[i][1] >= max_b:
                max_b = intervals[i][1]
                selected_professor = i
                found = True
            i += 1
        if not found:
            # impossible de couvrir la chambre current_coverage
            print("Impossible")
            return
        # On sélectionne ce professeur
        result.append(selected_professor)
        # On avance la couverture au-delà de l'intervalle choisi
        current_coverage = max_b + 1
        # On remet i à la position de résultat pour continuer la recherche à partir du début
        # car on a parcouru tous les intervalles qui commencent <= current_coverage précédemment,
        # il faut continuer à partir d'ici pour couvrir la suite.
        # En réalité, on doit remettre i au premier intervalle qui commence après la couverture actuelle:
        # Pour cela, on peut remettre i à la position du dernier professeur sélectionné +1 et scanner à nouveau.
        # Mais pour simplifier, on re-scannera tous les intervalles qui commencent <= current_coverage
        # Donc on remet i à la position de result[-1]+1 et on ajuste en conséquence.
        # Pour simplifier la gestion, on va utiliser un pointeur séparé.

    print(len(result))

if __name__ == "__main__":
    main()