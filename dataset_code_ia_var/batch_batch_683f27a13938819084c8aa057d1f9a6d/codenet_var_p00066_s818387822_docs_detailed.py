import sys

def win(c, line):
    """
    Détermine si le joueur représenté par le caractère 'c' (ex: 'o' ou 'x') a gagné la partie de morpion.
    La ligne 'line' doit contenir une chaîne de 9 caractères représentant la grille de morpion,
    parcourue ligne par ligne.

    Args:
        c (str): Le caractère du joueur à tester ('o' ou 'x').
        line (str): La chaîne représentant la grille du plateau, de longueur 9.

    Returns:
        bool: True si le joueur 'c' a une combinaison gagnante, False sinon.
    """
    # Vérifie les trois lignes horizontales
    for i in range(0, 9, 3):
        # Vérifie si les trois cases de la ligne sont occupées par le joueur 'c'
        if all(p == c for p in line[i:i + 3]):
            return True

    # Vérifie les trois colonnes verticales
    for i in range(3):
        # Vérifie si toutes les cases de la colonne i sont occupées par le joueur 'c'
        if all(line[j] == c for j in range(i, 9, 3)):
            return True

    # Vérifie la diagonale descendante (\) : indices 0, 4, 8
    if all(line[i] == c for i in range(0, 9, 4)):
        return True

    # Vérifie la diagonale ascendante (/) : indices 2, 4, 6
    if all(line[i] == c for i in range(2, 7, 2)):
        return True

    # Aucune condition gagnante détectée pour le joueur 'c'
    return False

# Parcourt chaque ligne lue depuis l'entrée standard (stdin)
for line in sys.stdin:
    # Supprime les éventuels retours à la ligne à la fin de la chaîne
    line = line.strip()
    # Teste pour chacun des joueurs, 'o' puis 'x', s'il a gagné
    for c in ['o', 'x']:
        if win(c, line):
            # Affiche le caractère du joueur vainqueur et arrête le test pour cette ligne
            print(c)
            break
    else:
        # Si aucun joueur n'a gagné, affiche 'd' pour indiquer un match nul (draw)
        print('d')