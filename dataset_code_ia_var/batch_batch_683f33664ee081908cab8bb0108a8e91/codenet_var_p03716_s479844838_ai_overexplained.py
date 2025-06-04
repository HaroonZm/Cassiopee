import heapq  # Importe le module heapq, qui permet d'utiliser des files de priorité (tas) min-heaps

# Lecture de la valeur entière N au clavier
N = int(input())  # 'input()' récupère la chaîne entrée, 'int()' la convertit en entier

# Lecture d'une ligne d'entiers, séparés par des espaces, convertis en liste d'entiers
src = list(map(int, input().split()))
# 'input()' lit la ligne, 'split()' sépare les valeurs, 'map(int, ...)' convertit chaque valeur en entier
# et 'list()' construit la liste effective des entiers

# Calcul de la somme des N premiers éléments de la liste src
s1 = sum(src[:N])
# 'src[:N]' crée une sous-liste allant du début jusqu'à (sans inclure) src[N]
# 'sum()' additionne tous les éléments de cette tranche

# Création d'une liste r1 contenant s1 comme premier élément
r1 = [s1]

# Création d'une copie des N premiers éléments de src, appelée q1
q1 = src[:N]

# Transformation de q1 en un tas min-heap pour pouvoir accéder rapidement au plus petit élément
heapq.heapify(q1)
# Après cette opération, q1 respecte la propriété de tas (le plus petit élément est q1[0])

# Boucle sur N éléments pour traiter les éléments suivants dans src (ceux après les N premiers)
for i in range(N):
    # Ajoute le (N+i)-ième élément de src au tas q1
    heapq.heappush(q1, src[N + i])
    # 'heapq.heappush()' insère un élément dans q1 en conservant la propriété de tas

    # Retire et récupère le plus petit élément de q1
    p = heapq.heappop(q1)
    # 'heapq.heappop()' enlève le plus petit élément du tas min-heap et le retourne

    # Ajoute à r1 une nouvelle valeur qui est la somme précédente,
    # plus l'élément ajouté, moins le plus petit élément enlevé
    r1.append(r1[-1] + src[N + i] - p)
    # r1[-1] accède au dernier élément ajouté à r1

# Calcul de la somme des N derniers éléments de src, rendue négative
s2 = -sum(src[-N:])
# 'src[-N:]' sélectionne les N derniers éléments de la liste
# Le signe '-' inverse le résultat, ce sera important pour l'utilisation comme max-heap plus loin

# Création d'une liste r2 contenant s2 comme premier élément
r2 = [s2]

# Création d'une liste q2 contenant les N derniers éléments mais négativés (changement de signe)
# Ceci est un truc pour utiliser heapq (min-heap) comme un max-heap
q2 = [-a for a in src[-N:]]
# La compréhension de liste génère une nouvelle liste contenant l'opposé de chaque entité dans src[-N:]

# Transformation de q2 en tas min-heap, mais comme les éléments sont négatifs, cela simule un tas max-heap
heapq.heapify(q2)

# Cette boucle parcourt les N éléments précédant la fin de la liste src,
# en commençant juste avant les N derniers, dans l'ordre inverse
for i in range(N):
    # Ajoute un nouvel élément (négatif) au tas q2.
    # L'indice -N-i-1 part de l'élément juste avant les N derniers, et recule à chaque tour;
    # les indices sont négatifs, donc on retourne en arrière sur la liste
    heapq.heappush(q2, -src[-N - i - 1])
    # On insère l'inverse de la valeur pour continuer à simuler le comportement d'un max-heap

    # Retire et récupère le plus petit élément du tas min-heap (donc le "plus grand" initial à cause des signes)
    p = heapq.heappop(q2)

    # Ajoute à r2 une nouvelle valeur, qui est la dernière valeur ajoutée,
    # moins la nouvelle valeur ajoutée, moins l'élément retiré (toujours en accord avec la logique des signes)
    r2.append(r2[-1] - src[-N - i - 1] - p)
    # Ici, 'r2[-1]' est la dernière somme, 'src[-N - i - 1]' est l'élément effectivement considéré,
    # 'p' est négatif car q2 stocke des valeurs négatives

# Initialisation de la variable contenant la réponse maximale possible,
# on commence avec le plus petit nombre possible pour s'assurer que tout nombre réel le surpassera
ans = -float('inf')
# '-float("inf")' crée une valeur négative représentant moins l'infini

# Boucle simultanée sur les valeurs de r1 et celles de r2, mais r2 est parcouru à l'envers
# 'zip(r1, r2[::-1])' permet d'itérer sur les paires correspondantes
for a, b in zip(r1, r2[::-1]):
    # Pour chaque paire, on met à jour 'ans' si la somme de 'a' et 'b' est supérieure à la valeur actuelle de 'ans'
    ans = max(ans, a + b)
    # 'max()' retourne la valeur la plus grande entre 'ans' et 'a + b';

# Affichage de la réponse finale la plus grande trouvée dans la boucle précédente
print(ans)
# 'print()' affiche la valeur de 'ans' sur une ligne de sortie