def read_paths():
    """
    Lis les chemins d'entrée de l'utilisateur sur trois lignes. 
    Chaque ligne doit contenir deux entiers séparés par un espace.
    Returns:
        list: Une liste de trois sous-listes, 
            chacune contenant deux entiers représentant un chemin.
    """
    paths = []
    for _ in range(3):
        # Demande à l'utilisateur de saisir deux entiers séparés par un espace
        chemin = list(map(int, input().split()))
        paths.append(chemin)
    return paths

def compter_passages(paths):
    """
    Comptabilise les passages par chaque sommet à partir de la liste des chemins.
    Les sommets sont supposés être numérotés de 1 à 4.

    Args:
        paths (list): Liste de listes, où chaque sous-liste contient deux entiers.

    Returns:
        list: Liste de 4 entiers représentant le nombre de fois 
              que chaque sommet (1 à 4) est utilisé dans les chemins.
    """
    cnt = [0, 0, 0, 0]  # Compteur pour chaque sommet (1 à 4)
    for i in range(3):  # Parcourt les trois chemins
        for j in range(2):  # Pour chaque extrémité du chemin
            sommet = paths[i][j]
            cnt[sommet - 1] += 1  # Incrémente le compteur correspondant
    return cnt

def verification(cnt):
    """
    Vérifie qu'aucun sommet n'est utilisé trois fois ou plus dans les chemins.

    Args:
        cnt (list): Liste de 4 entiers, compteurs de passages par sommet.

    Returns:
        bool: True si chaque sommet est utilisé strictement moins de 3 fois, False sinon.
    """
    for compteur in cnt:
        if compteur >= 3:
            return False
    return True

def main():
    """
    Programme principal. Lit les chemins, compte les passages, 
    vérifie la condition, puis affiche 'YES' ou 'NO'.
    """
    paths = read_paths()
    cnt = compter_passages(paths)
    if verification(cnt):
        print("YES")
    else:
        print("NO")

# Lancement du programme principal
main()