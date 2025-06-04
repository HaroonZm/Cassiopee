# Solution complète en Python avec commentaires détaillés

import sys
sys.setrecursionlimit(10**7)

def can_complete_roundtrip(N, d):
    """
    Détermine si le sauteur peut compléter le trajet aller-retour en respectant les contraintes.
    
    Paramètres:
    - N: nombre de trampolines
    - d: liste des distances maximales de saut pour chaque trampoline
    
    Retourne:
    - "yes" si le trajet aller-retour est possible
    - "no" sinon
    """
    
    # Les trampolines sont espacés de 10m.
    # Le jumper peut sauter d'un trampoline i jusqu'à tout trampoline j tel que:
    #   abs(j - i)*10 <= min(d[i], d[j])
    #
    # En effet, le jumper saute d'un trampoline i vers un trampoline j (i < j pour aller,
    # i > j pour retour) si et seulement si:
    # - La distance horizontale entre i et j est (|j - i| * 10)
    # - Cette distance doit être <= à la portée maximale des deux trampolines
    #   puisque il ne faut pas que le saut dépasse la portée de départ ni d'arrivée.
    #
    # Problème : déterminer s'il existe un chemin allant de 0 à N-1 puis de N-1 à 0
    # dans le graphe défini par ces arcs.
    #
    # Observation importante :
    # Le graphe des transitions se base sur une distance horizontale 10*m,
    # et la condition min(d[i], d[j]) >= 10*|j-i|.
    #
    # Pour une direction donnée (aller ou retour), on peut représenter le graphe
    # orienté et vérifier si on peut se rendre de 0 à N-1 (aller), puis de N-1 à 0 (retour).
    #
    # Pour vérifier la connectivité, on peut construire le graphe orienté dans les deux sens :
    # - Arcs aller : i -> j avec i<j si 10*(j-i) <= min(d[i], d[j])
    # - Arcs retour : j -> i avec i<j même condition.
    #
    # Pour faire cela efficacement, on peut exploiter une approche basée sur les intervalles.
    #
    # Algorithme efficace:
    #
    # Given the large constraint (N up to 3*10^5), il est impossible de vérifier tous les couples.
    #
    # Utilisons une traversée en deux phases:
    # 1. Sens aller (de 0 à N-1):
    #    On veut vérifier si on peut "marcher" de 0 à N-1 avec les arcs i->j (j>i) satisfaisant
    #    10*(j-i) <= min(d[i], d[j]).
    #
    # 2. Sens retour (de N-1 à 0):
    #    De manière similaire, vérifier la connectivité en sens inverse.
    #
    # Approche:
    # Chaque trampoline i peut atteindre les trampolines j supérieurs dans un intervalle correspondant.
    #
    # Concrètement:
    #
    # Pour chaque trampoline i, définissons un intervalle de saut vers la droite:
    # - Le index j doit vérifier j > i
    # - 10*(j - i) <= d[i], donc j <= i + d[i]//10
    # - De même, pour que j puisse être atteint, d[j] >= 10*(j-i)
    #
    # Pour la portée du trampoline d[j] pour j > i, on doit vérifier la condition que :
    # 10*(j - i) <= d[j]
    #
    # On peut remarquer que pour pouvoir sauter de i vers j:
    #  10*(j - i) <= d[i]  and 10*(j - i) <= d[j]
    #
    # Par conséquent:
    # j peut être dans [i+1, i + d[i] // 10] (en respectant j < N)
    # puis, on doit s'assurer que d[j] >= 10*(j - i)
    #
    # On peut donc, pour le sens aller:
    # - pour chaque trampoline i, on connaît l'intervalle des indices possibles à atteindre pour j :
    #   j ∈ [i + 1, min(N - 1,  i + d[i] // 10)]
    # - on choisit parmi ces j ceux qui vérifient d[j] >= 10*(j - i)
    #
    # Il faudrait vérifier ce critère pour tous les j dans cet intervalle.
    #
    # Faire cela pour tous les i, naïvement, est trop coûteux.
    #
    # Optimisation:
    # On va parcourir les trampolines et déterminer la portée maximale de saut vers la droite
    # par dp ou segment tree.
    #
    # Stratégie:
    # Construire un graphe implicite où:
    # - On peut aller de i à j > i, si 10*(j - i) <= d[i] et 10*(j - i) <= d[j]
    #
    # Remarquons que la condition 10*(j - i) <= d[j] est critique.
    #
    # Pour vérifier si on peut atteindre la droite jusqu’à un certain index, on peut implémenter un balayage linéaire.
    #
    # Implémentation pratique:
    # On va déterminer, pour chaque trampoline, le maximum reachable index vers la droite
    # qu'on peut atteindre soigneusement.
    # Puis on vérifiera si on peut finalement atteindre N-1.
    #
    #
    # Même raisonnement pour le retour, du N-1 vers 0 par arcs inverses.
    
    # Fonction qui calcule si on peut aller de start à goal dans une direction donnée
    # direction = 1 (aller de gauche à droite)
    # direction = -1 (retour de droite à gauche)
    def can_reach(d, start, goal, direction):
        # On travaille sur l'intervalle selon direction
        # L'idée: on maintient le maximum reachable via une exploration efficace
        
        N = len(d)
        # reachable[i] indique si on peut atteindre trampoline i
        reachable = [False] * N
        reachable[start] = True
        
        # max_reach indique jusqu'où on a réussi à se propager
        max_reach = start
        
        # On parcourt dans la direction demandée
        # La condition de saut est:
        # for i,j with direction=1: i < j
        # 10*(|j - i|) <= d[i] and 10*(|j - i|) <= d[j]
        #
        # On va avancer en étendant la zone reachable:
        
        # Pour faciliter un balayage efficace on génère un tableau "limite" qui contient pour chaque trampoline
        # le max j tel que j dans direction puisse être rejoint.
        
        # On crée un tableau next_max_reach où pour chaque trampoline i on définit la limite maximale d'indice
        # atteignable depuis i selon d[i].
        
        next_max_reach = [0]*N
        
        if direction == 1:
            # vers la droite
            for i in range(N):
                jump_max = i + d[i] // 10
                if jump_max >= N:
                    jump_max = N - 1
                next_max_reach[i] = jump_max
            
            # On avance de start à goal
            i = start
            while i <= max_reach and i < N:
                if reachable[i]:
                    # On essaye d'étendre max_reach vers next_max_reach[i], en vérifiant les conditions sur d[j]
                    # Contrairement à notre première idée, on doit vérifier condition sur d[j]
                    # Pour j dans (max_reach+1) à next_max_reach[i], on vérifie 10*(j - i) <= d[j]
                    # Si ok, reachable[j] = True, et on étend max_reach
                    from_idx = max(max_reach+1, i+1)
                    to_idx = next_max_reach[i]
                    for j in range(from_idx, to_idx+1):
                        distance = 10 * (j - i)
                        if distance <= d[j]:
                            if not reachable[j]:
                                reachable[j] = True
                                max_reach = max(max_reach, j)
                        else:
                            # Si la condition est fausse pour un j donné,
                            # et comme d[j] est indépendante, continuer a un j supérieur ne garantit rien.
                            # Mais d est arbitraire, donc on doit tester tous.
                            pass
                i += 1
            
            return reachable[goal]
        
        else:
            # direction == -1, vers la gauche
            # mêmes raisonnements mais indices décroissants
            for i in range(N):
                jump_min = i - d[i] // 10
                if jump_min < 0:
                    jump_min = 0
                next_max_reach[i] = jump_min
            
            i = start
            min_reach = start
            reachable[start] = True
            while i >= min_reach and i >= 0:
                if reachable[i]:
                    # On essaye d'etendre min_reach vers next_max_reach[i] < i
                    from_idx = min(min_reach-1, i-1)
                    to_idx = next_max_reach[i]
                    # En ordre décroissant
                    for j in range(from_idx, to_idx-1, -1):
                        distance = 10 * (i - j)
                        if distance <= d[j]:
                            if not reachable[j]:
                                reachable[j] = True
                                min_reach = min(min_reach, j)
                        else:
                            # Même raisonnement que pour l'aller
                            pass
                i -= 1
            return reachable[goal]

    # Appel des deux phases:
    can_go = can_reach(d, 0, N - 1, 1)
    can_return = can_reach(d, N - 1, 0, -1)

    return "yes" if can_go and can_return else "no"

if __name__ == "__main__":
    input = sys.stdin.readline
    N = int(input())
    d = [int(input()) for _ in range(N)]
    print(can_complete_roundtrip(N, d))