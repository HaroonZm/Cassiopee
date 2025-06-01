import sys

def main():
    """
    Programme principal pour calculer la quantité maximale d'une ressource après une série d'entrées et sorties.

    L'utilisateur saisit deux entiers :
    - n : le nombre d'étapes.
    - m : la quantité initiale de la ressource.

    Ensuite, pour chacune des n étapes, l'utilisateur saisit deux entiers :
    - a : la quantité ajoutée à la ressource.
    - b : la quantité retirée de la ressource.

    Le programme met à jour la quantité de ressource en ajoutant a et en soustrayant b.
    Si à un moment la quantité devient négative, le programme affiche 0 et s'arrête immédiatement.
    Sinon, il affiche la quantité maximale atteinte durant toutes les étapes.
    """

    # Lecture du nombre d'étapes
    n = int(input())
    # Lecture de la quantité initiale de la ressource
    m = int(input())

    # Liste pour stocker la quantité de ressource à chaque étape, débutant avec la valeur initiale
    s = [m]

    # Parcours des n étapes pour mettre à jour la quantité de ressource
    for i in range(1, n+1):
        # Lecture des quantités ajoutée (a) et retirée (b) à la ressource pour cette étape
        a, b = map(int, input().split())

        # Mise à jour de la quantité de ressource
        m = m + a - b

        # Vérification que la quantité ne soit pas négative
        if m < 0:
            # Si négative, affichage de 0 et arrêt immédiat du programme
            print(0)
            sys.exit(0)

        # Stockage de la quantité de ressource après cette étape
        s.append(m)

    # Affichage de la quantité maximale atteinte pendant toutes les étapes
    print(max(s))

if __name__ == "__main__":
    main()