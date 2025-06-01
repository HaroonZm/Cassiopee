from collections import deque  # Importation de la classe deque depuis le module collections. deque est une file à double extrémité, utilisée ici pour gérer efficacement les éléments à traiter dans un ordre FIFO (First In First Out).

# Définition de la fonction Topologicalsort qui prend en entrée un entier v représentant le nombre de sommets dans un graphe.
def Topologicalsort(v):
    # Création d'une deque vide nommée start, qui va contenir les nœuds ayant un degré d'entrée nul (pas de dépendances).
    start = deque()

    # Boucle sur les indices de 0 à v-1 (les identifiants des sommets)
    for i in xrange(v):
        # Condition : si le degré d'entrée du sommet i est zéro, cela signifie qu'il n'a aucune arête entrante.
        if indeg[i] == 0:
            # Ajout du sommet i dans la deque start, ce sommet peut être traité en premier dans l'ordre topologique.
            start.append(i)

    # Vérification initiale si plusieurs sommets peuvent être traités en premier (conflit)
    if len(start) > 1:
        # Si plus d'un sommet a un degré d'entrée nul, cela signifie qu'il y a plusieurs choix possibles pour commencer, on met le flag à True.
        flag = True
    else:
        # Sinon, il n'y a qu'un seul choix possible au départ, flag est False.
        flag = False

    # Tant que la deque start n'est pas vide, c'est-à-dire qu'il reste des sommets à traiter dans l'ordre topologique.
    while len(start) > 0:
        # Extraction (retour et suppression) du premier élément (sommet) de la deque start.
        i = start.popleft()
        # Ajout du sommet i dans la liste ans qui va contenir l'ordre topologique final.
        ans.append(i)

        # Création d'une liste temporaire tmp vide, qui va stocker les sommets découverts dont le degré d'entrée vient de devenir zéro.
        tmp = []

        # Boucle sur tous les sommets j accessibles à partir du sommet i (les successeurs de i dans le graphe).
        for j in g[i]:
            # Décrémentation du degré d'entrée du sommet j, car on vient de traiter un de ses prédécesseurs.
            indeg[j] -= 1
            # Si après décrémentation le degré d'entrée de j est à zéro, cela signifie qu'il est désormais disponible pour être traité.
            if indeg[j] == 0:
                # On ajoute ce sommet j à la liste temporaire tmp.
                tmp.append(j)
                # On ajoute aussi ce sommet j à la deque start pour traitement ultérieur.
                start.append(j)
                # Si plus d'un sommet est ajouté simultanément dans tmp, cela signifie qu'il y a plusieurs choix possibles à ce niveau, on met flag à True.
                if len(tmp) > 1:
                    flag = True
    # Retourne la liste ordonnée des sommets ans correspondant à un ordre topologique, et le flag booléen indiquant s'il y avait plusieurs ordres possibles.
    return ans, flag

# Fonction solve qui prend en entrée n (nombre de sommets) et m (nombre d'arêtes).
def solve(n, m):
    # Boucle pour lire les m arêtes du graphe.
    for i in xrange(m):
        # Lecture des deux entiers wt et lt représentant une arête de wt vers lt. raw_input() lit une ligne, map convertit en int.
        wt, lt = map(int, raw_input().split())
        # Conversion des sommets de la base 1 (entrée utilisateur) à la base 0 (indexation Python).
        wt -= 1
        lt -= 1
        # Ajout du sommet lt dans la liste des successeurs du sommet wt du graphe orienté g.
        g[wt].append(lt)
        # Incrémentation du degré d'entrée (nombre d'arêtes entrantes) du sommet lt.
        indeg[lt] += 1
    # Appel à la fonction Topologicalsort pour calculer l'ordre topologique du graphe g avec n sommets.
    ans, flag = Topologicalsort(n)
    # Retourne la liste ordonnée des sommets et le flag.
    return ans, flag

# Lecture du nombre de sommets n depuis l'entrée standard.
n = int(raw_input())
# Lecture du nombre d'arêtes m depuis l'entrée standard.
m = int(raw_input())

# Initialisation d'une liste indeg de taille n remplie d'entiers 0, représentant le degré d'entrée de chaque sommet.
indeg = [0] * n

# Initialisation d'une liste g de taille n composée de listes vides, représentant une liste d'adjacence du graphe orienté.
g = [[] for _ in xrange(n)]

# Initialisation d'une liste ans vide qui contiendra l'ordre topologique final.
ans = []

# Appel de la fonction solve avec les paramètres n et m, remplissant g, indeg, et obtenant l'ordre topologique ans ainsi que le flag.
ans, flag = solve(n, m)

# Condition vérifiant si flag est True, ce qui signifie que plusieurs ordres topologiques sont possibles.
if flag:
    # Boucle pour parcourir tous les sommets indexés de 0 à n-1.
    for i in xrange(n):
        # Affichage de chaque sommet dans l'ordre trouvé, conversion de la base 0 à la base 1 pour correspondre à l'entrée originale.
        print(ans[i] + 1)
    # Impression d'un 1 pour indiquer qu'il existe plusieurs ordres topologiques possibles.
    print(1)
else:
    # Sinon, il n'y a qu'un ordre topologique unique.
    for i in xrange(n):
        # Affichage de chaque sommet dans l'ordre unique, conversion base 0 à base 1.
        print(ans[i] + 1)
    # Impression d'un 0 signifiant l'unicité de l'ordre topologique.
    print(0)