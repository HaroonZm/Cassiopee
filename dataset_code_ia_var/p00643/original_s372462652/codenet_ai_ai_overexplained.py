# Définition de six constantes (T, S, E, W, N, B) représentant les six faces d'un dé
# T : Top (dessus), S : South (sud), E : East (est), W : West (ouest), N : North (nord), B : Bottom (dessous)
# La fonction range(6) génère les entiers de 0 à 5, chacun assigné à une de ces directions
T, S, E, W, N, B = range(6)

# Déclaration de la classe Dice représentant un dé à six faces
class Dice:

    # Constructeur (__init__) appelé lors de la création d'une instance Dice
    def __init__(self):
        # Chaque face du dé aura un état. self.state est une liste contenant les valeurs initiales des faces 0 à 5
        self.state = list(range(6))

    # Méthode de comparaison d'égalité. Appelée par l'opérateur ==.
    # Retourne True si les états internes des deux dés sont identiques, sinon False
    def __eq__(self, dice):
        # Compare l'attribut state (liste) des deux objets Dice
        return self.state == dice.state

    # Méthode de comparaison "plus grand que". Appelée par l'opérateur >.
    # Compare les listes des états faces à faces selon l'ordre des indices.
    def __gt__(self, dice):
        return self.state > dice.state

    # Crée et retourne un nouvel objet Dice qui est une copie exacte de l'objet actuel (deep copy)
    def copy(self):
        dice = Dice()  # Crée une nouvelle instance Dice
        # Copie la liste des états de faces dans le nouvel objet, élément par élément
        dice.state = [x for x in self.state]
        return dice  # Retourne le nouvel objet Dice

    # Effectue une rotation cyclique des valeurs des faces du dé selon la liste de faces fournie
    # Le paramètre 'turn' est une liste de 4 indices indiquant l'ordre des faces à faire tourner
    def _turn(self, turn):
        # Sauvegarde temporairement la valeur de la dernière face de la rotation
        k = self.state[turn[-1]]
        # Fait tourner les valeurs des quatre faces selon l'ordre indiqué par turn
        for i in range(4):
            # Pour chaque face visitée, échange sa valeur avec la valeur sauvegardée
            self.state[turn[i]], k = k, self.state[turn[i]]

    # Effectue une rotation du dé vers le sud (déplacement d'une case vers le sud)
    def go_south(self):
        # Les indices des faces affectées par une rotation vers le sud
        turn = [T, S, B, N]
        # Effectue la rotation cyclique de ces faces
        self._turn(turn)

    # Effectue une rotation du dé vers le nord
    def go_north(self):
        turn = [N, B, S, T]
        self._turn(turn)

    # Effectue une rotation du dé vers l'est (droite)
    def go_east(self):
        turn = [T, E, B, W]
        self._turn(turn)

    # Effectue une rotation du dé vers l'ouest (gauche)
    def go_west(self):
        turn = [T, W, B, E]
        self._turn(turn)

    # Retourne la valeur de la face nord du dé (indice N)
    def north(self):
        return self.state[N]

    # Retourne la valeur de la face sud
    def south(self):
        return self.state[S]

    # Retourne la valeur de la face est
    def east(self):
        return self.state[E]

    # Retourne la valeur de la face ouest
    def west(self):
        return self.state[W]

    # Retourne la valeur de la face du dessous (bottom)
    def bottom(self):
        return self.state[B]

    # Retourne la valeur de la face du dessus (top)
    def top(self):
        return self.state[T]

    # Effectue le mouvement du dé selon l'indice n (0=ouest, 1=nord, 2=est, 3=sud)
    def goto(self, n):
        # Associe chaque direction (index 0 à 3) à la méthode de mouvement correspondante
        func = [self.go_west, self.go_north, self.go_east, self.go_south]
        # Appelle la fonction de déplacement appropriée
        func[n]()

    # Affiche l'état actuel du dé en associant chaque lettre à sa valeur
    def show(self):
        # Crée une liste de lettres représentant les faces dans l'ordre
        d = list("TSEWNB")
        # Parcourt chaque lettre et valeur de face (self.state)
        for x, s in zip(d, self.state):
            # Affiche la lettre et la valeur de la face correspondante
            print(x + " : {}".format(s))

# Importation du module heapq pour manipuler des files de priorité (tas binaire)
import heapq

# Constante représentant une valeur infinie (utilisée pour initialiser les coûts)
INF = 10**9

# Début du code principal, exécuté uniquement si ce fichier est exécuté comme programme principal
if __name__ == "__main__":
    # dx et dy sont des listes d'entiers permettant de calculer le déplacement en x et y
    # dx et dy représentent, pour chaque direction (0 à 3), comment la coordonnée change
    dx = [-1, 0, 1, 0]  # Variation de x : ouest, nord, est, sud
    dy = [0, -1, 0, 1]  # Variation de y : ouest, nord, est, sud (positions sont permutées, dépend du contexte)

    # Boucle principale, itère sur plusieurs jeux de données d'entrée tant que l'utilisateur ne donne pas h=0
    while True:
        # Définition et initialisation de la matrice 4D dp
        # dp[y][x][bottom][east] stocke le coût minimal pour arriver à (x, y) avec une certaine face dessous et une certaine face à l'est
        dp = [[[[INF for _ in range(6)] for i in range(6)] for j in range(10)] for k in range(10)]
        # Lecture de la hauteur (h) et largeur (w) de la grille depuis l'entrée utilisateur
        h, w = map(int, input().split())
        # Condition de sortie, si h est égal à zéro, on quitte la boucle principale
        if h == 0:
            break

        # Lecture du coût pour chaque case de la carte, pour h lignes de w entiers chacune
        cost = [list(map(int, input().split())) for _ in range(h)]
        # Lecture des coordonnées de départ (sy, sx) depuis l'entrée, format: ligne colonne
        sy, sx = map(int, input().split())
        # Lecture des coordonnées d'arrivée (gy, gx)
        gy, gx = map(int, input().split())
        # Initialisation de la file de priorité (min-heap) utilisée pour la recherche du plus court chemin
        q = []
        # Création du dé avec sa configuration de départ
        dice = Dice()
        # Insertion du point de départ dans la file de priorité avec coût 0
        # L'élément ajouté est une liste de 4 éléments : [coût total, position x, position y, objet dé]
        heapq.heappush(q, [0, sx, sy, dice])
        # Initialisation du coût dp du point de départ avec la configuration de départ du dé
        dp[sy][sx][dice.bottom()][dice.east()]

        # Initialisation de la réponse par défaut à une valeur supérieure à INF
        ans = INF+1

        # Boucle principale de la recherche de chemin (algorithme similaire à Dijkstra)
        # Tant que la file de priorité n'est pas vide
        while q:
            # Extraction du sommet du tas ayant le coût le plus bas
            c, x, y, dice = heapq.heappop(q)
            # Si la position extraite correspond à la destination
            if x == gx and y == gy:
                # On conserve le coût minimal trouvé
                ans = min(ans, c)
                # Passe à l'itération suivante sans voir plus loin
                continue
            # Si le coût de ce chemin est déjà plus grand ou égal à la meilleure solution trouvée, on stoppe ce chemin
            if c >= ans:
                continue
            else:
                # Pour chacune des 4 directions de mouvement possibles
                for i in range(4):
                    ddx, ddy = dx[i], dy[i]  # Calcul du déplacement en x et y pour la direction i
                    # Vérifie si la nouvelle position est à l'intérieur de la grille, sinon on continue
                    if x + ddx >= w or x + ddx < 0 or y + ddy >= h or y + ddy < 0:
                        continue
                    else:
                        # Crée une copie du dé pour simuler le mouvement (ne modifie pas le dé original)
                        d = dice.copy()
                        # Applique le mouvement/déplacement au dé dans la direction i
                        d.goto(i)
                        # Calcule le nouveau coût pour atteindre la nouvelle case
                        # (valeur de la face du dessous + 1) multipliée par le coût de la case cible
                        new_cost = c + (d.bottom()+1)*cost[y+ddy][x+ddx]
                        # Si ce nouveau chemin jusqu'à la position cible avec cette configuration de dé est plus économique que le précédent
                        if dp[y+ddy][x+ddx][d.bottom()][d.east()] > new_cost:
                            # Met à jour le tableau dp avec le nouveau coût le plus bas
                            dp[y+ddy][x+ddx][d.bottom()][d.east()] = new_cost
                            # Ajoute ce nouvel état dans la file de priorité pour exploration ultérieure
                            heapq.heappush(q, [new_cost, x+ddx, y+ddy, d])
        # Affiche la solution pour cette instance (coût minimal pour atteindre la destination)
        print(ans)