from copy import deepcopy

def afficher_grille(grille):
    for ligne in range(10):
        print(' '.join(map(str, grille[ligne])))

def basculer_cases_autour(grille, position_ligne, position_colonne):
    deplacements_colonne = [-1, 0, 0, 1, 0]
    deplacements_ligne = [0, -1, 0, 0, 1]
    for index_deplacement in range(5):
        nouvelle_ligne = position_ligne + deplacements_ligne[index_deplacement]
        nouvelle_colonne = position_colonne + deplacements_colonne[index_deplacement]
        if 0 <= nouvelle_ligne < 10 and 0 <= nouvelle_colonne < 10:
            grille[nouvelle_ligne][nouvelle_colonne] = 1 - grille[nouvelle_ligne][nouvelle_colonne]

def determiner_solution_premiere_ligne(grille_depart, combinaison_premiere_ligne):
    sequence_presses = [[0] * 10 for _ in range(10)]
    grille_temporaire = grille_depart
    for colonne in range(10):
        if (combinaison_premiere_ligne >> colonne) & 1 == 1:
            basculer_cases_autour(grille_temporaire, 0, colonne)
            sequence_presses[0][colonne] = 1

    for ligne in range(1, 10):
        for colonne in range(10):
            if grille_temporaire[ligne - 1][colonne] == 1:
                basculer_cases_autour(grille_temporaire, ligne, colonne)
                sequence_presses[ligne][colonne] = 1

    if 1 not in grille_temporaire[9]:
        afficher_grille(sequence_presses)
        return True

    return False

nombre_grilles = int(raw_input())
for _ in range(nombre_grilles):
    grille_entree = [list(map(int, raw_input().split())) for _ in range(10)]
    for combinaison in range(2 ** 10):
        if determiner_solution_premiere_ligne(deepcopy(grille_entree), combinaison):
            break