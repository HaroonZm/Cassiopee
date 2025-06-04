import sys

# Assign shorthand variables for input/output operations for efficiency
readline = sys.stdin.readline
write = sys.stdout.write

def calc(V, es, r):
    """
    Implémente l’algorithme de l'arbre couvrant dirigé de poids minimum, aussi appelé algorithme de Chu-Liu/Edmonds.
    
    Args:
        V (int): Nombre de sommets dans le graphe.
        es (list): Liste des arêtes sous forme de tuples (source, cible, poids).
        r (int): Indice du sommet racine.
        
    Returns:
        float/int: Poids total du plus petit arbre couvrant dirigé ancré en r.
    """
    # Initialisation: pour chaque sommet, on enregistre le parent d'entrée minimal (poids, noeud source)
    mins = [(10**18, -1)] * V
    for s, t, w in es:
        # Pour chaque arête vers t, on garde la moins chère
        mins[t] = min(mins[t], (w, s))
    mins[r] = (-1, -1)  # On n'a pas besoin d'arête entrante pour la racine

    # Initialisation des tableaux pour composantes et groupes/cycles
    group = [0] * V   # Marque le groupe de chaque sommet (pour contraction)
    comp = [0] * V    # Distingue si un groupe est un cycle contracté
    cnt = 0           # Compteur de nouveaux sommets après contraction

    # Tableau indiquant si un sommet a été visité
    used = [0] * V
    for v in range(V):
        if not used[v]:
            chain = []
            cur = v
            # Suivre la chaîne d'arêtes entrantes minimales
            while cur != -1 and not used[cur]:
                chain.append(cur)
                used[cur] = 1
                cur = mins[cur][1]
            if cur != -1:
                # Un cycle est détecté
                cycle = 0
                for e in chain:
                    group[e] = cnt
                    if e == cur:
                        cycle = 1
                        comp[cnt] = 1  # Marque ce groupe comme étant un cycle
                    if not cycle:
                        cnt += 1
                if cycle:
                    cnt += 1
            else:
                # Pas de cycle, chaque sommet obtient un nouveau groupe
                for e in chain:
                    group[e] = cnt
                    cnt += 1

    if cnt == V:
        # Aucun cycle détecté, solution trouvée. Somme des poids des arêtes optimales entrantes.
        return sum(map(lambda x: x[0], mins)) + 1

    # On traite les cycles contractés
    res = sum(mins[v][0] for v in range(V) if v != r and comp[group[v]])
    
    # Création d’un nouveau graphe contracté (les cycles deviennent des super-noeuds)
    n_es = []
    for s, t, w in es:
        gs = group[s]
        gt = group[t]
        if gs == gt:
            continue  # Pas d’arêtes intra-cycle dans le graphe contracté
        if comp[gt]:
            # Pour les sommets dans un cycle, il faut soustraire le coût déjà pris en compte
            n_es.append((gs, gt, w - mins[t][0]))
        else:
            n_es.append((gs, gt, w))
    # Appel récursif sur le graphe contracté, ajoute la contribution des cycles
    return res + calc(cnt, n_es, group[r])

def solve():
    """
    Lis les données d'entrée, construit les arêtes du graphe avec les poids appropriés,
    puis lance l'algorithme pour déterminer le coût optimal.
    Écrit le résultat avec une précision de 16 décimales.
    
    Entrée attendue :
        - Un entier N (dimension des vecteurs), un entier M (nombre de vecteurs).
        - M lignes de N flottants (les vecteurs à traiter).
    
    L’arête entre deux vecteurs i et j a pour poids le carré de la distance du vecteur i à la droite générée par j.
    L’origine (vecteur nul) est indexée 0.
    """
    N, M = map(int, readline().split())
    V = []  # Liste des vecteurs non-nuls
    D = []  # Norme au carré de chaque vecteur

    # Lecture et normalisation des vecteurs, suppression des vecteurs nuls
    for i in range(M):
        Vi = list(map(float, readline().split()))
        d = sum(e ** 2 for e in Vi)
        if d <= 1e-9:  # On ignore les vecteurs quasi-nuls pour des raisons de stabilité numérique
            continue
        V.append(Vi)
        D.append(d)

    M = len(V)  # Nouveau nombre de vecteurs (après filtrage)
    E = []      # Liste des arêtes du graphe (source, destination, poids)

    # Construction du graphe complet dirigé (i=0 pour la racine/origine)
    for i in range(M):
        Vi = V[i]
        for j in range(M):
            if i == j:
                continue  # Pas d’arête d’un vecteur vers lui-même
            Vj = V[j]
            # Produit scalaire Vi·Vj
            t = 0
            for k in range(N):
                t += Vi[k] * Vj[k]
            # Projette Vi sur Vj (rapport des produits scalaires sur la norme au carré)
            r = t / D[j]
            # Calcule le carré de la distance de Vi à la droite générée par Vj
            c = 0
            for k in range(N):
                c += (Vi[k] - r * Vj[k]) ** 2
            E.append((j + 1, i + 1, c))  # Les noeuds sont indexés à partir de 1 (origine à 0)
        # Arête de l’origine (0) vers chaque vecteur avec poids égal à sa norme au carré
        E.append((0, i + 1, D[i]))
    # Calcul du coût minimal via l’algorithme de Chu-Liu/Edmonds puis affichage du résultat
    write("%.16f\n" % calc(M + 1, E, 0))

# Exécution du programme principal
solve()