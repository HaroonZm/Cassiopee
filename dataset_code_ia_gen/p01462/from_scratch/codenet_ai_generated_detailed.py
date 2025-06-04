import sys
sys.setrecursionlimit(10**7)

def main():
    # Lecture des entrées
    N, M, P = map(int, sys.stdin.readline().split())
    edges = [tuple(map(int, sys.stdin.readline().split())) for _ in range(M)]
    
    # Probabilités
    p_edge = P / 100.0      # probabilité qu'une arête disparaisse
    p_keep = 1 - p_edge     # probabilité qu'une arête reste
    
    # On veut calculer la probabilité que le graphe restant soit connecté.
    # Il y a M arêtes, chacune est indépendante.
    # Chaque arête peut être présente ou absente (modèle Bernoulli).
    # L'approche naïve est d'examiner tous les 2^M sous-graphes possibles, 
    # calculer leur probabilité, vérifier s'il est connexe et sommer ces probabilités.
    # N <= 14 et M <= 100 donc 2^M est trop grand.
    
    # On va utiliser une programmation dynamique sur les ensembles de sommets.
    # La connexion d'un graphe induit peut être représentée en fonction des arbres couvrants.
    # Cependant, les arbres couvrants sont difficiles à compter avec probabilité de disparition des arêtes.
    
    # Alternative : utilisation de la transformée de Fourier discrète pour le calcul de la probabilité, mais complexe.
    
    # Puisque N <= 14 (petit), on peut utiliser la méthode suivante:
    # - On énumère tous les sous-graphes possibles (2^M), mais cela est trop grand pour M=100.
    # - Cependant, si M est plus petit, on peut traiter.
    #
    # Il faut une méthode plus rapide.
    
    # On peut appliquer l'algorithme de "Kirchhoff's theorem / Matrix-tree theorem" modifié pour compter la probabilité que le graphe restant soit connecté.
    # En fait il existe une formule pour la fiabilité d'un réseau : 
    # reliability = somme des probabilités sur tous les sous-graphes connexe couvrant tous les sommets
    # La solution la plus directe est l'inclusion-exclusion sur les composantes connexes.
    #
    # Implémentation d'une DP cachée par l'ensemble des sommets:
    # f[S] = probabilité que l'ensemble S soit une composante connexe dans le sous-graphe restant.
    #
    # On peut construire f avec la formule de reccurence:
    # - choix d'un sommet racine r dans S
    # - considérer tous les sous-ensembles T de S avec r dans T. Si la sous-composante T est connexe et reliée au reste via des arêtes, on peut exprimer f[S].
    #
    # Pour gérer cela on peut faire un DP sur les ensembles.
    
    # Construction de la matrice d'adjacence pour accès rapide
    adj = [[False]*N for _ in range(N)]
    for v, u in edges:
        adj[v-1][u-1] = True
        adj[u-1][v-1] = True
    
    # Pour gérer rapidement les probabilités des arêtes dans un sous-ensemble,
    # on prépare un tableau edge_prob [i][j] = probabilité que l'arête (i,j) soit présente
    edge_prob = [[0.0]*N for _ in range(N)]
    for v,u in edges:
        i, j = v-1, u-1
        edge_prob[i][j] = p_keep
        edge_prob[j][i] = p_keep
    
    # Fonction pour vérifier la connectivité d'un graphe donné par un masque d'arêtes
    # Pas utilisée ici par la complexité forte.
    
    # Méthode DP sur les sous-ensembles de sommets (mask) et la connectivité
    
    # La probabilité que le graphe induit sur un ensemble de sommets S soit connecté peut être déterminée par DP:

    # f[mask] = probabilité que le sous-graphe induit par mask soit connecté
    # base: f[1<<v] = 1 pour tout v
    # relation:
    #   Pour un ensemble S > 1 élément
    #   Choisir un sommet racine r dans S
    #   f[S] = somme sur tous les sous-ensembles non vides T contenant r de (la probabilité que les arêtes entre T et S\T soient absentes) * f[T] * f[S\T]
    # mais cette forme est compliquée.
    
    # Une autre approche est la décomposition basée sur les arbres recouvrants
    
    # Comme N est petit, on peut utiliser une technique de "polynôme générateur" par décomposition basée sur les sous-ensembles.
    # Utilisation d'une technique appelée "DP sur sous-ensemble avec product over edges" (SET DP)
    
    # Pour chaque ensemble de sommets S, on veut calculer:
    # P_conn(S) = probabilité que le sous-graphe induit par S soit connexe
    
    # On effectue la récurrence suivante :
    # - si S a un seul sommet, P_conn(S)=1
    # - sinon, on choisit un sommet racine r dans S
    # - on considère toutes les partitions de S en deux sous-ensembles A et S\A avec r dans A, A non vide et différent de S
    # - P_conn(S) = somme_{A} P_conn(A) * P_conn(S\A) * probabilité qu'il n'y ait pas d'arêtes entre A et S\A (sinon S serait pas connexe)
    #   or c'est la probabilité que toutes les arêtes entre les deux ensembles soient absentes (chaque arête râte disparaît avec p ou reste avec 1-p)
    # Le problème c'est que cette formule est plutôt pour calculer la probabilité d'être déconnecté.
    # En fait, la probabilité que le graphe soit connexe = 1 - probabilité qu'il soit déconnecté.
    #
    # Usage de la décomposition par inclusion-exclusion:
    # Définissons g[S]: probabilité que le graphe induit par S soit au moins connecté (pas disconnecté)
    #
    # On peut calculer la probabilité que le graphe induit par S soit non connexe:
    # Notons que cette probabilité peut être calculée par inclusion-exclusion sur la partition en deux sous-ensembles.
    #
    # Soit Q[S] la probabilité que le sous-graphe induit par S soit **disconnexe**.
    #
    # On sait que:
    # Q[S] = somme_{A⊂S, A≠∅, A≠S} [ P_conn(A) * P_conn(S\A) * probabilité qu'aucune arête ne relie A à S\A ]
    #
    # Comme P_conn(X) = 1 - Q[X], on effectue un DP sur Q
    
    # On procède donc en DP pour Q:
    # Si |S|=1, Q[S]=0 (un seul sommet est connexe)
    # Sinon Q[S] = somme_{A⊂S avec r fixé dans A, A≠∅, A≠S}  (1 - Q[A]) * (1 - Q[S\A]) * probabilité qu'aucune arête ne relie A et S\A
    #
    # On choisit un sommet r arbitraire fixé dans S pour limiter le nombre de partitions (on ne prend que celles qui contiennent r pour éviter double comptage)
    
    # pré-calcul des probabilités d'absence d'arêtes entre deux ensembles de sommets.
    
    # Un ensemble de sommets est représenté par un entier mask (bits 0..N-1)
    
    # Calcul de la probabilité qu'il n'existe aucune arête entre A et B:
    # multiplication des (p_edge pour chaque arête entre un sommet de A et un sommet de B)
    
    # Précalcul on va stocker comme cache prob_no_edge[A][B]
    # mais trop grand O(2^N * 2^N)?
    # Nous pouvons calculer à la volée car N=14, à chaque appel on fait simplement double boucle sur les 2 ensembles
    
    from functools import lru_cache
    
    # fonction pour calculer la probabilité qu'il n'y ait pas d'arêtes entre two subsets S1 et S2
    def prob_no_edges_between(S1, S2):
        # S1 et S2 sont des masks disjoints
        # Pour chaque paire (u,v) avec u in S1, v in S2 on regarde si arête présente, sinon 1. Si arête présente, multiplier par p_edge: prob de disparition.
        # On multiplie toutes ces probabilités
        res = 1.0
        u = 0
        while u < N:
            if ((S1 >> u) & 1) == 1:
                v = 0
                while v < N:
                    if ((S2 >> v) & 1) == 1:
                        if adj[u][v]:
                            res *= p_edge
                            # optimisation si prob nul
                            if res == 0.0:
                                return 0.0
                    v += 1
            u += 1
        return res

    # Q(S) = probabilité que le sous-graphe induit par S soit pas connexe (disconnexe)
    @lru_cache(None)
    def Q(S):
        # si ensemble singleton, pas disconnexe
        if S & (S-1) == 0:
            # un seul sommet
            return 0.0
        
        # on fixe un sommet racine r = bit de poids faible de S
        r = (S & (-S)).bit_length() - 1
        
        res = 0.0
        # t parcourt tous les sous-ensembles A de S contenant r qui ne sont ni vides ni égaux à S
        # On énumère les sous-ensembles A de S tels que r in A, A != S
        A = S
        while True:
            A = (A-1) & S
            if A == 0:
                break
            if (A >> r) & 1 == 0:
                continue
            if A == S:
                continue
            # S\A
            B = S ^ A
            # on calcule la probabilité que A et B soient connexes (1 - Q(A))*(1 - Q(B)) multiplié par la probabilité qu'aucune arête ne relie A et B
            p_no_edge = prob_no_edges_between(A, B)
            term = (1 - Q(A))*(1 - Q(B))*p_no_edge
            res += term
        return res
    
    full_mask = (1 << N) - 1
    
    # La probabilité que le graphe restant soit connexe est 1 - Q(ensemble complet)
    ans = 1 - Q(full_mask)
    
    print(f"{ans:.12f}")

if __name__ == "__main__":
    main()