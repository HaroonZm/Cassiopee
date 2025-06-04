# Lecture de trois entiers séparés par des espaces à partir de l'entrée utilisateur
# La fonction input() lit une ligne de texte depuis l'utilisateur sous forme de chaîne de caractères
# La méthode split() divise la chaîne d'entrée en une liste de sous-chaînes, en utilisant l'espace comme séparateur par défaut
# La fonction map(int, ...) applique la fonction int à chaque élément de cette liste pour les convertir en entiers
# Les trois valeurs ainsi obtenues sont affectées respectivement aux variables N, M, et T grâce à l'affectation multiple
N, M, T = map(int, input().split())

# Lecture d'une seconde ligne de l'entrée représentant une séquence d'entiers
# input() lit la ligne entière comme chaîne
# split() la convertit en liste de chaînes représentant des nombres
# La liste en compréhension [int(x) for x in ...] convertit chaque élément en entier
# Le résultat est une liste d'entiers stockée dans la variable A
A = [int(x) for x in input().split()]

# Le calcul suivant consiste à déterminer une valeur selon plusieurs opérations :
# - A[0] : accède au premier élément de la liste A (indice 0), car en Python les indices commencent à 0
# - M : c'est un entier déjà lu plus haut, sera soustrait de A[0]
# - A[-1] : accède au dernier élément de la liste A de manière compacte avec l'indice négatif
# - T : entier précédemment défini
# - T - A[-1] - M : calcule la différence entre le temps total (T), le dernier élément de A et M
# - max(T - A[-1] - M, 0) : prend la valeur précédente ou 0, selon laquelle est la plus grande ; donc si la différence est négative, 0 sera pris
# - sum(... for i in range(N - 1)) : somme d'une série de valeurs générées par une expression pour chaque i variant de 0 à N-2 inclus, soit pour chaque paire consécutive d'éléments dans A
# - A[i+1] - A[i] : différence entre deux éléments consécutifs
# - 2 * M : double la valeur de M
# - max(0, A[i+1] - A[i] - 2 * M) : prend la différence précédente, mais la valeur 0 si elle est négative afin de ne pas soustraire plus que disponible
# Enfin, tous ces éléments sont additionnés ensemble
# Le résultat de ce calcul est envoyé à la fonction print() qui l'affiche à l'écran
print(
    A[0]                     # Premier élément de la liste A
    - M                      # Soustraction de la valeur M
    + max(T - A[-1] - M, 0)  # Ajout du maximum entre (T - dernier élément de A - M) et 0
    + sum(                   # Ajout de la somme obtenue sur chacun des écarts entre éléments consécutifs
        max(                 # On ne garde que le positif :
            0,               # soit 0
            A[i+1] - A[i] - 2 * M # soit la différence entre deux éléments consécutifs moins deux fois M
        )
        for i in range(N - 1) # pour tous les indices i allant de 0 à N-2 (inclus), soit sur chaque paire voisine
    )
)