from collections import deque

def process_commands(q, commands):
    """
    Traite une série de commandes pour manipuler une double file (deque).
    
    Args:
        q (int): Le nombre de commandes à exécuter.
        commands (list of list of int): Une liste de commandes. Chaque commande 
            est une liste d'entiers dont la signification dépend du type de commande.
            
            - [0, d, x]: Insère l'élément 'x' en tête (d=0) ou en queue (d=1) de la deque.
            - [1, p]: Affiche l'élément à la position 'p' dans la deque.
            - [2, d]: Retire l'élément en tête (d=0) ou en queue (d=1) de la deque.
    
    Returns:
        None
    """
    # Initialise la deque pour stocker les éléments
    lis = deque()
    # On parcourt chaque commande
    for cmd in commands:
        order = cmd[0]
        if order == 0:
            # Commande d'insertion
            d = cmd[1]
            value = cmd[2]
            if d == 0:
                # Insertion en tête
                lis.appendleft(value)
            else:
                # Insertion en queue
                lis.append(value)
        elif order == 1:
            # Commande d'accès à un élément selon l'index
            index = cmd[1]
            print(lis[index])
        elif order == 2:
            # Commande de suppression d'un élément (tête ou queue)
            d = cmd[1]
            if d == 0:
                # Suppression en tête
                lis.popleft()
            else:
                # Suppression en queue
                lis.pop()
        # Autres commandes éventuelles peuvent être ajoutées ici si nécessaire

def read_commands():
    """
    Lit les commandes de l'entrée standard au format décrit et exécute la fonction process_commands().
    
    Returns:
        None
    """
    # Lire le nombre de commandes à exécuter
    q = int(input())
    commands = []
    # Lire chaque commande et les ajouter à la liste
    for _ in range(q):
        cmd = [int(x) for x in input().split()]
        commands.append(cmd)
    # Traitement des commandes
    process_commands(q, commands)

# Point d'entrée pour lancer la lecture et l'exécution des commandes
if __name__ == "__main__":
    read_commands()