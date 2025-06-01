import sys

# Augmente la limite de récursion pour permettre des appels récursifs profonds
sys.setrecursionlimit(100000)

def resolve():
    """
    Fonction principale qui résout le problème donné en lisant des entrées jusqu'à 
    ce que n soit égal à 0. Pour chaque cas, elle calcule le nombre minimal de 
    mouvements requis selon certaines règles et affiche le résultat ou -1 si le 
    nombre dépasse une limite donnée.
    """

    def toC(A, B, C):
        """
        Calcule récursivement le nombre minimal de mouvements nécessaires pour 
        déplacer des "gobelets" représentés par des bits dans les entiers A, B, 
        et C vers une configuration cible.

        Args:
            A (int): Un entier dont les bits représentent la présence de gobelets 
                     dans la première pile.
            B (int): Même chose pour la deuxième pile.
            C (int): Même chose pour la troisième pile.

        Returns:
            int: Le nombre minimal de déplacements nécessaires.
        """
        # Cas de base : s'il n'y a plus de gobelets dans A ni B, aucun mouvement nécessaire
        if not (A or B):
            return 0

        # Si le gobelet le moins significatif est dans C (C & 1),
        # on ignore ce gobelet et on décale de 1 bit vers la droite
        if C & 1:
            return toC(A >> 1, B >> 1, C >> 1)  # Ne pas considérer ce gobelet dans C

        # Si le gobelet le moins significatif est dans B,
        # on applique une séquence de mouvements spécifiques
        if B & 1:
            return (toC(C >> 1, B >> 1, A >> 1)  # Déplacer temporairement vers l'autre côté
                    + toC((A | B | C) >> 1, 0, 0)  # Ramener les gobelets de l'autre côté
                    + 1)  # Compter le déplacement de B vers C

        # Si le gobelet le moins significatif est dans A,
        # on applique une autre séquence de mouvements plus complexe
        if A & 1:
            return (toC(A >> 1, B >> 1, C >> 1)  # Regrouper tous vers C
                    + 2 * toC((A | B | C) >> 1, 0, 0)  # Deux déplacements de bout en bout
                    + 2)  # Deux mouvements : A vers B puis B vers C

    while True:
        # Lecture des entiers n et m
        n, m = map(int, input().split())

        # Initialisation des piles des gobelets (représentées en bits dans des entiers)
        cup = [0 for _ in range(3)]

        # Condition de terminaison si n == 0
        if n == 0:
            return

        # Lecture des trois piles avec leurs gobelets
        for i in range(3):
            a = list(map(int, input().split()))
            # Pour chaque gobelet dans la pile, on place un bit à 1 correspondant
            for s in a[1:]:
                cup[i] |= 1 << (s - 1)

        # Calcul du nombre minimal de déplacements soit dans l'ordre initial soit inversé
        a = min(toC(*cup), toC(*reversed(cup)))

        # Affichage du nombre minimum s'il ne dépasse pas m, sinon -1
        print(a if a <= m else -1)

if __name__ == "__main__":
    resolve()