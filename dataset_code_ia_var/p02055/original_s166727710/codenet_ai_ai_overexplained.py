import sys

# Prend deux entiers N et R à partir de l'entrée standard (typiquement l'utilisateur)
# input().split() sépare la ligne entrée par l'utilisateur selon les espaces
# map(int, ...) convertit chaque morceau (string) en entier
N, R = map(int, input().split())

# Si deux fois R est strictement plus grand que N, alors cela veut dire que choisir R ou N-R éléments est équivalent,
# donc on prend la plus petite valeur; cela force R à être au plus la moitié de N
if 2 * R > N:
    R = N - R

# Lis une seconde ligne d'entrée utilisateur, considérée comme une permutation de taille N.
# On convertit chaque élément en entier. On met un 0 au début pour que la permutation P soit 1-indexée,
# c'est-à-dire que l'élément de P d'indice 1 sera le premier (cela simplifie le raisonnement sur les permutations)
P = [0] + list(map(int, input().split()))

# Initialise une liste vide L qui va contenir la taille de chaque cycle détecté dans la permutation
L = []

# 'used' est une liste de booléens, initialisée à False. Elle enregistre pour chaque position si cet élément a déjà
# été visité dans le parcours des cycles ou non. Sa taille est N+1 car on ne se sert pas de l'indice 0 (à cause de la 1-indexation de P)
used = [False] * (N + 1)

# 'pre' est initialisé à 0, mais n'est jamais utilisé par la suite (il est donc superfétatoire ici)
pre = 0

# On parcourt chaque position possible dans la permutation, de 1 à N inclus.
for i in range(1, N + 1):
    cnt = 0  # Compteur qui va compter la longueur du cycle courant
    # On utilise une boucle while pour visiter un cycle à partir de la position i
    while not used[i]:
        # On marque l'élément courant comme déjà visité pour ne pas compter plusieurs fois le même cycle
        used[i] = True
        cnt += 1  # On augmente la taille du cycle courant
        i = P[i]  # On avance dans le cycle en allant à la position indiquée par P[i]
    # Une fois le cycle terminé (quand on tombe sur un déjà visité),
    # si la longueur cnt du cycle est non-nulle, on l'ajoute à L
    if cnt:
        L.append(cnt)

# On crée une table (liste d'entiers) de taille N+1 qui va compter le nombre de cycles de chaque taille possible.
# table[l] va contenir le nombre de cycles de longueur l
table = [0] * (N + 1)

# Pour chaque taille de cycle trouvée dans L, on incrémente le compteur correspondant dans table
for l in L:
    table[l] += 1

# On ré-initialise L à la liste vide pour s'en resservir ensuite
L = []

# On parcourt toutes les tailles possibles de cycle, en commençant par les plus grandes
# i varie de N//2 (la division entière) jusqu'à 1, en décrémentant de 1 à chaque fois
for i in range(N // 2, 0, -1):
    x = table[i]  # x est le nombre de cycles de taille i
    if not x:
        continue  # S'il n'y a pas de cycle de cette taille, on passe à l'itération suivante
    if x == 1:
        L.append(i)  # S'il n'y a qu'un seul cycle de taille i, on ajoute simplement i à L
    else:
        p = 1  # p commence à 1 et va doubler à chaque fois
        # Tant que le double de p reste inférieur ou égal à x, on ajoute p*i et double p
        while p + p <= x:
            L.append(p * i)  # On ajoute p fois i à L
            p = p + p  # On double p
        # Après la boucle, on ajoute le reste : si x - p + 1 est non nul, on ajoute ce nombre fois i à L
        if x - p + 1:
            L.append(i * (x - p + 1))

# À ce stade, L contient des tailles de cycles (ou de "lots" de cycles regroupés) 
# On ne garde que ceux dont la taille est inférieure ou égale à R (notre contrainte de sélection)
L = [l for l in L if l <= R]

# On trie L en ordre croissant (ça aide l'étape du masque binaire à la fin)
L.sort()

# On va préparer un masque binaire pour résoudre un problème de somme exacte (subset sum).
# H est le masque, on l'initialise à 1, ce qui signifie que la somme 0 est "atteignable"
H = 1

# Pour chaque longueur l possible dans L, on met à jour le masque binaire H :
# L'opération (H << l) décale tous les bits de H vers la gauche de l positions,
# et le "or" (|) entre H et ce décalage simule l'ajout de cet élément à tous les sous-ensembles déjà considérés,
# ce qui est la technique classique du subset-sum avec un masque binaire.
for l in L:
    H = H | (H << l)

# Le test final vérifie si, dans le masque binaire H, le bit correspondant à la valeur R est à 1.
# Cela signifie qu'il est possible, en utilisant des combinaisons des longueurs collectées dans L, 
# de faire une somme exacte de R (c'est-à-dire sélectionner exactement R éléments dans les cycles trouvés).
if H & (1 << R):
    print('Yes')  # Si c'est possible, on affiche Yes
else:
    print('No')   # Sinon, on affiche No