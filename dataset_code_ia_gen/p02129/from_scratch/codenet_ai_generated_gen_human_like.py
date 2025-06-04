N = int(input())
ladder = []

# Chaque amida-kuji fait passer de 3 lignes verticales à 3 lignes verticales avec des permutations
# On modélise la permutation induite par chaque amida-kuji sur les indices [0,1,2]

def get_perm(w, a):
    # positions des 3 lignes: 0,1,2
    # a[i] indique si la barre horizontale est à gauche (0) ou à droite (1) de la ligne centrale
    # le nombre de barres w_i correspond aux mouvements entre les lignes adjacentes
    # Les barres sont du haut vers le bas. On simule l'effet de chaques barres.
    pos = [0,1,2]
    # On "descend" en simulant les barres dans l'ordre
    
    # L'amida-kuji est construit avec 3 lignes, les barres horizontales s'appliquent entre les lignes
    # On traite les barres dans l'ordre, chacune correspond à un swap entre deux lignes
    # Dans ce problème, un barre étend entre la ligne centrale (index 1) et gauche (index 0) si a==0,
    # ou entre centre (1) et droite (2) si a==1, et c'est la barre jème d'en haut.
    perm = list(range(3))
    for c in a:
        if c == 0:
            # barre entre ligne 0 et 1 => swap perm[0] et perm[1]
            perm[0], perm[1] = perm[1], perm[0]
        else:
            # barre entre ligne 1 et 2 => swap perm[1] et perm[2]
            perm[1], perm[2] = perm[2], perm[1]
    return perm

permutations = []
for _ in range(N):
    data = list(map(int,input().split()))
    w = data[0]
    a = data[1:]
    permutations.append(get_perm(w,a))

# On veut concaténer une ou plusieurs amida-kujis dans un ordre quelconque
# On cherche s'il est possible d'obtenir l'identité en multipliant les permutations choisies

# Toutes ces permutations sont dans S_3 (sur 3 éléments)

# On effectue un BFS sur l'espace des permutations composées
# L'état initial est l'identité; on applique les permutations données dans n'importe quel ordre en boucle
# Et on essaie de voir si on peut retourner à l'identité après au moins une application
# On peut démarrer avec un noeud 'identité' et parcourir les groupes générés

from collections import deque

start = (0,1,2)
visited = set()
queue = deque()
queue.append(start)
visited.add(start)

while queue:
    current = queue.popleft()
    for p in permutations:
        # multiplier p par current: p après current
        # en terme de permutation de la base [0,1,2], la composition s'écrit p(current(x))
        # mais ici les listes donnent l'image de 0,1,2
        # La composition perm2 * perm1 est perm2[perm1[i]] pour i=0..2
        new_perm = tuple(p[current[i]] for i in range(3))
        if new_perm not in visited:
            visited.add(new_perm)
            queue.append(new_perm)

# On cherche dans visited de permutations qui sont l'identité
# L'identity est (0,1,2)
# Nous devons vérifier si l'identité a été atteinte après avoir utilisé au moins un amida-kuji;
# or, on a toujours dans visited l'identity, car on a commencé par là
# On doit savoir si on peut revenir à l'identity via une composition non triviale, autrement dit,
# il faut que la group générée par permutations contienne l'identité autre que celle triviale.

# Puisque on a ajouté la permut identité dès le début, on doit vérifier si on peut obtenir l'identity
# en faisant au moins un pas (i.e. qu'il y a une permutation p différente de l'identité dans la génération)

# Or si "visited" contient plus que juste la permutation identité, 
# alors en composant certaines permutations on peut faire une boucle qui revient à l'identity.

print("yes" if len(visited) > 1 else "no")