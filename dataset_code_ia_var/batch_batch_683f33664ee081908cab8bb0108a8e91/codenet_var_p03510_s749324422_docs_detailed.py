def main():
    """
    Programme principal pour lire un nombre d'événements, puis traiter chacun pour calculer
    la valeur maximale atteinte par la variable A après chaque événement.

    Lecture de N. Pour chaque événement, on saisit un instant x et une valeur s.
    À chaque étape, on applique: 
      - La diminution de A en fonction du temps écoulé depuis l'événement précédent
      - L'ajout de s à A
      - La mise à jour de la valeur maximale atteinte par A
    Enfin, on affiche la valeur maximale atteinte.
    """
    N = int(input())  # Lire le nombre d'événements à traiter

    A = 0  # Variable accumulant la quantité présente à l'instant courant
    p = 0  # Dernier instant de temps traité
    ans = 0  # Maximum atteint par la variable A

    for i in range(N):
        x, s = read_event()
        # Mise à jour de A : perte naturelle avec le temps, puis ajout du nouvel apport
        A = max(0, A - (x - p)) + s
        # Mise à jour du maximum atteint si besoin
        ans = max(ans, A)
        # Mise à jour de l'instant précédent pour le prochain tour de boucle
        p = x

    print(ans)


def read_event():
    """
    Lis une ligne d'entrée depuis l'utilisateur et retourne un tuple (x, s), où :
      - x (int) représente l'instant auquel un événement intervient
      - s (int) représente la valeur apportée à cet instant

    Returns:
        tuple: (x, s)
    """
    x, s = map(int, input().split())
    return x, s


if __name__ == "__main__":
    main()