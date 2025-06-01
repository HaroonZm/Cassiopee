# Solution complète en Python avec commentaires détaillés

import sys
sys.setrecursionlimit(10**7)
input = sys.stdin.readline

def can_reach_all(N, d, start, end, step):
    """
    Fonction pour vérifier si on peut atteindre `end` à partir de `start`
    en sautant de trampoline en trampoline.
    La direction est définie par `step`: +1 pour aller vers la droite,
    -1 pour aller vers la gauche.
    On utilise une approche en parcours BFS pour éviter la récursivité profonde
    et pour rejeter rapidement les trampolines inaccessibles.
    
    Arguments:
    - N : nombre de trampolines
    - d : liste des distances maximales de saut pour chaque trampoline
    - start : index de départ
    - end : index d'arrivée (inclus)
    - step : direction du déplacement (+1 ou -1)
    
    Retourne:
    - True si on peut atteindre `end` à partir de `start`
    - False sinon
    """
    from collections import deque
    
    visited = [False]*N
    queue = deque([start])
    visited[start] = True
    
    while queue:
        current = queue.popleft()
        # Si on a atteint la destination finale, on s'arrête
        if current == end:
            return True
        
        # Distance max en mètres à sauter = d[current]
        # Comme les trampolines sont espacés de 10m, on peut calculer
        # combien de trampolines on peut potentiellement atteindre dans cette direction
        max_steps = d[current] // 10
        
        # Dans la direction donnée (step), on peut aller de current+step jusqu'à current+step*max_steps
        # On vérifie toutes les cibles potentielles qui ne dépassent pas les limites de la ligne
        
        # Pour optimisation, on itère les trampolines atteignables
        for nxt in range(current+step, current+step*(max_steps+1), step):
            if 0 <= nxt < N and not visited[nxt]:
                visited[nxt] = True
                queue.append(nxt)
            # Si hors limites, on arrête la recherche dans cette direction
            if nxt < 0 or nxt >= N:
                break
    
    return False

def main():
    # Lecture du nombre de trampolines
    N = int(input())
    # Lecture des distances max de saut pour chaque trampoline
    d = [int(input()) for _ in range(N)]
    
    # Le problème est de déterminer si on peut aller du trampoline 0 (gauche)
    # au trampoline N-1 (droite), puis revenir au trampoline 0,
    # en respectant la portée de saut de chaque trampoline à chaque étape.
    #
    # Approach:
    # 1) Vérifier si on peut aller de 0 à N-1 en sautant vers la droite
    # 2) Vérifier si on peut revenir de N-1 à 0 en sautant vers la gauche
    #
    # Si les deux conditions sont satisfaites, on imprime "yes"
    # sinon "no"
    
    can_go_right = can_reach_all(N, d, 0, N-1, step=1)
    if not can_go_right:
        print("no")
        return
    
    can_go_left = can_reach_all(N, d, N-1, 0, step=-1)
    if not can_go_left:
        print("no")
        return
    
    print("yes")

if __name__ == '__main__':
    main()