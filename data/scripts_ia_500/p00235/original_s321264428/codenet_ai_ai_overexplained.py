def tree_walk_1(start, parent=None):
    # Fonction récursive qui parcourt les sommets d'un arbre à partir d'un nœud 'start'.
    # 'parent' est le nœud précédent pour éviter de revenir en arrière.
    # La fonction construit deux structures globales P et C :
    # P[i] stocke le parent du nœud 'i' et la valeur 't' associée à l'arête entre parent et i.
    # C[start] stocke une liste des fils directs de 'start' sous forme de tuples (noeud_enfant, t).
    
    # 'adj' est une liste d'adjacences globale contenant pour chaque nœud une liste des voisins sous forme (voisin, t)
    # On itère sur tous les voisins (i, t) de 'start' dans la liste adj[start].
    for i, t in adj[start]:
        # Pour éviter de revenir en arrière vers le parent, on ignore l'itération si i est le parent.
        if i != parent:
            # On enregistre que le parent de i est 'start' avec le poids t.
            P[i] = (start, t)
            # On ajoute i dans la liste des enfants de 'start' avec la valeur t.
            C[start].append((i, t))
            # Appel récursif sur l'enfant i en précisant que le parent est 'start'.
            tree_walk_1(i, start)

def tree_walk_2(start):
    # Fonction récursive qui visite les nœuds en partant du nœud 'start'
    # et calcule le temps total accumulé suivant certaines règles.
    # 'time' est une variable globale qui accumule la somme des temps.
    # 'notVisited' est une liste globale de booléens indiquant si le nœud a été visité.
    
    global time
    # Marquer le nœud courant comme visité.
    notVisited[start] = False
    # On itère sur les enfants directs du nœud 'start', ils sont stockés dans C[start].
    # Chaque élément est un tuple (c, t1) où c est l'enfant et t1 la valeur liée.
    for c, t1 in C[start]:
        # Si l'enfant n'a pas encore été visité, on le visite.
        if notVisited[c]:
            # Augmente le temps global (deux fois le poids t1) avant d'appeler récursivement le sous-arbre.
            time += 2 * t1
            # Appel récursif sur l'enfant c.
            tree_walk_2(c)
    # Une fois les enfants traités, on remonte vers le parent.
    p, t2 = P[start]  # on récupère le parent p et la valeur t2
    # Si le parent n'a pas encore été visité, on l'explore en augmentant le temps avec t2.
    if notVisited[p]:
        time += t2
        tree_walk_2(p)

from sys import stdin
# 'stdin' représente le flux d'entrée standard.
f_i = stdin  # On attribue stdin à la variable f_i pour plus de commodité.

while True:
    # Lecture d'une ligne entière puis conversion en int, correspondant au nombre de nœuds N.
    N = int(f_i.readline())
    # Condition de fin de boucle lorsque N vaut 0.
    if N == 0:
        break
    
    # Création d'une liste d'adjacence vide pour chaque nœud, initialisée à des listes vides.
    adj = [[] for i in range(N)]
    # Lecture des N-1 arêtes décrivant l'arbre: chaque arête est ligne contenant a, b, t.
    for i in range(N - 1):
        # Lecture et conversion immédiate des trois entiers.
        a, b, t = map(int, f_i.readline().split())
        # Décrémentation par 1 pour que les indices soient basés sur 0 (de 1-based à 0-based).
        a -= 1
        b -= 1
        # Ajout des voisins dans les listes d'adjacence pour chaque extrémité (graphe non orienté).
        adj[a].append((b, t))
        adj[b].append((a, t))
    
    # Phase de suppression des feuilles adjacentes au nœud 1 (indice 1).
    # 'lf' va contenir les indices des feuilles connectées au nœud 1.
    lf = []
    # On parcourt la liste d'adjacence des nœuds à partir du deuxième nœud (indice 1 et suivants).
    for i, a in enumerate(adj[1:], start=1):
        # Un nœud est une feuille s'il a exactement un voisin.
        if len(a) == 1:
            lf.append(i)
    # Pour chaque feuille identifiée dans lf, on retire l'arête correspondante.
    for l in lf:
        # On récupère l'unique voisin i et l'arête t.
        i, t = adj[l].pop()
        # Puis on supprime la référence inverse de l'adjacence dans adj[i].
        adj[i].remove((l, t))
    
    # Recherche des candidats pour racine qui sont des nœuds feuilles dans la liste avec indice à partir de 1.
    rc = [i for i, a in enumerate(adj[1:], start=1) if len(a) == 1]
    # Si aucun nœud feuille n'existe dans la partie considérée, on affiche 0 et passe à l'itération suivante.
    if not rc:
        print(0)
        continue
    
    # Liste pour stocker les temps calculés pour chaque racine candidate.
    time_rec = []
    # Pour chaque racine candidate, on effectue un parcours et calcul du temps.
    for r in rc:
        # Initialisation de la liste P avec None pour tous les nœuds (stockage des parents).
        P = [None] * N
        # Le parent de la racine est elle-même, poids 0.
        P[r] = (r, 0)
        # Initialisation d'une liste C vide pour stocker les enfants de chaque nœud.
        C = [[] for i in range(N)]
        # Construction de l'arbre à partir de la racine r.
        tree_walk_1(r)  # appel récursif, remplit P et C.
        
        # Initialisation du temps à 0 avant le second parcours.
        time = 0
        # Tableau de marquage des nœuds non visités (True pour non visité).
        notVisited = [True] * N
        # Lancement du second parcours à partir du nœud 0 (indice 0).
        tree_walk_2(0)
        # On ajoute le temps total calculé pour cette racine candidate.
        time_rec.append(time)
    
    # Affichage du temps minimum parmi tous les candidats trouvés.
    print(min(time_rec))