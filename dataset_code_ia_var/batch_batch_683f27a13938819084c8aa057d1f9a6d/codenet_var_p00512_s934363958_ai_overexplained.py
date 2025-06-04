# Demande à l'utilisateur de saisir une donnée via le clavier
# La fonction input() reçoit une chaîne de caractères et int() la transforme en nombre entier
n = int(input())

# Création d'un dictionnaire vide appelé 'o'
# Le dictionnaire permet de stocker des paires clé/valeur, où chaque clé est le nom et chaque valeur est un total associé
o = {}

# Utilisation d'une boucle for pour répéter une opération n fois (de 0 à n-1)
for i in range(n):
    # Lecture d'une ligne de texte, séparation en 2 parties par défaut (sur les espaces) et affectation aux variables 'name' et 'value'
    name, value = input().split()
    # Vérifie si le nom est déjà présent dans le dictionnaire 'o'
    if name in o:
        # Si 'name' existe, ajoute la valeur entière convertie à la valeur déjà stockée
        o[name] += int(value)
    else:
        # Si 'name' n'existe pas dans le dictionnaire, crée une nouvelle entrée avec comme valeur l'entier lu
        o[name] = int(value)

# Trie les éléments de 'o' (qui sont des couples clé/valeur) selon la clé (le nom, c'est-à-dire x[0])
# La méthode items() extrait les couples clé/valeur du dictionnaire sous forme de tuples (name, total)
# La fonction sorted() retourne une nouvelle liste triée sans modifier l'ordre d'origine
o = sorted(o.items(), key=lambda x: x[0])

# Trie la liste 'o' in-place (modifie l'objet 'o' lui-même) selon la longueur des noms (len(x[0]))
# Cela revient à appliquer d'abord le tri alphabétique (précédent), puis un tri par longueur du nom
# o devient donc une liste de tuples triée de façon stable (le premier tri étant préservé pour les longueurs égales)
o.sort(key = lambda x: len(x[0]))

# Parcours la liste triée 'o' à l'aide d'une boucle for, 'i' représentant chaque tuple
for i in o:
    # Affiche le nom (i[0]) et la valeur associée (i[1]), séparés par un espace
    # La méthode format() insère les éléments dans la chaîne à la place des {0} et {1}
    print("{0} {1}".format(i[0], i[1]))