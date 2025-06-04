# 定義 d'un class Dice ("Dé") qui représente un dé à six faces avec des méthodes de manipulation et de comparaison.
class Dice:
    # Le constructeur (__init__) prend une liste 'l' qui représente les valeurs sur les 6 faces du dé.
    # L'ordre des faces est important : U (Up/Top), S (South), E (East), W (West), N (North), D (Down/Bottom)
    def __init__(self, l):
        # Attribut d'instance 'f' : liste contenant les valeurs des faces selon l'ordre spécifié.
        self.f = l

    # Méthode spéciale __str__ pour définir la façon dont une instance de Dice est affichée avec print().
    def __str__(self):
        l = self.f  # Obtenir la liste des faces.
        # Construire une chaîne de caractères en affichant la valeur de chaque face du dé.
        # f-string permet d'insérer facilement les valeurs des faces dans la chaîne.
        s = f'[U:{l[0]},S:{l[1]},E:{l[2]},W:{l[3]},N:{l[4]},D:{l[5]}]'
        return s  # Retourne la chaîne formatée.

    # Méthode pour faire rouler le dé dans l'une des quatre directions cardinales : Nord (N), Sud (S), Est (E), Ouest (W).
    def roll(self, c):
        # Selon le caractère 'c', déterminer comment les indices des faces changent après la rotation.
        # Chaque direction correspond à une permutation des indices.
        if c == 'N':
            # Rouler vers le Nord : les indices des faces changent de cette façon.
            ni = [1, 5, 2, 3, 0, 4]
        elif c == 'S':
            # Rouler vers le Sud.
            ni = [4, 0, 2, 3, 5, 1]
        elif c == 'E':
            # Rouler vers l'Est.
            ni = [3, 1, 0, 5, 4, 2]
        elif c == 'W':
            # Rouler vers l'Ouest.
            ni = [2, 1, 5, 0, 4, 3]
        # Applique la permutation : reconstitue la liste des faces après la rotation.
        self.f = [self.f[j] for j in ni]

    # Méthode pour tourner le dé autour de l'axe vertical (vue du dessus, faire pivoter le dé sur place sans le déplacer).
    # r == +1 : tourner vers la gauche (sens antihoraire, "vers l'ouest" quand vu du dessus)
    # r == -1 : tourner vers la droite (sens horaire, "vers l'est" quand vu du dessus)
    def rotate(self, r):
        if r == +1:  # Sens antihoraire.
            # Changement d'indices des faces selon la rotation demandée.
            ni = [0, 3, 1, 4, 2, 5]
        elif r == -1:  # Sens horaire.
            ni = [0, 2, 4, 1, 3, 5]
        # Appliquer la permutation des faces pour simuler la rotation.
        self.f = [self.f[j] for j in ni]

    # Méthode qui génère et retourne une liste de toutes les configurations possibles du dé par roulement et rotation.
    # Cela permet de parcourir toutes les orientations possibles (24) d'un dé à 6 faces.
    def patterns(self):
        # Créer une liste vide pour contenir chaque configuration unique de faces du dé.
        fs = []
        # Pour chaque face comme "haut" du dé (6 possibilités) :
        for i in range(6):
            # Pour les faces paires (0,2,4), rouler vers le Nord ; pour les impaires (1,3,5), rouler vers l'Est.
            if i % 2 == 0:
                self.roll('N')  # Rouler vers le nord.
            else:
                self.roll('E')  # Rouler vers l'est.
            # Pour chacune des 4 orientations autour de la verticale (0°, 90°, 180°, 270°) :
            for j in range(4):
                self.rotate(+1)  # Tourner vers la gauche (antihoraire).
                # Ajouter la configuration courante des faces à la liste.
                fs.append(self.f)
        # Retourner la liste de toutes les configurations collectées.
        return fs

    # Cette méthode cherche (dans toutes les orientations possibles du dé) une configuration où les faces U et S valent l'entrée l[0], l[1].
    # Si trouvée, retourne la valeur de la face E (East) dans cette configuration.
    def lookEast(self, l):
        # Parcourir tous les arrangements de faces possibles.
        for f in self.patterns():
            # Si la face du haut (U) et la face du sud (S) correspondent à celles données en argument :
            if f[0] == l[0] and f[1] == l[1]:
                return f[2]  # Retourner la valeur de la face Est.

    # Méthode pour comparer ce dé avec un autre dé d (instance de Dice), indépendamment de leur orientation.
    # Retourne True si une orientation du second dé correspond exactement à celle du premier.
    def equals(self, d):
        # Pour chaque orientation possible du dé courant :
        for f in self.patterns():
            # Si cette configuration correspond exactement à celle de l'autre dé (d.f) :
            if f == d.f:
                return True  # Les dés sont égaux pour au moins une orientation.
        return False  # Sinon, ils sont différents dans toutes les orientations.

# Lecture du nombre de dés à traiter depuis l'entrée standard. L'utilisateur doit entrer un nombre entier.
n = int(input())
# Lecture de la configuration du premier dé : une ligne des 6 nombres séparés par des espaces.
# map(int, input().split()) transforme chaque chaîne lue en entier, puis list() crée une liste avec ces valeurs.
d0 = Dice(list(map(int, input().split())))
flag = True  # On suppose par défaut que tous les dés sont différents (pas de doublons).

# Boucle pour lire les n-1 autres dés et les comparer au premier.
for i in range(n-1):
    # Lecture d'un dé, conversion en instance de Dice.
    d = Dice(list(map(int, input().split())))
    # Utilisation de la méthode equals pour comparer ce dé au premier (d0).
    if d0.equals(d):
        # S'ils sont équivalents dans une orientation, il y a au moins un doublon.
        flag = False  # Il existe au moins une paire de dés identiques sous rotation.
        break  # Inutile de vérifier les autres.

# Affichage : 'Yes' si tous les dés sont différents, 'No' s'il y a au moins un doublon.
print('Yes' if flag else 'No')