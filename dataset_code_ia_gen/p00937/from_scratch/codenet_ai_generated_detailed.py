from collections import deque

# On modélise le problème comme un jeu à plusieurs étapes sur un graphe orienté.
# Chaque "état" est un cercle (noeud). Le mouvement possible en un tour est de 
# faire exactement k pas sur les arêtes, avec k ∈ {a,b,c}.
# On veut trouver le nombre minimum de tours pour garantir d'atteindre le but peu
# importe les choix adverses, ou détecter qu'il est impossible d'y parvenir.

def main():
    n, m, a, b, c = map(int, input().split())
    graph = [[] for _ in range(n+1)]
    
    for _ in range(m):
        u, v = map(int, input().split())
        graph[u].append(v)
    
    # On va créer des graphes dérivés représentant les transitions possibles
    # en un nombre donné de pas
    # Pour chaque longueur k dans {a,b,c}, on construit un graphe "k-step" où il y a une arête
    # entre u et v s'il existe un chemin de longueur k dans le graphe original.
    # Pour cela, on fait une recherche BFS allongée en k étapes à partir de chaque noeud.
    
    def build_k_step_graph(k):
        kstep_graph = [[] for _ in range(n+1)]
        for start in range(1, n+1):
            # BFS pour trouver les noeuds accessibles en exactement k étapes depuis start
            queue = deque()
            queue.append((start, 0))
            visited = [False]*(n+1)
            # Mais on doit distinguer les états selon la profondeur, donc on mémorise (node, step)
            visited_steps = [[False]*(k+1) for _ in range(n+1)]
            visited_steps[start][0] = True
            
            while queue:
                node, step = queue.popleft()
                if step == k:
                    # ajout d'une arête "k-step" de start à node
                    if node != start:  # éviter boucle inutile dans ce graphe (mais pas obligatoire)
                        kstep_graph[start].append(node)
                    continue
                for nxt in graph[node]:
                    if not visited_steps[nxt][step+1]:
                        visited_steps[nxt][step+1] = True
                        queue.append((nxt, step+1))
        return kstep_graph

    # Construction des trois graphes à 1, 2, ... pas etc.
    # Ici on a seulement trois longueurs a,b,c
    sets = [a,b,c]
    kstep_graphs = [build_k_step_graph(k) for k in sets]

    # Maintenant on modélise le jeu de façon inversée:
    # État du jeu : cercle courant où l'on se trouve au début d'un tour.
    # On veut minimiser le nb de tours pour atteindre le but n quel que soit le choix adverse.

    # On définira dp[node] = nombre minimum de tours nécessaires pour atteindre n depuis node,
    # si on peut forcer la victoire. Sinon, dp[node] = inf ou marqueur impossible

    INF = 10**9
    dp = [INF]*(n+1)
    dp[n] = 0  # On est déjà au but, donc 0 tours nécessaires

    # On utilise une approche de programmation dynamique par ordre inverse,
    # on met à jour une valeur pour un noeud s'il existe une stratégie pour lequel
    # pour tous les choix adverses (i.e. tous les kstep_graphs),
    # on peut aller vers un noeud avec dp < inf en une étape.

    # C'est un problème classique de résolution de jeu alterné :
    # On fixe dp[n] = 0, puis on boucle jusqu'à convergence.

    changed = True
    while changed:
        changed = False
        for node in range(1, n+1):
            if node == n: continue
            # On veut vérifier si on peut garantir finir
            # Cela signifie: pour T = 1 + max_{for adversary's choice k} min_{next nodes after k steps} dp[next]
            # En d'autres termes, on doit pouvoir pour chaque choix de k (a,b,c)
            # atteindre un noeud avec dp[next] fini, sinon l'adversaire choisira ce k
            # donc on doit considérer "max sur k des min dp des noeuds accessibles en k pas"
            # Pour gagner, ce max doit être fini => pour chaque k, on doit pouvoir aller en un noeud "bon"
            # en k pas.

            # Pour chaque k-step graph, on regarde tous les prochains noeuds accessibles en k pas:
            # si aucun noeud accessible n'a dp[next] < INF -> perdu pour ce k choice.

            max_min = -1  # max des min de dp[next] sur chaque choix k
            possible = True
            max_over_choices = -1

            for g in kstep_graphs:
                next_nodes = g[node]
                # Si pas d'arêtes, on perd (car on doit faire exactement k pas)
                if not next_nodes:
                    # Cela signifie qu'avec cette longueur, on est bloqué => adversaire peut forcer défaite
                    possible = False
                    break
                # Min dp[next] parmi next_nodes
                min_dp_next = INF
                for nxt in next_nodes:
                    if dp[nxt] < min_dp_next:
                        min_dp_next = dp[nxt]
                if min_dp_next == INF:
                    # Aucune ligne d'attaque gagnante pour ce choix k
                    possible = False
                    break
                # Sinon on garde max sur ces min dp[next]
                if min_dp_next > max_over_choices:
                    max_over_choices = min_dp_next
            
            if possible:
                # T = 1 + max_over_choices
                candidate = 1 + max_over_choices
                if candidate < dp[node]:
                    dp[node] = candidate
                    changed = True
            # sinon pas de victoire possible à partir de node
    
    # Résultat
    if dp[1] == INF:
        print("IMPOSSIBLE")
    else:
        print(dp[1])

if __name__ == "__main__":
    main()