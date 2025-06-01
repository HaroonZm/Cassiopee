import queue

def process_game(m, n, d):
    """
    Traite une instance du problème en déterminant si la condition finale est satisfaite.
    
    Args:
        m (int): Le paramètre maximal utilisé pour les déplacements (portée maximale).
        n (int): Le nombre d'étapes ou positions dans le jeu.
        d (list[int]): Liste des décalages associés à chaque position (indexée de 1 à n).
        
    Retourne:
        str: 'OK' si la condition est satisfaite, 'NG' sinon.
    """
    # Initialisation des tableaux de travail avec taille n+2 pour gérer les positions 0 à n+1
    d = [0] + d + [0]  # Ajoute un 0 en début et fin pour correspondre à l'original
    visited = [False] * (n + 2)  # Marque les positions déjà atteintes durant la recherche avant
    visited[0] = True  # La position de départ (0) est considérée visitée
    ok = [False] * (n + 2)  # Indique si une position est "OK" (accessible depuis la position finale)
    ok[n + 1] = True  # La position finale (n+1) est toujours "OK"

    # Liste de prédecesseurs inverse, rev[k] contient les positions pouvant atteindre k
    rev = [[] for _ in range(n + 2)]

    # Première phase : recherche des positions atteignables à partir de la position 0
    que = queue.LifoQueue()
    que.put(0)

    while not que.empty():
        i = que.get()
        # Pour tous les déplacements possibles allant de 1 à m
        for j in range(1, m + 1):
            if i + j > n + 1:
                # Sort de la boucle si dépasse la position finale
                break
            # Nouvelle position corrigée par le décalage d[i+j]
            k = min(max(i + j + d[i + j], 0), n + 1)
            rev[k].append(i)  # Enregistre i comme prédécesseur de k
            if not visited[k]:
                que.put(k)  # Ajoute la position à visiter
                visited[k] = True  # Marque comme visitée

    # Deuxième phase : propagation inversée pour marquer les positions "ok"
    que.put(n + 1)
    while not que.empty():
        i = que.get()
        for j in rev[i]:
            if not ok[j]:
                ok[j] = True  # Marque la position accessible depuis la fin comme "ok"
                que.put(j)

    # Vérification finale : si la position finale n'est pas visitée ou
    # s'il existe une position visitée mais pas "ok", alors 'NG'
    ans = 'OK'
    if not visited[n + 1]:
        ans = 'NG'
    else:
        for i in range(n + 1):
            if visited[i] and (not ok[i]):
                ans = 'NG'
                break

    return ans

if __name__ == "__main__":
    while True:
        m = int(input())
        if m == 0:
            # Fin de la saisie et du programme
            break
        n = int(input())
        # Lecture des décalages pour chaque position i de 1 à n
        d = [int(input()) for _ in range(n)]
        resultat = process_game(m, n, d)
        print(resultat)