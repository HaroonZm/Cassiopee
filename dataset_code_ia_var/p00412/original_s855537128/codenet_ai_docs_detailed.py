from collections import deque

def initialize_queues(num_queues):
    """
    Crée une liste de files (deque vides).

    Args:
        num_queues (int): Le nombre de files à créer.

    Returns:
        list: Une liste de files (deques), initialement vides.
    """
    queues = []
    for _ in range(num_queues):
        queues.append(deque())
    return queues

def initialize_lengths(num_queues):
    """
    Crée une liste représentant la taille de chaque file, initialisée à 0.

    Args:
        num_queues (int): Le nombre de files.

    Returns:
        list: Une liste d'entiers à zéro.
    """
    return [0] * num_queues

def process_operations(num_queues, num_operations):
    """
    Gère la séquence d'opérations sur les files en fonction des entrées utilisateur.

    Args:
        num_queues (int): Le nombre de files à gérer.
        num_operations (int): Le nombre d'opérations à traiter.
    """
    # Initialiser les files et leur suivi de taille associée
    queues = initialize_queues(num_queues)
    lengths = initialize_lengths(num_queues)

    # Parcourir chaque opération
    for _ in range(num_operations):
        info, num = [int(x) for x in input().split(" ")]

        if info == 0:
            # Opération 0 : Retirer et afficher l'élément le plus ancien de la file 'num-1'
            print(queues[num - 1].popleft())
            lengths[num - 1] -= 1
        elif info == 1:
            # Opération 1 : Ajouter 'num' à la file la moins chargée
            # On cherche la file avec la taille maximale, pour un comportement identique au code d'origine (remarque: le code original utilise le plus petit indice dont la taille est maximale)
            index = 0
            for j in range(num_queues):
                if lengths[index] > lengths[j]:
                    index = j
            queues[index].append(num)
            lengths[index] += 1

def main():
    """
    Point d'entrée principal du programme. Lis les paramètres, puis traite les opérations sur les files.
    """
    # Lire le nombre de files et d'opérations à effectuer
    N, M = [int(x) for x in input().split(" ")]
    process_operations(N, M)

if __name__ == "__main__":
    main()