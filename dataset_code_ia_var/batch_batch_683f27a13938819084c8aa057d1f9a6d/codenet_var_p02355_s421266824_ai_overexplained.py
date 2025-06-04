# Lecture de deux entiers à partir de l'entrée standard, séparés par un espace
# map(int, ...) convertit chaque élément en entier
# input().split() divise la ligne d'entrée en une liste de chaînes de caractères
n, k = map(int, input().split())

# Lecture d'une séquence de n entiers à partir de l'entrée standard
# map(int, ...) convertit chaque élément en entier
# input().split() divise la ligne d'entrée en une liste de chaînes de caractères
# list(...) convertit l'objet map en liste
aa = list(map(int, input().split()))

# Initialisation d'un tableau de compteurs de taille k + 1 (indice 0 à k inclus)
# Cela permet de compter l'occurrence de chaque nombre de 1 à k dans la fenêtre considérée
cnts = [0] * (k + 1)

# Initialisation de la variable de réponse avec une grande valeur (1 000 000.0)
# Elle servira à garder la longueur minimale trouvée
ans = 1e6

# Variable pour compter combien de nombres distincts de 1 à k existent actuellement dans la fenêtre
existing = 0

# Variable représentant la borne droite de la fenêtre (pointeur du sliding window)
r = 0

# On va parcourir toutes les positions possibles de départ de la fenêtre (variable l)
# range(n - k + 1) signifie que l va de 0 à n - k inclus
for l in range(n - k + 1):

    # Boucle pour agrandir la fenêtre à droite autant que nécessaire
    # On continue tant que r < n (on ne sort pas du tableau)
    # ET qu'on n'a pas encore trouvé k nombres distincts dans la fenêtre actuelle
    while r < n and existing < k:
        # On prend la valeur courante à la position r dans aa (sliding window droite)
        a = aa[r]
        # Si la valeur lue est inférieure ou égale à k, on la prend en compte
        if a <= k:
            # On incrémente le compteur pour ce nombre
            cnts[a] += 1
            # Si c'est la première fois qu'on rencontre ce nombre dans la fenêtre
            if cnts[a] == 1:
                # On augmente le nombre de types distincts présents
                existing += 1
        # On élargit la fenêtre vers la droite
        r += 1

    # Après la boucle, si on a bien k valeurs distinctes de 1 à k dans la fenêtre
    if k == existing:
        # On met à jour la plus petite taille de fenêtre trouvée
        ans = min(ans, r - l)

    # On va maintenant déplacer la borne gauche, donc on retire aa[l] de la fenêtre
    a = aa[l]
    # Si la valeur retirée est inférieure ou égale à k, on met à jour le compteur
    if a <= k:
        # On décrémente le nombre de fois où aa[l] apparaît dans la fenêtre
        cnts[a] -= 1
        # Si le nombre n'est plus présent dans la fenêtre, on enlève un type à existing
        if cnts[a] == 0:
            existing -= 1

# Finalement, on vérifie si on a trouvé une solution
# Si la réponse est restée à 1e6 (pas de solution), on affiche 0
# Sinon, on affiche la plus petite taille trouvée
print(ans if ans < 1e6 else 0)