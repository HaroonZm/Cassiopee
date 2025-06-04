def shuffle(card, h):
    """
    Effectue une opération de brassage sur une chaîne représentant une pile de cartes.

    Le brassage consiste à couper les 'h' premières cartes du dessus et à les placer à la fin du paquet.

    Args:
        card (str): La pile de cartes, chaque caractère représentant une carte.
        h (int): Le nombre de cartes à couper du dessus du paquet.

    Returns:
        str: La nouvelle pile de cartes après le brassage.
    """
    # Convertir la chaîne de caractères 'card' en liste pour manipulation
    card_list = list(card)
    # Prendre la sous-liste des cartes après les 'h' premières
    new_card_list = card_list[h:]
    # Ajouter à la fin la sous-liste des 'h' premières cartes coupées du dessus
    new_card_list.extend(card_list[0:h])
    # Convertir la liste de cartes remodelée en chaîne et la retourner
    return ''.join(new_card_list)

# Boucle principale pour la lecture des entrées et le traitement de chaque cas
while True:
    # Lecture de la pile de cartes depuis l'entrée, suppression des espaces en fin de ligne
    card = raw_input().rstrip()
    # Si l'entrée est '-', la boucle s'arrête (fin des données)
    if card == '-':
        break
    else:
        # Lecture du nombre de brassages à effectuer pour cette pile de cartes
        shuffles = int(raw_input())
        # Pour chaque brassage, lire la valeur de découpe et effectuer le brassage
        for i in range(shuffles):
            h = int(raw_input())
            card = shuffle(card, h)
        # Affichage du résultat final du brassage pour cette pile de cartes
        print card