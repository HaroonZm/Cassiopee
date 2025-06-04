class Dice:
    # La classe Dice représente un dé standard à 6 faces.
    # Chaque face du dé possède une valeur spécifique.
    # Les 6 faces sont : dessus (top), sud (south), est (east), ouest (west), nord (north), dessous (bottom).
    # Les abréviations utilisées seront : t (top), s (south), e (east), w (west), n (north), b (bottom).

    def __init__(self, t, s, e, w, n, b):
        # __init__ est une méthode spéciale appelée constructeur en Python.
        # Elle est automatiquement appelée lors de l'instanciation d'un objet Dice.
        # Elle attend 6 arguments, traditionnellement notés self (pour l'instance créée), t, s, e, w, n, b représentant les valeurs de chaque face.

        # self est une référence à l'instance en elle-même (obligatoire dans toute méthode d'une classe).
        self.t = t  # face supérieure (top)
        self.s = s  # face sud (south)
        self.e = e  # face est (east)
        self.w = w  # face ouest (west)
        self.n = n  # face nord (north)
        self.b = b  # face inférieure (bottom)
        # rotway est un dictionnaire associant une direction à un entier (correspondant aux directions de rotation).
        # "S": Sud, "N": Nord, "E": Est, "W": Ouest.
        self.rotway = {"S": 0, "N": 1, "E": 2, "W": 3}

    def rot(self, way):
        # La méthode rot effectue une rotation du dé en fonction de la direction spécifiée par l'argument way.
        # way doit être un entier compris entre 0 et 3 inclus.
        # La rotation réaffecte les valeurs des différentes faces selon le mouvement :

        if way == 0:
            # way == 0 : rotation vers le sud (face nord vers le haut)
            # On affecte à chaque face sa nouvelle valeur après la rotation :
            # top devient north, south devient top, north devient bottom, bottom devient south, east et west ne changent pas.
            self.t, self.s, self.e, self.w, self.n, self.b = self.n, self.t, self.e, self.w, self.b, self.s
        elif way == 1:
            # way == 1 : rotation vers le nord (face sud vers le haut)
            # top devient south, south devient bottom, bottom devient north, north devient top, east et west ne changent pas.
            self.t, self.s, self.e, self.w, self.n, self.b = self.s, self.b, self.e, self.w, self.t, self.n
        elif way == 2:
            # way == 2 : rotation vers l'est (face ouest vers le haut)
            # top devient west, west devient bottom, bottom devient east, east devient top, south et north ne changent pas.
            self.t, self.s, self.e, self.w, self.n, self.b = self.w, self.s, self.t, self.b, self.n, self.e
        elif way == 3:
            # way == 3 : rotation vers l'ouest (face est vers le haut)
            # top devient east, east devient bottom, bottom devient west, west devient top, south et north ne changent pas.
            self.t, self.s, self.e, self.w, self.n, self.b = self.e, self.s, self.b, self.t, self.n, self.w

def main():
    # La fonction main sera appelée lors de l'exécution directe du script.
    # Elle contient la logique principale d'entrée, traitement et sortie du programme.

    import random  # On importe le module random pour générer des nombres aléatoires.

    n = int(input())  # On lit une ligne depuis l'entrée standard. Elle doit être convertie en entier. n représente le nombre de dés à traiter.

    # Création d'une liste à deux dimensions pour stocker les valeurs de chaque dé.
    # On crée une liste de n sous-listes, chacune contenant 6 zéros initialement.
    diceList = [[0 for _ in range(6)] for _ in range(n)]

    # Remplissage de diceList avec les valeurs des faces de chaque dé.
    for i in range(n):
        # Pour chaque dé (entier de 0 à n-1 inclus), on lit une ligne contenant 6 entiers séparés par des espaces.
        # map(int, input().split()) convertit chacun des 6 éléments saisis en int.
        diceList[i][0], diceList[i][1], diceList[i][2], diceList[i][3], diceList[i][4], diceList[i][5] = map(int, input().split())

    flag = 0  # flag est une variable booléenne utilisée comme indicateur. Si elle prend la valeur 1, cela signifie qu'au moins deux dés sont identiques.

    # Pour chaque dé à partir du second (index 1), on vérifie s'il est identique à un des précédents.
    for i in range(1, n):
        # Si flag est déjà à 1, cela signifie qu'on a trouvé une paire identique, on peut donc sortir de la boucle.
        if flag == 1:
            break
        else:
            # On crée un objet Dice pour le dé i (appelé dice_a), en passant les 6 valeurs appropriées.
            dice_a = Dice(
                diceList[i][0],
                diceList[i][1],
                diceList[i][2],
                diceList[i][3],
                diceList[i][4],
                diceList[i][5]
            )
            # Pour chaque dé précédent (index de 0 à i-1), on compare dice_a à dice_b (autre dé déjà saisi).
            for j in range(i):
                dice_b = Dice(
                    diceList[j][0],
                    diceList[j][1],
                    diceList[j][2],
                    diceList[j][3],
                    diceList[j][4],
                    diceList[j][5]
                )
                # On va faire jusqu'à 50 rotations aléatoires pour tester toutes les orientations possibles du dé dice_a.
                # Cette méthode probabiliste vise à détecter si deux dés sont identiques sous une quelconque orientation.
                for _ in range(50):
                    # On compare les 6 faces des deux dés.
                    # Si les 6 valeurs sont égales dans le même ordre, alors les deux dés sont équivalents sous rotation.
                    if (dice_a.t, dice_a.s, dice_a.e, dice_a.w, dice_a.n, dice_a.b) == (dice_b.t, dice_b.s, dice_b.e, dice_b.w, dice_b.n, dice_b.b):
                        flag = 1  # On a trouvé une correspondance.
                        break  # On n'a plus besoin de continuer à comparer ce dé à d'autres.
                    else:
                        # On génère un entier aléatoire entre 0 et 3 inclus, représentant une direction de rotation.
                        seed = random.randint(0, 3)
                        # On effectue une rotation du dé dice_a selon la direction choisie.
                        dice_a.rot(seed)
                # Si flag est passé à 1, on peut sortir de la boucle imbriquée suivante pour ne pas comparer davantage.
                if flag == 1:
                    break

    # À la fin, si flag est toujours à 0, aucun dé n'était identique à un autre, on affiche "Yes".
    if flag == 0:
        print("Yes")
    else:
        # Sinon, au moins une paire de dés est identique (même sous rotation), on affiche "No".
        print("No")

# __name__ est une variable spéciale en Python.
# Elle a la valeur "__main__" quand le script est exécuté directement (pas lors d'une importation comme module).
# Cela permet de contrôler l'exécution du code principal du programme.
if __name__ == '__main__':
    main()  # Appel de la fonction main si et seulement si le script est exécuté en tant que programme principal.