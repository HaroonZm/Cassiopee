from collections import deque

def read_input_sequence():
    """
    Lit le format d'entrée standard pour le problème.
    Lit la hauteur maximale de saut M, puis le nombre de positions N,
    puis la liste des hauteurs supplémentaires D pour chaque position.
    Retourne un tuple (M, N, D) ou None si M == 0 (fin des cas).
    """
    M = int(input())  # Lecture de la hauteur maximale de saut
    if M == 0:
        return None
    N = int(input())  # Lecture du nombre de positions (plateformes)
    # Lecture des valeurs supplémentaires D pour chaque position (liste indexée à partir de 1)
    D = [int(input()) for _ in range(N)]
    return (M, N, D)

def build_graph_and_reachability(M, N, D):
    """
    Construit le graphe implicite des déplacements possibles à partir de la position de départ.
    Calcule la liste de positions atteignables en partant de la case 0, selon la logique décrite.
    Retourne le graphe inversé G et la liste de positions atteintes u.
    
    Args:
        M (int): Hauteur maximale de saut.
        N (int): Nombre de positions.
        D (list): Liste des valeurs de bonus (longueurs de saut supplémentaires).
        
    Returns:
        G (list): Graphe inversé, G[to] contient les positions d'où on vient à 'to'
        u (list): Liste booléenne d'accessibilité depuis la case de départ.
    """
    # Ajout de 0 au début et à la fin pour gérer le départ (0) et l'arrivée (N+1)
    D_full = [0] + D + [0]
    G = [[] for _ in range(N + 2)]  # Graphe inversé (pour la rétro-propagation après)
    u = [0] * (N + 2)  # Liste des cases atteintes depuis la position de départ
    queue = deque([0])  # On démarre toujours de la position 0
    u[0] = 1  # On marque la position de départ comme atteinte

    while queue:
        v = queue.popleft()
        for j in range(1, M + 1):  # Pour chaque saut d'une hauteur possible
            next_pos = min(v + j, N + 1)  # Calcul de la destination de base
            # Si la prochaine case a un bonus (D != 0)
            if D_full[next_pos] != 0:
                # On applique le bonus (peut projeter au-delà de N+1 mais on limite)
                to = max(min(next_pos + D_full[next_pos], N + 1), 0)
            else:
                to = next_pos
            if not u[to]:
                queue.append(to)  # On ajoute au parcours BFS si non visitée
                u[to] = 1
            G[to].append(v)  # On ajoute l'origine v comme antécédent de 'to'
    return G, u

def check_double_reachability(G, u):
    """
    Vérifie si, en partant de la case d'arrivée, on atteint exactement les mêmes cases
    que celles qui étaient atteignables depuis le départ (par rétropropagation sur le graphe inversé).
    
    Args:
        G (list): Graphe inversé des antécédents.
        u (list): Liste booléenne d'accessibilité depuis la case de départ.
    
    Returns:
        bool: True si toutes les cases atteignables depuis le départ sont accessibles
        en rétropropagation depuis N+1, False sinon.
    """
    N = len(G) - 2  # On retrouve N
    z = [0] * (N + 2)  # Liste des positions rétro-accessibles depuis (N+1)
    queue = deque([N + 1])
    z[N + 1] = 1  # On considère la case d'arrivée comme accessible

    while queue:
        v = queue.popleft()
        for w in G[v]:  # Pour chaque position d'origine menant à v
            if z[w]:
                continue  # Déjà visitée
            z[w] = 1
            queue.append(w)
    return u == z  # On compare l'ensemble des positions accessibles dans les deux sens

def process_case(M, N, D):
    """
    Traite un cas d'entrée : calcule la possibilité d'accès de N+1 à partir de 0
    en tenant compte des sauts et bonus, et affiche "OK" si le parcours est valide
    dans les deux sens, sinon "NG".
    
    Args:
        M (int): Hauteur maximale de saut.
        N (int): Nombre de cases principales.
        D (list): Liste des bonus pour chaque case.
    """
    G, u = build_graph_and_reachability(M, N, D)
    if check_double_reachability(G, u):
        print("OK")
    else:
        print("NG")

def main():
    """
    Programme principal. Lit la séquence d'entrées, traite chaque cas jusqu'à M=0 (fin),
    et imprime le résultat "OK" ou "NG" pour chaque cas.
    """
    while True:
        input_case = read_input_sequence()
        if input_case is None:
            break  # Fin de l'entrée
        M, N, D = input_case
        process_case(M, N, D)

if __name__ == "__main__":
    main()