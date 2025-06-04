from heapq import heappush, heappop

while True:
    # Lecture des paramètres principaux : nombre d'arêtes (n), nombre de points spéciaux (m), et capacité maximale (cap)
    n, m, cap = map(int, raw_input().split())
    # Cas d'arrêt : si n vaut 0, on termine la boucle principale
    if n == 0:
        break

    # Lecture des noms du sommet de départ (src) et d'arrivée (dest)
    src, dest = raw_input().split()

    # Construction du graphe initial G sous forme de dictionnaire d'adjacence
    G = {}
    for i in xrange(n):
        c1, c2, d = raw_input().split()
        d = int(d)  # Conversion de la distance en entier
        # Ajout de l'arête entre c1 et c2 avec poids d (pour les deux sens)
        G.setdefault(c1, {})[c2] = d
        G.setdefault(c2, {})[c1] = d

    # Construction de l'ensemble S contenant les 'm' sommets spéciaux + src et dest
    S = {raw_input() for i in xrange(m)} | {src, dest}

    INF = 10 ** 18  # Valeur utilisée pour représenter l'infini
    cap *= 10       # Multiplication de la capacité par 10 selon l'énoncé

    def dijkstra(s, G):
        """
        Algorithme de Dijkstra pour trouver les plus courts chemins depuis un sommet source.

        Args:
            s (str): sommet source à partir duquel lancer Dijkstra.
            G (dict): dictionnaire d'adjacence du graphe, {noeud: {voisin: cout, ...}, ...}

        Returns:
            dict: dictionnaire contenant les coûts minimaux depuis 's' jusqu'à tous les autres sommets atteignables.
        """
        dist = {s: 0}        # initialisation : distance depuis 's' jusque lui-même est 0
        que = [(0, s)]       # initialisation de la file de priorité avec la source

        while que:
            co, v = heappop(que)  # extrait le sommet de coût minimal
            # Ignore s'il a déjà une meilleure distance enregistrée
            if dist.get(v, INF) < co:
                continue
            # Itère sur les voisins du sommet courant
            for t, cost in G[v].items():
                # Si un chemin plus court est trouvé, mise à jour et ajout dans la file
                if co + cost < dist.get(t, INF):
                    dist[t] = co + cost
                    heappush(que, (co + cost, t))
        return dist

    # Construction du graphe intermédiaire H ne reliant que les sommets de S selon les contraintes de cap
    H = {}
    for s in S:
        # Pour chaque sommet spécial, on récupère les plus courts chemins vers tous les autres sommets
        dist = dijkstra(s, G)
        for k, v in dist.items():
            # On ne considère que les chemins entre éléments de S et de longueur <= cap
            if k in S and v <= cap:
                H.setdefault(s, {})[k] = v

    # Calcul du plus court chemin dans le graphe réduit H (entre src et dest uniquement via S)
    dist = dijkstra(src, H)
    # Affichage du résultat final : distance minimale entre src et dest selon contraintes, -1 si inatteignable
    print dist.get(dest, -1)