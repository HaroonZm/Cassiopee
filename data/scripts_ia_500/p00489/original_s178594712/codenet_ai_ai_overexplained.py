import copy  # Importation du module 'copy' qui permet de faire des copies profondes d'objets complexes

# Lecture de l'entrée utilisateur pour obtenir un entier 'n'
# La fonction input() prend l'entrée utilisateur sous forme de chaîne de caractères
# La fonction int() convertit cette chaîne en entier
n = int(input())

# Calcul du nombre total de parties (matches) que l'on va simuler
# Pour un tournoi où chaque équipe joue contre toutes les autres une seule fois,
# le nombre de matches est n * (n-1) divisé par 2
game = n * (n - 1) // 2  
# '//' est l'opérateur de division entière en Python, qui renvoie un entier

# Initialisation de la liste 'point' de taille 'n'
# Cette liste contiendra les points accumulés par chaque équipe
# [0] * n crée une liste de 'n' éléments, tous initialisés à 0
point = [0] * n

# Boucle qui va s'exécuter 'game' fois, une fois pour chaque match
for _ in range(game):
    # Lecture d'une ligne d'entrée, contenant quatre entiers séparés par des espaces
    # Ceux-ci sont assignés aux variables a, b, c et d respectivement
    # a et b sont les indices des deux équipes jouant le match (1-indexés)
    # c et d sont les scores respectifs des équipes a et b
    a, b, c, d = map(int, input().split())

    # Comparaison des scores pour attribuer les points selon les règles
    # Si l'équipe a a un score supérieur à l'équipe b, elle gagne 3 points
    if c > d:
        # Les équipes sont 1-indexées en entrée, donc on soustrait 1 pour avoir un index 0-based
        point[a - 1] += 3
    # Si l'équipe b a un score supérieur, elle gagne 3 points
    elif c < d:
        point[b - 1] += 3
    # Si les scores sont égaux, c'est un match nul: chaque équipe gagne 1 point
    else:
        point[a - 1] += 1
        point[b - 1] += 1

# Création d'une copie profonde (indépendante) de la liste 'point'
# Cela permet de trier sans modifier la liste originale des points
point_tmp = copy.deepcopy(point)

# Tri de la liste copiée en ordre décroissant (du plus grand au plus petit)
# Le paramètre reverse=True inverse l'ordre de tri par défaut (croissant)
point_tmp.sort(reverse=True)

# Initialisation de la liste 'grade' qui contiendra le classement pour chaque équipe
# On crée une liste de taille 'n' remplie de zéros
grade = [0] * n

# Parcours de chaque équipe (index i) et de ses points p
for i, p in enumerate(point):
    # Pour chaque équipe, on cherche dans la liste triée (descendante) l'indice
    # de la première occurrence du score équivalent à p
    # index() renvoie la position de l'élément dans la liste, 0-based donc on ajoute 1 pour avoir un classement à partir de 1
    grade[i] = point_tmp.index(p) + 1

# Affichage du classement (grade) de chaque équipe
# Chaque élément est affiché sur une ligne séparée
for g in grade:
    print(g)