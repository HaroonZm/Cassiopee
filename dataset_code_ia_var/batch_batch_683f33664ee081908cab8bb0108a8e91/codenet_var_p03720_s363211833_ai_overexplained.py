# Importation du module defaultdict depuis la bibliothèque collections
# defaultdict est une sous-classe de dictionnaire qui permet de définir une valeur par défaut pour les clés inexistantes
from collections import defaultdict

# Lecture de la première ligne de l'entrée standard (input), qui contient deux entiers séparés par un espace
# L'appel à input() récupère la ligne sous forme de chaîne de caractères
# split() sépare la chaîne en une liste sur les espaces
# map(int, ...) applique la fonction int à chaque élément de la liste pour convertir les chaînes en entiers
# L'affectation multiple permet de stocker les deux valeurs dans les variables N et M respectivement
N, M = map(int, input().split())

# Création d'un dictionnaire nommé city_road_nums avec int comme valeur par défaut
# Cela signifie que si on essaie d'accéder à une clé inexistante, elle sera automatiquement créée avec la valeur 0 (car int() retourne 0)
city_road_nums = defaultdict(int)

# Utilisation d'une boucle for servant à répéter une action M fois, c'est-à-dire pour chaque route
# range(M) produit des entiers de 0 à M-1 (total M nombres), _ est une variable anonyme car la valeur n'est pas utilisée dans le corps de boucle
for _ in range(M):
    # Pour chaque itération, lecture d'une ligne d'entrée décrivant une route entre deux villes
    # Chaque ligne contient deux entiers a et b, séparés par un espace
    a, b = map(int, input().split())  # Conversion de l'entrée en deux entiers
    # Incrément du compteur d'arêtes (routes) pour la ville a
    # city_road_nums[a] représente le nombre actuel de routes connectées à la ville a, initialisé à 0 si a n'existe pas déjà comme clé
    city_road_nums[a] += 1
    # Incrément du compteur d'arêtes (routes) pour la ville b, car la route est bidirectionnelle (non orientée)
    city_road_nums[b] += 1

# Utilisation d'une boucle for pour parcourir tous les numéros de villes de 1 à N inclus
# range(1, N+1) génère une séquence d'entiers commençant à 1 jusqu'à N (puisque range exclut le dernier paramètre)
for i in range(1, N+1):
    # Affichage du nombre de routes connectées à la ville i
    # city_road_nums[i] retourne la valeur associée à la clé i dans le dictionnaire, 0 si la clé n'existe pas encore
    print(city_road_nums[i])