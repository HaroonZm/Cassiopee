from sys import stdin

def tree_walk_1(start, parent=None):
    """
    Construis un arbre enraciné à partir du graphe non orienté donné.

    Cette fonction remplit deux structures globales :
    - P : la liste des parents de chaque nœud dans l'arbre, avec le poids du bord les reliant.
    - C : la liste des enfants de chaque nœud avec les poids des arêtes correspondantes.

    Args:
        start (int): Le nœud courant à visiter.
        parent (int, optional): Le nœud parent du nœud courant pour éviter de remonter dans le graphe.
                                Par défaut, None pour le nœud racine.
    """
    for i, t in adj[start]:
        if i != parent:
            P[i] = (start, t)      # Enregistrer le parent et le poids de l'arête
            C[start].append((i, t)) # Ajouter l'enfant avec le poids du bord
            tree_walk_1(i, start)   # Appel récursif pour construire l'arbre du nœud enfant

def tree_walk_2(start):
    """
    Parcours l'arbre pour calculer le temps total de visite en fonction des contraintes du problème.

    Cette fonction met à jour la variable globale 'time' en cumulant les temps de déplacement.

    Algorithme:
    - Marque le nœud courant comme visité.
    - Parcourt les enfants non visités, augmente le temps en fonction des arêtes (aller-retour).
    - Après avoir visité tous les enfants, remonte vers le parent non visité, augmentant le temps par le poids de l'arête.

    Args:
        start (int): Le nœud courant en train d'être visité.
    """
    global time
    notVisited[start] = False  # Marquer le nœud courant comme visité
    for c, t1 in C[start]:     # Parcourir tous les enfants
        if notVisited[c]:
            time += 2 * t1     # Ajouter le temps aller-retour pour visiter l'enfant
            tree_walk_2(c)     # Visiter récursivement l'enfant
    p, t2 = P[start]           # Récupérer le parent et le poids de l'arête du nœud courant
    if notVisited[p]:
        time += t2             # Ajouter le temps pour remonter vers le parent
        tree_walk_2(p)         # Visiter récursivement le parent s'il n'a pas été visité

f_i = stdin

while True:
    N = int(f_i.readline())
    if N == 0:  # Condition d'arrêt de la lecture des cas
        break
    
    adj = [[] for i in range(N)]  # Liste d'adjacence pour le graphe initial non orienté
    for i in range(N - 1):
        a, b, t = map(int, f_i.readline().split())
        a -= 1  # Passage à l'indexation 0
        b -= 1
        adj[a].append((b, t))  # Ajouter l'arête a-b avec poids t
        adj[b].append((a, t))  # Ajouter l'arête b-a avec poids t
    
    # Suppression des feuilles attachées au nœud 0 (index 0)
    lf = []
    for i, a in enumerate(adj[1:], start=1):
        if len(a) == 1:    # Si le nœud est une feuille (une seule connexion)
            lf.append(i)
    for l in lf:
        i, t = adj[l].pop()     # Récupérer l'unique bord pour la feuille
        adj[i].remove((l, t))   # Enlever la feuille de la liste d'adjacence de son parent
    
    # Identification des candidats racines (feuilles restantes à partir du nœud 1)
    rc = [i for i, a in enumerate(adj[1:], start=1) if len(a) == 1]
    if not rc:  # Si aucun candidat racine n'existe, le temps est nul car pas de chemin à parcourir
        print(0)
        continue
    
    time_rec = []
    for r in rc:
        P = [None] * N            # Liste des parents avec poids, à initialiser pour chaque racine candidate
        P[r] = (r, 0)            # Définition du parent de la racine comme elle-même avec poids 0
        C = [[] for i in range(N)]  # Liste des enfants par nœud dans l'arbre enraciné
        
        tree_walk_1(r)           # Construction de l'arbre enraciné à partir de r
        
        time = 0                 # Initialisation du temps total pour ce parcours
        notVisited = [True] * N  # Marquage des nœuds non visités
        tree_walk_2(0)           # Calcul du temps de visite à partir du nœud 0
        
        time_rec.append(time)    # Enregistrer le temps total de ce parcours
    
    print(min(time_rec))          # Afficher le temps minimal obtenu parmi les racines candidates