import os
import sys
from heapq import heappop, heappush
import numpy as np

def solve(n, m, field):
    """
    Résout un problème de flots à coût minimum sur une grille de taille n x m représentée sous forme aplatie 'field'.

    Args:
        n (int): Nombre de lignes de la grille.
        m (int): Nombre de colonnes de la grille.
        field (np.ndarray): Tableau aplati représentant la grille, où chaque case est codée comme int8.

    Returns:
        int: La valeur optimale calculée pour le problème sur le champ donné.
    """
    MINCOSTFLOW_LINKS = []  # Liste globale contenant les graphes pour chaque instance de problème
    INF = 10 ** 10  # Valeur utilisée pour l'infini dans la recherche de chemin

    def mincostflow_init(n):
        """
        Initialise une nouvelle instance de graphe pour le flot à coût minimum.

        Args:
            n (int): Nombre de sommets dans le graphe.

        Returns:
            int: Identifiant (index) de l'instance créée dans MINCOSTFLOW_LINKS.
        """
        lst = [[0]]
        lst.clear()  # Nettoie la liste initiale
        MINCOSTFLOW_LINKS.append([lst.copy() for _ in range(n)])  # Crée n listes d'arêtes vides
        return len(MINCOSTFLOW_LINKS) - 1

    def mincostflow_add_link(ins, frm, to, capacity, cost):
        """
        Ajoute une arête dirigée et son arête résiduelle dans le graphe de l'instance donnée.

        Args:
            ins (int): Identifiant de l'instance de graphe.
            frm (int): Sommet de départ.
            to (int): Sommet d'arrivée.
            capacity (int): Capacité de l'arête.
            cost (int): Coût de l'arête.
        """
        links = MINCOSTFLOW_LINKS[ins]
        links[frm].append([to, capacity, cost, len(links[to])])  # Forward edge
        links[to].append([frm, 0, -cost, len(links[frm]) - 1])   # Residual edge

    def mincostflow_flow(ins, s, t, quantity):
        """
        Calcule le flot à coût minimum de 'quantity' unités depuis s vers t dans le graphe de l'instance 'ins'.

        Args:
            ins (int): Identifiant de l'instance de graphe.
            s (int): Source (sommet de départ).
            t (int): Puits (sommet d'arrivée).
            quantity (int): Quantité de flot à transporter.

        Returns:
            int: Le coût total minimum du flot. Retourne -1 si impossible.
        """
        links = MINCOSTFLOW_LINKS[ins]
        n = len(links)
        res = 0  # Résultat du coût total accumulé
        # Potentiels utilisés pour l'amélioration des coûts réduits (pour Dijkstra)
        potentials = np.zeros(n, dtype=np.int64)
        # Distances pour la recherche de chemin de coût minimum
        dist = np.full(n, INF, dtype=np.int64)
        # Pour reconstituer le chemin trouvé
        prev_v = np.full(n, -1, dtype=np.int64)
        prev_e = np.full(n, -1, dtype=np.int64)

        while quantity > 0:
            dist.fill(INF)
            dist[s] = 0
            que = [(0, s)]

            # Recherche du plus court chemin (Dijkstra) avec potential pour les coûts négatifs résiduels
            while que:
                total_cost, v = heappop(que)
                if dist[v] < total_cost:
                    continue
                for i, (u, cap, cost, _) in enumerate(links[v]):
                    # Calcul du coût réduit
                    new_cost = dist[v] + potentials[v] - potentials[u] + cost
                    if cap > 0 and new_cost < dist[u]:
                        dist[u] = new_cost
                        prev_v[u] = v
                        prev_e[u] = i
                        heappush(que, (new_cost, u))

            # Si le puits ne peut pas être atteint, le flot est impossible
            if dist[t] == INF:
                return -1

            potentials += dist  # Mise à jour des potentiels pour accélérer les prochaines itérations

            # Cherche l'augmentation maximale possible sur le chemin trouvé
            cur_flow = quantity
            v = t
            while v != s:
                cur_flow = min(cur_flow, links[prev_v[v]][prev_e[v]][1])
                v = prev_v[v]
            quantity -= cur_flow
            res += cur_flow * potentials[t]

            # Met à jour les capacités sur le chemin
            v = t
            while v != s:
                link = links[prev_v[v]][prev_e[v]]
                link[1] -= cur_flow
                links[v][link[3]][1] += cur_flow
                v = prev_v[v]

        return res

    # ----- Préparation du réseau de flot -----
    nm = (n + 2) * (m + 2)  # Nombre total de cases avec un border de taille 1 autour du terrain
    m2 = m + 2               # Largeur réelle de la grille avec bordure

    # Trouve les indices des points de départ (valeur == 1 dans 'field')
    starts = np.where(field == 1)[0]
    s_size = starts.size  # Nombre de sources réelles

    # Initialisation du graphe de flot. Noeuds complémentaires pour chaque source.
    ins = mincostflow_init(nm + s_size + 2)
    s = nm + s_size      # Noeud source super
    t = s + 1            # Noeud puits super

    # Allocation d'un buffer utilisé plus loin pour la BFS rapide
    stack = np.zeros(10 ** 7, np.int64)
    SENTINEL = INF - 1   # Valeur utilisée pour calculer le coût marginal par distance

    # ----- Ajout des arêtes du graphe : des sources virtuelles à leur position -----
    for i in range(s_size):
        mincostflow_add_link(ins, s, nm + i, 1, 0)  # Source super à chaque source réelle

        stack[0] = starts[i]
        stack[1] = 0
        sl = 0       # Pointeur de début dans le stack
        sr = 2       # Pointeur de fin actif du stack
        stacked = np.zeros(nm, np.int8)  # Marqueur pour ne pas revisiter un sommet
        stacked[starts[i]] = 1

        # BFS pour construire toutes les arêtes vers les cases atteignables par chaque source
        while sl < sr:
            v = stack[sl]
            c = stack[sl + 1]
            sl += 2

            # Lien du noeud source virtuel à chaque case atteinte, avec un coût en fonction de la distance
            mincostflow_add_link(ins, nm + i, v, 1, SENTINEL - c)

            # On explore la case à droite (v + 1) si accessible et non murée
            if stacked[v + 1] == 0 and field[v + 1] != 2:
                stack[sr] = v + 1
                stack[sr + 1] = c + 1
                stacked[v + 1] = 1
                sr += 2
            # On explore la case en bas (v + m2) si accessible et non murée
            if stacked[v + m2] == 0 and field[v + m2] != 2:
                stack[sr] = v + m2
                stack[sr + 1] = c + 1
                stacked[v + m2] = 1
                sr += 2

    # ----- Connexion de toutes les cases non murées au puits -----
    for i in range(nm):
        if field[i] != 2:
            mincostflow_add_link(ins, i, t, 1, 0)

    # ----- Calcul du flot à coût minimum -----
    f = mincostflow_flow(ins, s, t, s_size)

    # On ajuste le résultat brut en enlevant la composante envoyée sur le SENTINEL
    ans = SENTINEL * s_size - f
    return ans

# Signature de la fonction pour la compilation avec Numba
SIGNATURE = '(i8,i8,i1[:],)'

# ----- Compilation dans le contexte de juge en ligne -----
if sys.argv[-1] == 'ONLINE_JUDGE':
    from numba.pycc import CC

    cc = CC('my_module')
    cc.export('solve', SIGNATURE)(solve)
    cc.compile()
    exit()

# ----- Compilation ou import natif selon le système -----
if os.name == 'posix':
    # Import du module compilé (pour Linux, MacOS)
    from my_module import solve
else:
    from numba import njit

    # Compilation à la volée de solve via Numba pour Windows
    solve = njit(SIGNATURE, cache=True)(solve)
    print('compiled', file=sys.stderr)

# ----- Lecture d'entrée, prétraitement et appel principal -----
n, m = map(int, sys.stdin.readline().split())

# On traite et convertit la grille : ajoute des bordures et encode chaque caractère
field = '#' * (m + 3) + '##'.join(sys.stdin.read().split()) + '#' * (m + 3)
field = np.fromiter(map('.o#'.index, field), np.int8)  # '.'->0, 'o'->1, '#'->2

# Appel de la fonction principale et affichage du résultat
ans = solve(n, m, field)
print(ans)