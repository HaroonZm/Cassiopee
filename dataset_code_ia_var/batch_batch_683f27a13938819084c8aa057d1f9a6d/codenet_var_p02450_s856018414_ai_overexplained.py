# Importation du module 'itertools' qui contient des fonctions avancées sur les itérateurs
import itertools

# Demande à l'utilisateur d'entrer un nombre via la fonction input()
# input() permet de lire une ligne de texte depuis l'entrée standard (typiquement, le clavier)
# La valeur retournée par input() est une chaîne de caractères (str)
# La fonction int() convertit cette chaîne en un entier
user_input = input()           # Stocke la chaîne entrée par l'utilisateur
n = int(user_input)            # Convertit la chaîne en un entier

# La fonction range(1, n+1) génère des nombres entiers consécutifs, de '1' à 'n' inclus
# range(start, stop) commence à 'start' et s'arrête AVANT 'stop'
number_range = range(1, n+1)   # Crée un objet range allant de 1 à n compris

# La fonction permutations retourne un itérable contenant tous les arrangements ordonnés possibles sans répétition
# Chaque arrangement (ou 'permutation') est retourné comme un tuple
# On convertit cet itérable en liste pour permettre une itération multiple ou un accès par index (pas nécessaire ici, mais équivalent au code d'origine)
all_permutations = list(itertools.permutations(number_range))

# Boucle sur toutes les permutations stockées dans 'all_permutations'
for p in all_permutations:
    # L'étoile (*) est un opérateur qui "déréférence" ou "dépaquette" le tuple 'p', c'est-à-dire qu'il transmet chaque valeur du tuple comme argument séparé à la fonction print
    # Ainsi, les éléments de la permutation sont affichés séparés par un espace, car c'est le comportement par défaut de 'print'
    print(*p)