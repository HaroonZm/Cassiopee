# Demander à l'utilisateur de saisir deux entiers séparés par un espace.
# Cette ligne prend l'entrée de l'utilisateur au format texte, la sépare sur les espaces grâce à .split(),
# puis convertit chaque morceau en entier grâce à map(int, ...).
# Enfin, elle assigne les deux valeurs respectivement à N et M.
N, M = map(int, input().split())

# Lecture de N lignes depuis l'entrée standard pour constituer la première liste.
# On utilise une compréhension de liste pour itérer N fois (de 0 à N-1).
# À chaque itération, on appelle input() qui lit une ligne de texte.
# La liste résultante, A, contient N chaînes de caractères provenant de l'utilisateur.
A = [input() for _ in range(N)]

# Lecture d'un deuxième bloc de N lignes, de la même manière que précédemment.
# On stocke ces chaînes dans une nouvelle liste appelée B.
B = [input() for _ in range(N)]

# Initialisation d'une variable entière pour compter le nombre de différences,
# c'est-à-dire le nombre de caractères différents entre les deux blocs A et B.
# On commence ce compteur à zéro.
ans = 0

# La fonction zip(A, B) prend deux listes et forme des paires d'éléments ayant la même position
# dans chaque liste. Cela crée ainsi un itérable de tuples où chaque tuple contient une ligne de A et la même ligne de B.
# On fait alors une boucle for pour itérer sur toutes ces paires (a, b).
for a, b in zip(A, B):
    # Pour chaque paire de lignes (a dans A, b dans B), faites la même opération :
    # zip(a, b) ici va prendre deux chaînes de caractères (qui sont itérables),
    # et former des paires de caractères correspondants, c'est-à-dire le i-ème caractère de a avec le i-ème de b.
    for aa, bb in zip(a, b):
        # Pour chaque paire de caractères (aa tiré de a, bb tiré de b),
        # on vérifie s'ils sont différents avec l'opérateur != (différent de).
        if aa != bb:
            # Si les caractères sont différents, on incrémente le compteur ans de 1.
            ans += 1

# Affichage du résultat final à l'aide de la fonction print(),
# qui affiche le nombre total de caractères différents entre A et B.
print(ans)