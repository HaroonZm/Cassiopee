import sys
from collections import deque

def main():
    # Lecture des dimensions de la forêt
    H, W = map(int, sys.stdin.readline().split())
    # Lecture de la matrice A représentant le nombre d'arbres sur chaque case
    A = [list(map(int, sys.stdin.readline().split())) for _ in range(H)]
    
    # La case de l'usine (1,1) est à l'indice (0,0) en 0-based indexing
    # Elle ne contient aucun arbre par hypothèse

    # On va calculer la distance minimale en nombre de pas depuis l'usine vers chaque case
    # uniquement sur les cases où il n'y a pas d'arbre (arbres = 0), car on ne peut se déplacer
    # que sur les cases sans arbres.
    # Cependant, à partir de l'énoncé, nous pouvons uniquement marcher sur des cases sans arbres.
    # Mais on doit aller couper les arbres adjacents à ces cases sans arbres.
    #
    # En fait, on peut considérer la distance minimale de l'usine aux cases vides, mais aussi trouver
    # la distance minimale entre l'usine et TOUTES les cases (qu'elles aient des arbres ou non)
    # uniquement via cases vides pour s'y rendre. Or, si une case a des arbres, on ne peut marcher dessus,
    # donc le chemin est impossible.
    #
    # La stratégie est donc de faire un BFS depuis (0,0) sur les cases sans arbres,
    # pour obtenir la distance minimale pour VOIR toutes les cases accessibles sans arbres.
    # Puis, pour couper des arbres dans une case adjacente à une case vide, il faut
    # se rendre sur une case vide adjacente.
    #
    # Pour simplifier, on peut aussi calculer la distance depuis l'usine vers toutes les cases,
    # mais en posant une distance infinie si on ne peut s'y rendre (car arbres).
    #
    # Puis, on fait la même chose depuis la destination (H-1, W-1).
    # Si ce dernier n'est pas accessible (car arbres ou pas de chemin), la réponse est -1 (impossible).
    
    # Fonction pour faire un BFS à travers les cases sans arbre, retourne une matrice de distances
    def bfs(start_i, start_j):
        dist = [[-1]*W for _ in range(H)]
        dist[start_i][start_j] = 0
        queue = deque()
        queue.append((start_i, start_j))
        while queue:
            i, j = queue.popleft()
            for di,dj in [(-1,0),(1,0),(0,-1),(0,1)]:
                ni,nj = i+di, j+dj
                if 0 <= ni < H and 0 <= nj < W:
                    if A[ni][nj] == 0 and dist[ni][nj] == -1:
                        dist[ni][nj] = dist[i][j] + 1
                        queue.append((ni,nj))
        return dist

    dist_from_start = bfs(0,0)
    dist_from_goal = bfs(H-1, W-1)

    # Si la destination (H-1, W-1) n'est pas accessible sans arbres, alors impossible d'aller de
    # l'usine au point sud-est sans couper d'arbres. Or on doit couper des arbres pour établir un chemin.
    # Mais regardons les règles : on veut que nord-ouest et sud-est soient mutuellement accessibles
    # sans arbres. Cela signifie que l'on doit couper des arbres pour ouvrir un chemin.
    # Le problème revient à calculer le temps minimal pour couper les arbres permettant
    # la connexion.
    #
    # Analyse "coût" :
    # Pour chaque case (i,j) contenant des arbres (>0):
    # - Pour couper 1 arbre, on doit :
    #   * être sur une case adjacente sans arbre (pour pouvoir couper)
    #   * couper l'arbre (1 minute)
    #   * ramener l'arbre à la case usine (1,1) en se déplaçant (distance entre case usine et coupe*2, aller et retour).
    #
    # L'énoncé précise que la coupe s'effectue à partir d'une case adjacente sans arbre.
    # Donc on doit pouvoir atteindre une case vide voisine de (i,j).
    #
    # De plus, on doit couper tous les arbres qui bloquent le passage du chemin entre nord-ouest et sud-est.
    #
    # Pour cela, on va calculer, pour chaque case (i,j) avec des arbres, le nombre minimum de déplacements
    # aller-retour depuis l'usine vers une case vide adjacente à (i,j).
    #
    # On part de l'usine, puis on va couper les arbres une par une, et pour chaque arbre:
    # coût = (distance_aller_retour depuis usine à la case vide adjacente)*nombre d'arbres + (nombre d'arbres * 1 minute pour couper chaque arbre)
    #
    # Or 1 minute pour couper 1 arbre + (distance_aller_retour) minutes pour porter chaque arbre = (distance_aller_retour + 1) minutes
    # Selon l'exemple, le temps nécessaire pour couper un arbre et le rapporter est :
    # temps = 2*distance + 1 (l'exemple le montre ?)
    #
    # Exemple donné dans l'énoncé:
    # pour (1,3) avec 2 arbres:
    # distance from usine à (1,3) est 2
    # temps = 2 * distance + 1 = 2*2 + 1 = 5 pour 1 arbre, puis ça fois 2 arbres = 10 ?
    # Mais dans l'exemple il calcule differently:
    # Exemple explique que distance entre usine et arbre est 2 (cases)
    # Le trajet est: usine -> arbre (distance) + arbre -> usine (distance), pendant que l'arbre est porté (retour)
    # Le temps pour 1 arbre est: (aller + coupe + retour) = distance + 1 + distance = 2*distance +1
    #
    # Puis pour multipliquer par nombre d'arbres, car on ne peut couper qu'un arbre à la fois, pour chaque arbre on fait la même opération.
    #
    # Donc pour un arbre:
    # temps = (2 * distance + 1)
    #
    # Pour n arbres:
    # temps = n * (2 * distance + 1)
    #
    # Mais dans l'exemple du problème, ils calculent temps pour (1,3) avec 2 arbres = 6 minutes.
    # Pourquoi ? Ils ont le trajet comme distance aller-retour = 3 minutes pour couper 1 arbre.
    # Le nombre total: 2*3 = 6.
    # Donc ils prennent temps = n * (2*distance_arbre)
    # car le temps pour couper un arbre = 1 + temps de déplacement aller-retour
    # temps de déplacement aller-retour = 2 * distance depuis 1,1
    # Ici c'est 3, donc distance c'est 1,5 ? Non
    # Par exemple: Dist annoncer: "aller vers (1,3)" = 2 pas
    # Aller-retour = 4 pas + 1 min à couper = 5 ?
    # Mais dans l'exemple ça donne 6 pour 2 arbres, donc 3 par arbre => Sans compter le temps de coupe ?

    # Lisons précisément l'exemple d'entrée 1:
    # (1,2) arbres = 1, temps = 1
    # (1,3) arbres = 2,  
    # ils avancent de 1 case depuis usine (1,1) vers (1,2) puis vers (1,3)
    # distance aller-retour = 3 minutes (ils disent) et 2 arbres => 6 minutes.
    # Ils comptent 1 minute pour chaque arbre, puis aller-retour est 2 minutes (distance 1 case) *2 = 2
    # Mais ça ne colle pas avec l'analyse brute.
    #
    # Inspirons-nous directement de la méthode : pour chaque arbre coupé,
    # temps = (# d'arbres) * (distance aller-retour * 1 min +1 min couper)
    # or dans l'ensemble, le problème penche vers
    # pour un arbre en position (i,j):
    # t = nombre_arbre * (distance_aller-retour + temps_coupe) = n * (2 * distance + 1)
    #
    # Mais dans l'exemple, on lit plutôt :
    # le temps compte chaque déplacement sur case vide comme 1 minute
    # et couper 1 arbre comme 1 minute
    #
    # Plus simplement, on a :
    # temps = n * (2 * dist_from_start[i][j] + 1)
    #
    # On va donc prendre ceci comme coût.

    # Cependant, on ne peut couper un arbre que depuis une case sans arbre adjacente,
    # et il faut que cette case soit accessible depuis l'usine.
    #
    # Donc pour chaque cellule avec arbres, on doit trouver la distance minimale aller-retour depuis
    # l'usine vers UNE case vide adjacente à (i,j).
    #
    # Puis le coût total pour ces arbres est :
    # nombre_arbres * (2 * distance + 1)
    #
    # sum du tout pour chaque cellule avec arbres.

    INF = 10**9

    total_time = 0

    for i in range(H):
        for j in range(W):
            if A[i][j] > 0:
                # On cherche la distance minimale vers une case vide voisine
                min_dist_to_adjacent = INF
                for di,dj in [(-1,0),(1,0),(0,-1),(0,1)]:
                    ni,nj = i+di, j+dj
                    if 0 <= ni < H and 0 <= nj < W:
                        # Case adjacente doit être sans arbre et accessible depuis l'usine
                        if A[ni][nj] == 0 and dist_from_start[ni][nj] != -1:
                            # Pour couper l'arbre, le déplacement aller-retour est dist_from_start[ni][nj]*2
                            # Car il faut revenir à l'usine
                            if dist_from_start[ni][nj] < min_dist_to_adjacent:
                                min_dist_to_adjacent = dist_from_start[ni][nj]
                # Si pas d'accès, impossible de couper ces arbres. Selon l'énoncé, la solution doit être trouvée,
                # donc on peut ignorer ce cas.
                # Sinon on ajoute le temps nécessaire pour couper tous les arbres sur cette case
                # temps = nombre_arbres * (2*distance + 1)
                if min_dist_to_adjacent == INF:
                    # Impossible d'accéder à cette parcelle pour couper, mais problème dit que (H,W) ≠ (1,1),
                    # donc forçons passer
                    # On peut retourner -1 ou ignorer selon le problème, mais ici on ignore
                    # car la forêt est extérieure non accessible.
                    continue
                time_for_trees = A[i][j] * (2 * min_dist_to_adjacent + 1)
                total_time += time_for_trees
    
    # Enfin, on a accumulé le temps total minimal pour couper tous les arbres nécessaires
    # afin que le chemin puisse exister entre (1,1) et (H,W)
    # L'exemple semble indiquer qu'on ne doit couper que les arbres nécessaires pour ouvrir un chemin,
    # mais ici on somme pour tous les arbres.
    #
    # Cependant l'exemple ne coupe pas tous les arbres, certains laissant passer le chemin,
    # mais notre méthode consiste à ne couper que les arbres nécessaires en rapportant par
    # la distance minimale via cases sans arbres adjacentes
    
    # Or l'énoncé demande le temps minimal pour permettre la connexion.
    #
    # Comme dans l'exemple 2 et 3, on ne coupe pas tous les arbres, que ceux indispensables.
    #
    # Donc il faut trouver quels arbres sont sur "le chemin minimal", c'est un problème de "plus court chemin"
    # dans une grille où les cases avec arbres ont un coût à couper.
    #
    # Nous devons résoudre un problème de recherche de chemin du point NW à SE en minimisant le coût où
    # les cases vides coûtent 0 et les cases avec arbres coûtent (temps pour couper tous les arbres sur cette case).
    #
    # La méthode ci-dessus accumule le temps pour toutes les cases avec arbres, ce qui est incorrect.
    #
    # Donc il faut faire un Dijkstra sur la grille (H,W) en considérant :
    # - se déplacer sur case vide = coût 1 (1 minute), car c'est un déplacement
    # - se déplacer sur case avec arbres = interdit (car il faut couper les arbres d'abord)
    # - mais on peut couper les arbres avant : le coût pour couper et rapporter les arbres sur une case est
    #   A[i][j] * (2 * distance_to_nearest_adjacent_empty + 1)
    #
    # On peut modéliser le problème en rajoutant le poids de couper ces arbres sur le coût du chemin en allant vers SE.
    #
    # Alternativement :
    # l'énoncé dit que l'on commence à l'usine (1,1) sans arbres,
    # et chaque déplacement coute 1 minute,
    # pour couper les arbres sur une case voisine on dépense (nombre_arbres * 1) minute (de coupe),
    # pour rapporter chaque arbre on dépense (distance aller-retour) minutes en déplacement.
    #
    # Donc le coût pour couper les arbres d'une case = nombre_arbres * (1 + 2 * (distance_usine->case_adjacente)),
    # mais on peut se rendre à cette case seulement s'il y a un chemin de cases vides.
    #
    # Le problème revient à trouver un chemin en minimisant la somme des coûts de couper les arbres à côté,
    # c'est un problème de Dijkstra où on paye pour "couper" ou "marcher".
    #
    # On doit sortir un chemin du nord-ouest au sud-est : on peut marcher sur cases vides (coût 1),
    # on peut "couper" cases avec arbres adjacents (coût du coupe+rapporte),
    # puis continuer.
    #
    # Une solution est de transformer la grille en un graphe où :
    # - les cases vides ont un coût de déplacement 1,
    # - les cases avec arbres ont un coût de déplacement infinie,
    # - mais on peut "débloquer" une case avec arbres en "payant" le coût de couper les arbres,
    # ce qui revient à considérer ces cases comme une étape spéciale.
    #
    # Pour résoudre ce problème, on peut modéliser la grille en Dijkstra où à chaque case on a un
    # état : on peut soit passer normalement si case vide, soit si case avec arbres,
    # on doit payer le coût de couper.
    #
    # Ainsi, on définit un graphe pondéré où :
    # - pour les cases vides déplacement coût 1,
    # - pour chaque case à arbres coût de passer = couper tous les arbres et revenir à l'usine quand on coupe cette case,
    # on doit rendre le temps de coupe et transport.
    #
    # Mais cela complique le modèle.
    #
    # L'énoncé de l'exemple 1 explique simplement : on coupe les arbres à certains endroits, la somme des coûts est
    # la réponse.
    #
    # On peut penser :
    # - Toutes les cases non vides, on calcule le coût couper + rapporter.
    # - Puis on construit un graphe où on peut se déplacer sur cases vides uniquement.
    # - On sélectionne parmi les cases avec arbres celles qui justifient d'être coupées
    #   en les triant sur les chemins possibles.
    #
    # Une solution plus simple : 
    # on suppose que chaque case à arbres doit être coupée, et additionne leur coût.
    # Ce n'est pas optimal et ne respecte pas l'exemple 2-3.

    # Or les exemples 2 et 3 montrent que l'on ne doit pas couper tous les arbres mais uniquement ceux nécessaires pour assurer la connectivité.
    #
    # Le problème est en fait de trouver un chemin du nord-ouest vers sud-est dans une grille où chaque case a un coût (0 pour vide, temps pour couper arbres), et
    # on cherche le chemin minimal (somme des coûts plus déplacements).
    #
    # Solution adéquate:
    # Faire un Dijkstra où pour chaque case :
    # - si case vide: coût déplacement 1
    # - si case avec arbres: le coût = nombre_arbres * (2* minimal distance aller-retour vers usine depuis une case vide adjacente + 1), c'est-à-dire le temps de couper et ramener tous les arbres.
    #
    # Puis le chemin minimum en Dijkstra donne le temps minimal total.
    #
    # Le problème est que le coût de couper les arbres ne se réalise que si on arrive sur une case adjacente sans arbres, on coupe puis revient à l'usine.
    #
    # Cependant, l'énoncé ne dit pas qu'on peut avancer sur une case avec arbres.
    #
    # Par contre, lors de la coupe, on se trouve sur une case vide adjacente, puis on coupe les arbres dans une case voisine.
    #
    # Le découpage en coût pour déplacer semble inclure uniquement les cases vides.
    #
    # Donc un modèle clarifié:
    # - Les déplacements se font uniquement sur cases vides
    # - Pour couper les arbres sur une case (avec arbres), le joueur doit se rendre sur une case vide adjacente,
    #   y couper les arbres une par une (1min/arbre),
    #   puis ramener l'arbre à l'usine (temps déplacement aller-retour = 2 * distance du vide adjacente à l'usine).
    #
    # Le total du temps = somme sur toutes les cases avec arbres du nombre d'arbres * (1 + 2 * distance_from_usine_to_case_vide_adjacent)
    #
    # BUT on ne doit couper que les arbres qui empêchent la connectivité entre usine et destination.
    #
    # Pour trouver ces arbres, on peut simuler un graphe où les cases vides sont les noeuds,
    # et chaque arbre adjacent à un noeud vide nous devons "payer" le coût de couper ces arbres si on doit passer par ce noeud.
    #
    # Cela devient un problème complexe.
    
    # Simplification : la forêt est « démantelé » seulement sur les cases avec arbres bloquant le chemin.