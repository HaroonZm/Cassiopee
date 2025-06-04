def shuffle_cards(cards: str, operations: int, shifts: list) -> str:
    """
    Effectue une série de mélanges sur une séquence de cartes selon les instructions données.
    
    Args:
        cards (str): La chaîne représentant la séquence de cartes.
        operations (int): Le nombre d'opérations de découpe à effectuer.
        shifts (list of int): Une liste contenant les indices de découpe pour chaque opération.
    
    Returns:
        str: La séquence de cartes après toutes les opérations de découpe.
    """
    # On parcourt toutes les valeurs de découpe spécifiées
    for h in shifts:
        # À chaque opération, découpe la chaîne à l'indice h et recolle les morceaux dans l'ordre inversé
        cards = cards[h:] + cards[:h]
    # Retourne la séquence finale après toutes les opérations
    return cards

def main():
    """
    Boucle principale du programme qui lit les entrées utilisateur,
    applique les opérations de mélange jusqu'à recevoir le caractère '-',
    puis affiche la séquence de cartes après chaque série d'opérations.
    """
    while True:
        # Lis la séquence de cartes depuis l'entrée utilisateur
        cards = input()
        # Si la séquence lue est '-', on arrête le programme
        if cards == '-':
            break
        # Lis le nombre d'opérations à effectuer
        operations = int(input())
        shifts = []
        # Pour chaque opération, lire le nombre de cartes à découper
        for _ in range(operations):
            h = int(input())
            shifts.append(h)
        # Applique les opérations de découpe et affiche le résultat
        result = shuffle_cards(cards, operations, shifts)
        print(result)

# Si ce script est exécuté directement, on lance la fonction principale
if __name__ == '__main__':
    main()