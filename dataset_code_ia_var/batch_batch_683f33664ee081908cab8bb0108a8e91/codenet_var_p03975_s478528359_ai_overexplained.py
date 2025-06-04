# Demande à l'utilisateur de saisir trois entiers séparés par des espaces et les assigne respectivement à N, A et B.
# - input() lit la ligne saisie par l'utilisateur sous forme de chaîne de caractères.
# - .split() découpe cette chaîne à chaque espace et renvoie une liste de chaînes.
# - map(int, ...) applique la fonction int à chaque élément de la liste pour la convertir en entier.
# - N est le premier entier, A le second et B le troisième dans l'ordre d'apparition.
N, A, B = map(int, input().split())

# Initialise un compteur appelé 'cnt' à zéro.
# Ce compteur va servir à compter le nombre de fois où une certaine condition est vérifiée dans la boucle ci-dessous.
cnt = 0

# Utilise une boucle for pour répéter une action N fois, où N a été spécifié par l'utilisateur précédemment.
for i in range(N):
    # À chaque itération, demande à l'utilisateur un entier supplémentaire à traiter.
    # - input() lit la saisie utilisateur.
    # - int(...) convertit la saisie en entier.
    n = int(input())

    # Vérifie si la valeur de n est strictement inférieure à A, ou
    # si la valeur de n est supérieure ou égale à B.
    # - L'opérateur 'or' signifie que si au moins une des deux conditions est vraie, le bloc s'exécutera.
    if n < A or B <= n:
        # Si la condition précédente est vraie, incrémente le compteur de un.
        # - cnt += 1 est équivalent à cnt = cnt + 1.
        cnt += 1

# Après avoir traité tous les nombres, affiche la valeur de cnt,
# qui correspond au nombre d'entrées pour lesquelles la condition dans le if était vraie.
print(cnt)