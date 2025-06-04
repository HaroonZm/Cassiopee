# Importation de la classe defaultdict depuis le module collections.
# defaultdict est une sous-classe de dict qui fournit une valeur par défaut pour les clés non présentes.
from collections import defaultdict

# Lecture d'un entier à partir de l'entrée standard (l'utilisateur saisit une valeur).
# La fonction input() retourne une chaîne de caractères, qui est convertie en entier avec int().
N = int(input())

# Lecture d'une ligne de l'entrée standard correspondant à une suite d'entiers séparés par des espaces.
# input().split() divise la chaîne saisie par l'utilisateur en une liste de sous-chaînes selon les espaces.
# map(int, ...) transforme chaque sous-chaîne en entier.
# list(...) convertit l'objet map en une liste d'entiers.
src = list(map(int, input().split()))

# Initialisation d'une variable pour stocker le résultat final (réponse).
# Ici, ans compte le nombre de paires respectant une certaine condition.
ans = 0

# Création d'un dictionnaire avec une valeur entière par défaut de 0.
# Si une clé n'existe pas, elle sera créée automatiquement avec la valeur 0.
d = defaultdict(int)

# Création d'une liste vide nommée 'e', qui n'est pas utilisée dans le programme.
e = []

# Boucle pour parcourir la liste 'src' avec un indice.
# enumerate(src, 1) retourne des couples (i, s), où i démarre à 1 (premier indice) et s est la valeur correspondante.
for i, s in enumerate(src, 1):
    # Calcul de la somme de l'indice actuel (i) et de la valeur du tableau à cette position (s).
    # 'l' peut être vu comme une clé représentant un certain état ou critère métier.
    l = i + s

    # Calcul de la différence entre l'indice courant (i) et la valeur du tableau à cette position (s).
    # 'r' est une autre clé utilisée pour vérifier une condition.
    r = i - s

    # Incrémentation du nombre d'occurrences de la clé 'l' dans le dictionnaire 'd' de 1.
    # Si 'l' n'est pas encore présente dans 'd', elle est automatiquement initialisée à 0 grâce à defaultdict.
    d[l] += 1

    # Ajout au compteur 'ans' du nombre d'occurrences actuelles de la clé 'r' dans 'd'.
    # Cela permet de compter toutes les situations où une condition basée sur les indices et valeurs est respectée.
    ans += d[r]

# Affichage du résultat calculé, qui est le nombre total de paires correspondantes selon la logique précédente.
print(ans)