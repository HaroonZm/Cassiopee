import itertools  # On importe le module itertools, qui contient des fonctions pour travailler avec des itérateurs et des objets combinatoires, comme les permutations.

# Demande à l'utilisateur de saisir un nombre entier.
# La fonction input() récupère l'entrée sous forme de chaîne de caractères.
# int() convertit cette chaîne en un entier.
n = int(input())

# Création d'une liste appelée 'num'.
# Utilise une compréhension de liste pour générer les entiers de 1 à n (inclus).
# range(1, n+1) génère une séquence commençant à 1 et allant jusqu'à n compris (car le deuxième argument de range est exclusif).
num = [i for i in range(1, n+1)]

# Boucle 'for' utilisée pour itérer à travers toutes les permutations de la liste 'num'.
# itertools.permutations(num) génère toutes les permutations possibles de la liste 'num'.
# Chaque permutation est un tuple contenant un ordre unique des éléments de 'num'.
for per in itertools.permutations(num):
    # À chaque itération, 'per' est une permutation actuelle de 'num' sous forme de tuple.
    # 'str(p) for p in per' est une compréhension de générateur qui convertit chaque élément du tuple en chaîne de caractères.
    # ' '.join(...) prend chaque chaîne de caractères générée et les assemble en une seule chaîne, avec un espace entre chaque chiffre.
    # print() affiche ensuite cette chaîne à l'écran, correspondant à une permutation.
    print(' '.join(str(p) for p in per))