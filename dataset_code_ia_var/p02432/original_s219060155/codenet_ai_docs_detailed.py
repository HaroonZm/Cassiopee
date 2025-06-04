from collections import deque

def process_queries():
    """
    Traite une série de requêtes utilisateur pour manipuler une deque.
    Les requêtes peuvent insérer, accéder ou retirer des éléments.
    La fonction lit l'entrée standard pour récupérer le nombre et le détail des requêtes.

    Structure des requêtes et actions (selon entrée utilisateur) :
        - [0, from_left, value] : Ajoute 'value' au début (from_left=0) ou à la fin (from_left=1) de la deque
        - [1, index] : Affiche la valeur à l'index indiqué de la deque
        - [2, from_left] : Retire du début (from_left=0) ou de la fin (from_left=1) de la deque
    """
    # Initialisation d'une deque vide pour stocker les éléments de la file
    q = deque()

    # Lecture du nombre total de requêtes à traiter, entrée standard
    n = int(input())

    # Parcours des requêtes une par une
    for _ in range(n):
        # Lecture et parsing de la requête utilisateur sous forme de liste d'entiers
        req = list(map(int, input().split()))
        
        # Si la requête commence par 0 : insertion dans la deque
        if req[0] == 0:
            # req[1] == 0 : insérer à gauche (début), sinon à droite (fin)
            if req[1] == 0:
                q.appendleft(req[2])
            else:
                q.append(req[2])
        
        # Si la requête commence par 1 : afficher un élément de la deque
        elif req[0] == 1:
            # Affichage de l'élément situé à l'index req[1], suivi d'un retour à la ligne
            print(q[req[1]], end='\n')
        
        # Si la requête commence par 2 : suppression d'un élément de la deque
        else:
            # req[1] == 0 : retirer du début, sinon de la fin
            if req[1] == 0:
                q.popleft()
            else:
                q.pop()

# Appel de la fonction principale de traitement des requêtes
process_queries()