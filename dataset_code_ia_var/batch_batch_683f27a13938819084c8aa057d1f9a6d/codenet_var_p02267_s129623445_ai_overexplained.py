# Demande à l'utilisateur de saisir une valeur, la fonction input() retourne une chaîne de caractères, 
# donc nous utilisons int() pour convertir la chaîne en un entier
n = int(input())

# Demande à l'utilisateur de saisir plusieurs valeurs séparées par des espaces sur une seule ligne
# input() récupère la ligne entière en tant que chaîne de caractères
# split() découpe la chaîne en une liste de sous-chaînes à chaque espace
# Pour chaque sous-chaîne obtenue (représentant un nombre), on l'utilise dans une compréhension de liste :
# pour chaque élément _, on convertit ce texte en entier avec int() et on l'ajoute à la liste S
S = [int(_) for _ in input().split()]

# De la même façon que précédemment, on demande à l'utilisateur le prochain entier q
q = int(input())

# On récupère une nouvelle ligne de nombres séparés par des espaces
# On utilise une compréhension de liste pour les convertir tous en entiers et les stocker dans la liste T
T = [int(_) for _ in input().split()]

# On initialise une variable compteur cnt à zéro
# Cette variable servira à compter combien d'éléments de la liste T apparaissent aussi dans la liste S
cnt = 0

# On parcourt chaque élément t de la liste T avec une boucle for
for t in T:
    # Pour chaque t, on vérifie s'il existe dans la liste S en utilisant l'opérateur "in"
    # "in" va comparer t avec chaque élément de S et retourner True si t est trouvé dedans
    if t in S:
        # Si t est présent dans S, on incrémente de 1 la variable compteur cnt 
        cnt += 1

# À la fin, on affiche sur la sortie standard (l'écran) la valeur finale du compteur cnt
# C'est le nombre d'éléments de T qui étaient aussi dans S
print(cnt)