import sys

# Raccourcis pour la lecture de l'entrée pour plus d'efficacité
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

# Lecture de n (nombre de sommets) et m (nombre d'arêtes)
n, m = map(int, readline().split())

# Lecture des u, v, s successifs (les arêtes et la "somme" imposée entre deux sommets)
uvs = list(map(int, read().split()))

# Construction de la liste d'adjacence sous forme de dictionnaire pour chaque sommet,
# où links[u][v] = s  <=> l'arête (u, v) doit vérifier nums[u] + nums[v] = s
links = [dict() for _ in range(n+1)]
it = iter(uvs)
for u, v, s in zip(it, it, it):
    links[u][v] = s
    links[v][u] = s  # Graphe non orienté

def dfs(root, init):
    """
    Effectue un parcours DFS pour essayer d'attribuer des valeurs nums[x] aux nœuds,
    telles que pour chaque arête (u, v, s), nums[u] + nums[v] == s.
    
    Si un conflit est trouvé dans un cycle pair, le système n'a pas de solution (print(0) et exit).
    Pour un cycle impair, tente de résoudre et réessayez avec une nouvelle racine. 
    
    Args:
        root (int): Le sommet d'où partir la DFS.
        init (int): La valeur à assigner à nums[root].
            
    Returns:
        tuple: 
            - (True, nums, depth, 0, 0) si le DFS s'est bien passé;
            - (False, nums, depth, start, val) si une aberration rattrapable dans un cycle impair a été trouvée,
              on retourne la racine du cycle et la valeur imposée.
    """
    nums = [0] * (n+1)      # nums[i] = valeur assignée au sommet i
    depth = [-1] * (n+1)    # depth[i] = profondeur du sommet i dans l'arbre DFS
    parent = [-1] * (n+1)   # parent[i] = parent de i dans l'arbre DFS

    nums[root] = init
    depth[root] = 0
    stack = [root]          # Utilisation d'une pile pour le DFS

    while stack:
        next_stack = []
        while stack:
            i = stack.pop()
            for j, s_ij in links[i].items():
                if j == parent[i]:
                    continue  # Ne pas revenir vers le parent immédiat
                # Déduire nums[j] via l'équation : nums[i] + nums[j] = s_ij
                num_j = s_ij - nums[i]
                if depth[j] != -1:
                    # Détecte un cycle
                    # Deux façons possibles d'arriver à j, il faut que nums[j] soit consistant
                    if nums[j] != num_j:
                        # Conflit détecté, déterminons le type de cycle
                        loop_len = depth[j] + depth[i] + 1
                        if loop_len % 2 == 0:
                            # Cycle pair : pas de solution possible
                            print(0)
                            exit()
                        else:
                            # Cycle impair : essayons d'ajuster la solution
                            num_j_sum = nums[j] + num_j
                            if num_j_sum % 2 == 1:
                                # Impossible d'obtenir une solution entière
                                print(0)
                                exit()
                            return (False, nums, depth, j, num_j_sum // 2)
                elif depth[j] == -1:
                    # Première visite de ce sommet
                    depth[j] = depth[i] + 1
                    nums[j] = num_j
                    parent[j] = i
                    next_stack.append(j)
        stack = next_stack[:]

    # Fin du DFS sans conflits
    return (True, nums, depth, 0, 0)

# Premier passage DFS depuis le sommet 1 avec valeur initiale 0
flag, nums, depth, root, init = dfs(1, 0)

if flag == False:
    # Un cycle impair a été détecté, on réessaye avec la contrainte imposée
    flag2, nums, depth, root, init = dfs(root, init)
    if flag2 == False:
        # Encore bloqué ! (cycle impair multiple incompatible)
        print(0)
    else:
        # Vérification que toutes les valeurs sont positives
        if min(nums[1:]) < 1:
            print(0)
        else:
            print(1)
    exit()

# Séparation des sommets selon la parité de leur profondeur
even = []
odd = []
for i in range(1, n+1):
    if depth[i] % 2 == 0:
        even.append(nums[i])
    else:
        odd.append(nums[i])

# Calcul du minimum sur chaque groupe (paire/impair)
min0 = min(even)
min1 = min(odd)

# Cherche le nombre de solutions entières positives possibles (voir énoncé de la tâche)
# Pour chaque valeur t dans [1, min0] possible sur nums[paire] = t, il existe une correspondance sur nums[impair] = t'
ans = 1 + (min0 - 1) + (min1 - 1)
print(max(0, ans))