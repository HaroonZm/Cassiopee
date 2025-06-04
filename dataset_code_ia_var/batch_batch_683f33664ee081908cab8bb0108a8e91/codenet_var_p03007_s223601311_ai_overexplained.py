# Demander à l'utilisateur d'entrer un entier N (le nombre d'éléments du tableau).
N = int(input())

# Demander à l'utilisateur d'entrer N entiers séparés par des espaces, convertir chaque entrée en entier,
# créer une liste à partir de ces entiers, et finalement trier cette liste dans l'ordre croissant.
A = sorted((list(map(int, input().split()))))

# Si N est égal à 2, traiter ce cas séparément car il s'agit d'un cas simple où il n'y a que deux nombres.
if N == 2:
    # Décomposer la liste triée en deux variables y et x, la première reçoit le plus petit nombre,
    # la deuxième reçoit le plus grand.
    y, x = A
    # Calculer et afficher la différence entre les deux (éventuellement un nombre positif),
    # ce sera le "score" maximal possible.
    print(x-y)
    # Afficher x et y, qui seront les termes du premier (et unique) calcul, où x - y sera le résultat.
    print(x, y)
    # Arrêter le programme, car on a déjà traité ce cas.
    exit()

# Créer une liste vide XY pour stocker les paires (x, y) correspondant à chaque opération de soustraction x - y.
XY = []

# Définir deux compteurs pour compter combien il y a d'éléments positifs ou nuls (PLUS)
# et combien il y a d'éléments strictement négatifs (MINUS).
PLUS = 0   # Compteur pour les entiers >= 0
MINUS = 0  # Compteur pour les entiers < 0

# Parcourir chaque élément dans la liste A triée pour mettre à jour les compteurs PLUS et MINUS.
for a in A:
    if a >= 0:
        PLUS += 1  # Incrémenter PLUS si l'élément est positif ou nul
    else:
        MINUS += 1 # Incrémenter MINUS si l'élément est strictement négatif

# Réinitialiser la liste XY qui stockera les opérations effectuées.
XY = []

# Prendre le plus petit élément de la liste triée A et l'affecter à la variable temporaire tmp.
# Après ce point, tmp contiendra toujours le résultat temporaire des soustractions successives.
tmp = A[0]

# S'il y a à la fois des nombres positifs (ou nuls) ET des nombres négatifs dans la liste
if PLUS and MINUS:
    # On va privilégier une stratégie pour maximiser la différence finale.
    # Tant qu'il reste au moins deux entiers positifs ou nuls non utilisés,
    # on soustrait le plus grand de ces éléments à tmp à chaque étape.
    while PLUS >= 2:
        # Affecter à x la valeur de tmp (résultat courant), et à y le plus grand élément restant de la liste A.
        x, y = tmp, A.pop()  # Retirer l'élément de la fin (le plus grand)
        # Ajouter la paire (x, y) à la liste XY pour garder la trace de cette opération.
        XY.append((x, y))
        # Mettre à jour tmp en effectuant x - y, ce qui diminue (ou augmente négativement) tmp.
        tmp = x - y
        # Décrémenter le compteur PLUS car on vient d'utiliser un élément positif ou nul.
        PLUS -= 1

    # Après avoir soustrait tous les grands positifs sauf un, il reste à effectuer l'opération entre
    # le dernier positif et le résultat temporaire accumulé.
    x, y = A.pop(), tmp  # Prendre le dernier nombre positif restant et tmp
    XY.append((x, y))
    tmp = x - y

    # Maintenant il ne reste que les négatifs non utilisés au début.
    N = len(A)  # Met à jour N au nombre d'éléments restants (ce sont tous négatifs)
    # Commencer à partir du 2ème plus petit élément puisque le plus petit a déjà été utilisé comme tmp initial.
    for i in range(1, N):
        # Prendre chacun des éléments restant de la liste A, ce sont les valeurs négatives.
        a = A[i]
        # Effectuer la soustraction entre le résultat temporaire actuel et cet élément négatif.
        x, y = tmp, a
        XY.append((x, y))
        tmp = x - y  # Mettre à jour tmp

# S'il n'y a AUCUN élément strictement négatif (que des positifs ou des zéros)
elif PLUS:
    # Dans ce cas on procède différemment pour maximiser le résultat final.
    # Parcourir tous les éléments sauf le dernier.
    for i in range(N-1):
        # Tant qu'on n'est pas à l'avant-dernière étape, on continue à soustraire le plus grand disponible à tmp.
        if i < N-2:
            x, y = tmp, A.pop()  # tmp reste la première valeur (la plus petite) et A.pop() enlève le plus grand non utilisé.
            XY.append((x, y))
            tmp = x - y
        # À l'avant-dernier tour, on inverse l'ordre pour que tmp soit maintenant celui qu'on vient d'obtenir,
        # et le dernier élément restant de la liste (qui est la plus petite valeur positive si différents).
        if i == N-2:
            x, y = A.pop(), tmp
            XY.append((x, y))
            tmp = x - y

# S'il n'y a AUCUN nombre positif ou nul, donc que des valeurs négatives
else:
    # On effectue ici une stratégie adaptée aux valeurs strictement négatives.
    # On effectue d'abord la soustraction entre le plus grand négatif (donc celui le plus proche de 0)
    # et la plus petite valeur (la plus négative).
    for i in range(N-1):
        if i == 0:
            # x est le plus grand des négatifs (A.pop()), y est tmp (le plus petit/l'élément plus négatif)
            x, y = A.pop(), tmp
            XY.append((x, y))
            tmp = x - y
        else:
            # Ensuite, on continue à soustraire les autres plus grands à tmp successivement.
            x, y = tmp, A.pop()
            XY.append((x, y))
            tmp = x - y

# À la fin des opérations, tmp contient le résultat final obtenu après les (N-1) soustractions successives.
ans = tmp
# Afficher ce résultat final.
print(ans)
# Parcourir la liste XY et afficher chaque couple (x, y) sur une ligne, ce qui montre chaque opération effectuée.
for x, y in XY:
    print(x, y)