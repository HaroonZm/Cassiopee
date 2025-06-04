# Fonction utilitaire pour lire une ligne d'entrées de l'utilisateur,
# découper la chaîne de caractères aux espaces, convertir chaque morceau
# en entier, et retourner un itérable d'entiers.
def inpl():
    return map(int, input().split())

# Importation des utilitaires de collections.
# defaultdict permet d'avoir un dictionnaire qui retourne une valeur 
# par défaut lorsqu'une clé n'existe pas.
# Counter permet de compter facilement les occurrences de certains éléments.
from collections import defaultdict, Counter

# Lecture des dimensions d'une grille : H (hauteur), W (largeur), 
# et du nombre N de coordonnées à traiter.
H, W, N = inpl()

# Création d'un defaultdict pour stocker le décompte des sous-grilles
# qui comprennent un point donné. Chaque clé est un tuple (a, b), qui
# pourrait représenter le coin inférieur droit d'une sous-grille 3x3.
# Sa valeur est le nombre de fois où cette sous-grille a été affectée
# lors des insertions de points.
ddic = defaultdict(int)

# Boucle pour traiter les N insertions de points.
for _ in range(N):
    # Lecture des coordonnées A, B. Ce sont les positions (lignes et colonnes)
    # du point à placer sur la grille.
    A, B = inpl()
    # Pour chaque telle insertion, nous voulons parcourir tous les coins
    # en bas à droite des sous-grilles 3x3 qui contiennent ce point (A, B).
    # La sous-grille 3x3 dont le coin en bas à droite est (a, b) couvre 
    # les positions {(a-2, b-2), ..., (a, b)}.
    # Nous devons donc trouver tous les couples (a, b) tels que 
    # (A, B) appartient à cette sous-grille, en tenant compte des 
    # limites de la grille globale.
    # 
    # Le 'range' commence à max(3, A) car le coin droit-bas d'une 
    # sous-grille 3x3 doit avoir au moins la ligne/colonne 3.
    # On ne va pas plus loin que min(H, A+2)+1 car il ne faut pas dépasser
    # la grille, et on ajoute +1 car le second argument dans range est exclusif.
    for a in range(max(3, A), min(H, A+2)+1):
        for b in range(max(3, B), min(W, B+2)+1):
            # Pour chaque sous-grille affectée, on incrémente son compteur.
            ddic[(a, b)] += 1

# A ce stade, ddic contient pour chaque sous-grille 3x3 (clé = (a, b)) le nombre de points
# insérés qui tombent à l'intérieur.

# On utilise Counter pour compter combien de sous-grilles ont k points à l'intérieur,
# c'est-à-dire combien de valeurs de ddic sont égales à k pour chaque k.
C = Counter(ddic.values())

# Impression du nombre de sous-grilles 3x3 qui ne contiennent aucun point.
# Le nombre total de sous-grilles 3x3 dans la grille principale est (H-2)*(W-2)
# (car on ne peut placer le coin bas-droite qu'à partir de la ligne 3 et 
# jusque H, idem pour les colonnes).
# On fait la différence entre ce total et la somme de toutes les sous-grilles
# qui contiennent au moins 1 point.
print((H-2)*(W-2) - sum(C.values()))

# Pour chaque i de 1 à 9 (c'est-à-dire toutes les options possibles du nombre
# de points dans une sous-grille 3x3, sachant qu'une telle sous-grille peut 
# contenir entre 1 et 9 points maximum)
for i in range(1, 10):
    # On imprime combien de sous-grilles ont exactement i points à l'intérieur.
    # Si aucun sous-grille n'a exactement i points, Counter renvoie 0.
    print(C[i])