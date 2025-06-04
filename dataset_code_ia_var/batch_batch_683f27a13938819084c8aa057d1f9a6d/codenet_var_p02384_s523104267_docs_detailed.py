class Dice:
    """
    Classe représentant un dé à six faces, qui permet de simuler ses mouvements (rotations) et d'interroger ses faces.
    
    Attributs
    ----------
    pip : list[int]
        Liste représentant les valeurs numériques sur les six faces du dé. 
        L'ordre des indices est le suivant: 
        0: haut, 1: face avant, 2: droite, 3: gauche, 4: face arrière, 5: bas.
    """
    def __init__(self, pip):
        """
        Initialise une instance de la classe Dice avec une configuration des faces donnée.
        
        Paramètres
        ----------
        pip : list[int]
            Liste de 6 entiers représentant les valeurs sur les faces du dé dans l'ordre:
            [haut, avant, droite, gauche, arrière, bas]
        """
        self.pip = pip

    def move(self, dir):
        """
        Effectue une rotation du dé dans une direction donnée.
        
        Paramètres
        ----------
        dir : str
            La direction dans laquelle faire tourner le dé.
            Les directions possibles sont:
                - 'E' : rotation vers l'est (droite)
                - 'W' : rotation vers l'ouest (gauche)
                - 'N' : rotation vers le nord (vers le haut)
                - 'S' : rotation vers le sud (vers le bas)
        
        Cette méthode modifie la liste self.pip pour refléter la nouvelle orientation du dé.
        """
        if str(dir) == "E":
            # Rotation vers l'est: le dessus devient la gauche, la gauche devient le bas, le bas devient la droite, la droite devient le dessus
            self.pip[0], self.pip[2], self.pip[3], self.pip[5] = self.pip[3], self.pip[0], self.pip[5], self.pip[2]
        elif str(dir) == "W":
            # Rotation vers l'ouest: le dessus devient la droite, la droite devient le bas, le bas devient la gauche, la gauche devient le dessus
            self.pip[0], self.pip[2], self.pip[3], self.pip[5] = self.pip[2], self.pip[5], self.pip[0], self.pip[3]
        elif str(dir) == "N":
            # Rotation vers le nord: le dessus devient l'avant, l'avant devient le bas, le bas devient l'arrière, l'arrière devient le dessus
            self.pip[0], self.pip[1], self.pip[4], self.pip[5] = self.pip[1], self.pip[5], self.pip[0], self.pip[4]
        elif str(dir) == "S":
            # Rotation vers le sud: le dessus devient l'arrière, l'arrière devient le bas, le bas devient l'avant, l'avant devient le dessus
            self.pip[0], self.pip[1], self.pip[4], self.pip[5] = self.pip[4], self.pip[0], self.pip[5], self.pip[1]

# Lecture de la configuration initiale du dé
# L'utilisateur saisit 6 entiers correspondant aux faces du dé
d = Dice(list(map(int, input().split())))

# Lecture du nombre de requêtes à traiter
n = int(input())

# Pour chaque requête, trouver la valeur sur la face droite donné le dessus et la face avant
for i in range(n):
    # Lecture de la configuration recherchée: valeur sur la face du dessus et la face avant
    top, front = map(int, input().split())

    # On applique une séquence de mouvements qui place systématiquement toutes les faces en haut au cours du processus
    # Cette séquence permet d'atteindre n'importe quelle orientation
    for op in "EEENEEENEEESEEESEEENEEEN":
        # Si les faces du dessus et avant correspondent à la demande de la requête, on s'arrête
        if d.pip[0] == top and d.pip[1] == front:
            break
        # Sinon, on effectue la rotation selon le caractère de la séquence
        d.move(op)
    # On affiche la valeur sur la face droite pour l'orientation trouvée
    print(d.pip[2])