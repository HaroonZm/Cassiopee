import sys  # Importation du module sys pour accéder à stdin (entrée standard)

# On définit 'read' comme un alias pour la méthode 'read' du buffer de l'entrée standard, ce qui permet de lire tout le flux d'entrée standard sous forme de bytes d'un coup.
read = sys.stdin.buffer.read

# On définit 'readline' comme un alias pour la méthode 'readline' du buffer d'entrée standard, ce qui permet de lire une seule ligne à partir de l'entrée standard, comme bytes.
readline = sys.stdin.buffer.readline

# On définit 'readlines' comme un alias pour la méthode 'readlines' du buffer d'entrée standard, ce qui permet de lire toutes les lignes d'entrée standard restantes, sous forme d'une liste de bytes.
readlines = sys.stdin.buffer.readlines

"""
Le code traite d'un graphe en pseudo-arbre, avec quelques faits importants :
- Chaque sommet a un degré entrant (in-degree) égal à 1 (sauf peut-être le sommet initial),
- Cela garantit l'existence d'un unique cycle orienté,
- Une fois le choix pour un sommet du cycle fixé, tous les états sont alors déterminés.
"""

# Lecture du nombre de sommets, auquel on applique int() pour convertir la ligne de bytes en entier. readline() lit une ligne (bytes) contenant ce nombre.
N = int(readline())

# On lit l'entrée restante (read renvoie tous les bytes restants), puis split() sépare sur les espaces pour produire une liste de bytes, que map(int, ...) convertit en entiers.
# On ajoute un 0 en première position car le parent de la racine n'existe pas, ça permet de gérer l'indexation des sommets à partir de 1.
parent = [0] + list(map(int, read().split()))

# Création d'une liste vide pour les enfants de chaque sommet, pour chaque sommet de 0 à N inclus (donc N+1 au total).
child = [[] for _ in range(N + 1)]

# Remplissage de la structure enfant à partir de la liste 'parent'.
# enumerate(parent) génère les couples (indice, valeur) pour chaque élément de 'parent'.
# Pour chaque sommet 'i', on ajoute 'i' à la liste d'enfants du sommet parent 'x'.
for i, x in enumerate(parent):
    child[x].append(i)

# On crée une liste out_deg qui contient, pour chaque sommet, le nombre d'enfants (i.e. le degré sortant du sommet) ; len(x) pour chaque liste d'enfants x.
out_deg = [len(x) for x in child]

# A ce stade, 'child' est une liste où child[p] est la liste des enfants du sommet p, tandis que out_deg[p] en est la longueur (nombre d'enfants).

# On prépare une liste G qui contiendra le nombre de Grundy pour chacun des sommets.
# Elle est initialisée à -1 pour chaque sommet, pour indiquer qu'aucune valeur n'a encore été calculée pour ces sommets.
G = [-1] * (N + 1)

# Traitement initial : on s'occupe de tous les sommets qui ne sont pas dans le cycle (i.e. les sommets feuille).
# On va itérativement retirer les sommets dont le degré sortant (out_deg) est nul (des feuilles), et on propage la réduction du degré sortant à leur parent.
# On prépare une pile avec tous les indices (sommets) i tels que out_deg[i] vaut 0 (ils n'ont pas d'enfants).
stack = [i for i, x in enumerate(out_deg) if not x]

# On traite la pile jusqu'à ce qu'elle soit vide.
while stack:
    x = stack.pop()  # On enlève et récupère le dernier sommet ajouté à la pile (qui a un out_deg 0).
    # On construit l'ensemble 'se' contenant les Grundy des enfants de x (G[c] pour chaque c dans child[x]).
    se = set(G[c] for c in child[x])  # Typiquement, les enfants ont déjà été évalués.
    # Calcul du mex (minimum excludant) : on choisit le plus petit entier non négatif qui n'est pas dans 'se'.
    g = 0  # On commence à tester pour 0.
    while g in se:
        g += 1  # On incrémente tant que g est dans 'se'.
    G[x] = g  # On affecte la valeur mex trouvée comme Grundy du sommet x.
    # On réduit le degré sortant du parent de x, car on va considérer x comme retiré : il ne sera plus l'enfant de son parent.
    p = parent[x]
    out_deg[p] -= 1  # On enlève 1 au out_deg du parent.
    # Si ce parent n'a maintenant plus d'enfants (out_deg == 0), on l'ajoute à la pile pour le traiter à son tour.
    if not out_deg[p]:
        stack.append(p)

"""
On sait que les valeurs possibles de Grundy sur le cycle sont au plus 2.
On fixe arbitrairement l'une d'elles et on recalculera la suite, et la stabilité du cycle nous indiquera si tout est cohérent.
"""

# On cherche le sommet où il reste un arête sortante (il y en aura exactement autant que la taille du cycle), pour trouver un point de départ pour le cycle.
# enumerate(out_deg[1:], 1) permet de parcourir les sommets 1 à N avec leurs degrés sortants.
for i, x in enumerate(out_deg[1:], 1):
    if x == 1:
        root = i  # On garde le premier sommet du cycle rencontré.
        break  # On sort immédiatement après l'avoir trouvé, il ne peut y en avoir qu'un unique composant cyclique.

# La longueur du cycle est le nombre de sommets dont le out_deg reste égal à 1 (chaque sommet du cycle a un unique successeur dans ce contexte).
cycle_len = sum(out_deg[1:])  # Somme des out_deg pour les sommets 1 à N, chaque sommet du cycle compte pour 1.

# On va vérifier si le Grundy des sommets du cycle devient stable après quelques tours sur ce cycle.
is_stable = False  # On commence par postuler qu'il n'y a pas de stabilité.

x = root  # On initialise le parcours du cycle avec le sommet 'root'.
# On va effectuer assez de tours pour garantir la convergence : on fait 2 * cycle_len + 10 tours (plus qu'il n'en faut : c'est un cycle de taille cycle_len).
for _ in range(cycle_len * 2 + 10):
    # On rassemble l'ensemble de tous les Grundy des enfants directs du sommet x.
    se = set(G[c] for c in child[x])
    # Calcul du mex, comme précédemment : la plus petite valeur naturelle non présente parmi les Grundy des enfants.
    g = 0
    while g in se:
        g += 1
    # Si le nouveau Grundy calculé pour x est égal à sa valeur précédente, le cycle est stable (fixpoint) :
    if g == G[x]:
        is_stable = True
        break  # On peut sortir car tout est déterminé.
    G[x] = g  # Sinon, on met à jour la valeur.
    x = parent[x]  # On remonte au parent, ce qui sur le cycle fait le tour du cycle.

# Selon si on a atteint une situation stable, la réponse est 'POSSIBLE' ou 'IMPOSSIBLE' ;
# On affiche le résultat.
answer = 'POSSIBLE' if is_stable else 'IMPOSSIBLE'
print(answer)  # Affichage final du résultat sur la sortie standard.