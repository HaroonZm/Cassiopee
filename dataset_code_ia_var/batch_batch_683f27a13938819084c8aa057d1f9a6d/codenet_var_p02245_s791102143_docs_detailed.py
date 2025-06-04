from sys import stdin
import queue

# Définition des mouvements possibles pour chaque position du plateau dans le puzzle 8-puzzle.
# Par exemple, depuis la position 0, le trou peut être échangé avec les positions 1 et 3.
adjacent = (
    (1, 3),      # 0
    (0, 2, 4),   # 1
    (1, 5),      # 2
    (0, 4, 6),   # 3
    (1, 3, 5, 7),# 4
    (2, 4, 8),   # 5
    (3, 7),      # 6
    (4, 6, 8),   # 7
    (5, 7)       # 8
)

class State:
    """
    Représente un état du plateau du 8-puzzle.

    Attributs:
        board (list): Plateu actuel du puzzle sous forme d'une liste de 9 entiers.
        space (int): Position du trou (zéro) sur le plateau.
        prev (State): État précédent menant à cet état (utilisé pour remonter la solution).
    """
    def __init__(self, board, space, prev):
        self.board = board
        self.space = space
        self.prev = prev

def bf_search(start, end):
    """
    Exécute une recherche en largeur (BFS) pour trouver le nombre minimal de mouvements 
    entre l'état initial et l'état cible dans le puzzle 8-puzzle.

    Args:
        start (list): Liste des entiers représentant l'état initial du puzzle.
        end (list): Liste des entiers représentant l'état final du puzzle.

    Returns:
        int: Nombre minimal de déplacements pour atteindre l'état final, ou None en cas d'absence de solution.
    """
    q = queue.Queue()  # File d'attente pour BFS
    q.put(State(start, start.index(0), None))  # Ajouter l'état initial à la queue
    table = {}  # Table de hachage pour mémoriser les états déjà visités
    table[tuple(start)] = True  # Marquer l'état initial comme visité

    while not q.empty():
        a = q.get()  # Extraire l'état courant de la file
        for i in adjacent[a.space]:  # Pour chaque mouvement possible du trou
            b = a.board[:]  # Copier le plateau actuel
            b[a.space] = b[i]  # Échanger le trou avec la tuile voisine
            b[i] = 0

            key = tuple(b)  # Transformer le plateau en tuple pour usage comme clé de table
            if key in table:
                continue  # Passer aux mouvements suivants si cet état a été déjà visité

            # Créer un nouvel état basé sur ce plateau
            c = State(b, i, a)

            # Si l'état courant correspond à l'état final, retourner la solution
            if b == end:
                return printAns(c)

            # Sinon, ajouter cet état à la file d'attente pour exploration future
            q.put(c)
            table[key] = True  # Marquer comme visité

count = -1  # Variable globale pour compter les mouvements

def printAns(c):
    """
    Parcourt récursivement les états précédents pour compter le nombre de mouvements 
    nécessaires depuis l'état initial jusqu'à l'état courant.

    Args:
        c (State): État courant.

    Returns:
        int: Nombre de mouvements effectués depuis l'état initial.
    """
    global count
    if c is not None:
        count += 1
        printAns(c.prev)  # Retour à l'état précédent pour compter tous les mouvements
    return count

# Définition de l'état final du 8-puzzle ([1,2,3,4,5,6,7,8,0])
end = [1, 2, 3, 4, 5, 6, 7, 8, 0]

# Lecture de l'état initial en brut depuis l'entrée standard (3 lignes, 3 nombres par ligne)
start = [int(n) for _ in range(3) for n in stdin.readline().split()]

# Si l'état initial est déjà l'état final, retourner 0, sinon lancer la recherche BFS
if start == end:
    print(0)
else:
    print(bf_search(start, end))