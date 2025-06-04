def main():
    """
    Fonction principale qui gère la saisie utilisateur en boucle et affiche le résultat du jeu
    pour chaque paire d'entiers (man, donst) fournie en entrée.
    Termine lorsque '0 0' est saisi.
    """

    while True:
        # Récupérer une ligne de saisie utilisateur et la séparer en entiers
        data = input()
        data = data.split(" ")

        # Conversion des chaînes de caractères de la liste en entiers
        for i in range(len(data)):
            data[i] = int(data[i])

        # Condition d'arrêt du programme : si l'utilisateur saisit '0 0'
        if data == [0, 0]:
            return

        man = data[0]      # Nombre d'hommes/joueurs/éléments
        donst = data[1]    # "Dons" ou unités à répartir au début

        # Appel de la logique du jeu et affichage du résultat
        print(game(man, donst))


def game(man, donst):
    """
    Simule le 'jeu' sur une distribution circulaire de dons/unités.
    
    Args:
        man (int): Nombre d'éléments/joueurs.
        donst (int): Nombre initial de dons/unités à répartir.
    
    Returns:
        int: Indice (base 0) de l'élément qui satisfait la condition de fin du jeu.
    
    La logique consiste à distribuer les dons un par un à chaque joueur successivement.
    Si un tour est terminé alors que des dons restent, le processus recommence.
    Lorsqu'il ne reste qu'une seule case vide (toutes les autres ont reçu au moins un don),
    le jeu s'arrête et retourne l'indice du joueur qui a reçu le dernier don.
    """

    # Initialiser la liste des joueurs à 0 dons
    manst = [0 for _ in range(man)]

    while True:
        # Parcourir chaque joueur (distribution circulaire)
        for j in range(len(manst)):
            if donst != 0:
                # Distribuer un don au joueur actuel
                donst -= 1
                manst[j] += 1

                # Vérifier si c'était le dernier don
                if donst == 0:
                    zerocount = 0
                    # Compter combien de joueurs n'ont reçu aucun don
                    for item in manst:
                        if item == 0:
                            zerocount += 1

                    # Si tous sauf un joueur ont 0, retourner l'indice de ce joueur
                    if zerocount == man - 1:
                        return j

            else:
                # Récupérer tous les dons du joueur actuel et les redonner à distribuer
                donst = manst[j]
                manst[j] = 0

main()