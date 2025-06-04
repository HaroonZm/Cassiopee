class Dice:
    """
    Représente un dé à six faces et permet de déterminer la valeur de la droite d'une face donnée 
    une fois la face du dessus (top) et la face avant (front) spécifiées.
    """
    
    def __init__(self):
        """
        Initialise les arrangements par défaut des faces du dé en lignes nord-sud (NS) et est-ouest (EW).
        L'ordre des faces est maintenu par deux listes qui sont manipulées selon les rotations du dé.
        Les valeurs dans les listes représentent les numéros des faces.
        """
        # Copie des arrangements initiaux pour éviter que des modifications dans une instance n'affectent une autre
        self.NS = [1, 5, 6, 2]  # L'ordre est : top, north, bottom, south
        self.EW = [1, 3, 6, 4]  # L'ordre est : top, east, bottom, west

    def question(self, top, front):
        """
        Donne la valeur de la face à droite de la face 'front' quand la face 'top' est au-dessus.

        Args:
            top (int): La valeur (numéro) de la face à placer sur le dessus du dé.
            front (int): La valeur (numéro) de la face placée à l'avant (face visible à l'avant).

        Returns:
            int: La valeur de la face située à droite de la face 'front'.
        """
        # Met en place le dé avec la bonne face sur le dessus
        self.setTop(top)
        # Sélectionne les valeurs des faces dans l'ordre [north, east, south, west]
        sides = [self.NS[1], self.EW[1], self.NS[3], self.EW[3]]
        # Calcule et renvoie la face située à droite de 'front'
        return sides[(sides.index(front) + 1) % 4]

    def setTop(self, n):
        """
        Oriente le dé pour que la face 'n' se retrouve sur le dessus (top).

        Args:
            n (int): Valeur (numéro) de la face à mettre au dessus.

        Cette méthode modifie les arrangements 'NS' et 'EW' pour refléter la rotation sur l'axe nord-sud ou est-ouest.
        """
        if n in self.NS:
            # On fait pivoter le dé sur l'axe nord-sud jusqu'à ce que la face 'n' soit en haut
            while self.NS[0] != n:
                self.N()
        else:
            # Si la face n'est pas déjà dans l'axe nord-sud, on fait des rotations est-ouest
            while self.NS[0] != n:
                self.E()

    def N(self):
        """
        Effectue une rotation du dé vers le nord. Met à jour les listes 'NS' et 'EW' en conséquence.
        Après la rotation :
            - La face du nord devient le dessus,
            - La face du dessous devient le sud, etc.
        """
        tail = self.NS.pop()        # Retire la face 'south'
        self.NS.insert(0, tail)     # Met la face 'south' sur le dessus
        self.EW[0] = self.NS[0]     # Synchronise la face du dessus sur EW
        self.EW[2] = self.NS[2]     # Synchronise la face du dessous sur EW

    def E(self):
        """
        Effectue une rotation du dé vers l'est. Met à jour les listes 'EW' et 'NS' en conséquence.
        Après la rotation :
            - La face de l'est devient le dessus,
            - La face du dessous devient l'ouest, etc.
        """
        tail = self.EW.pop()        # Retire la face 'west'
        self.EW.insert(0, tail)     # Met la face 'west' sur le dessus
        self.NS[0] = self.EW[0]     # Synchronise la face du dessus sur NS
        self.NS[2] = self.EW[2]     # Synchronise la face du dessous sur NS

if __name__ == '__main__':
    # Lecture des identifiants de faces du dé en entrée (ordre : [top, south, east, west, north, bottom])
    dnum = input().split()
    # Pour chaque question posée...
    for _ in range(int(input())):
        # Lecture de la face du dessus et de la face de devant
        t, f = input().split()
        # On détermine la valeur à droite de 'f' quand 't' est en haut
        dice = Dice()
        right_index = dice.question(dnum.index(t) + 1, dnum.index(f) + 1)
        print(dnum[right_index - 1])