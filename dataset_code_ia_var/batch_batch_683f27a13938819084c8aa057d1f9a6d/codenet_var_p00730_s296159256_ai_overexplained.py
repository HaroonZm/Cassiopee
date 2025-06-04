# Importation de la fonction setrecursionlimit depuis le module sys
# Cette fonction permet de spécifier la profondeur maximale de récursion pour éviter un dépassement de pile (stack overflow)
from sys import setrecursionlimit

# Appel de la fonction setrecursionlimit pour définir une limite très élevée (100000)
# Cela permet de garantir que, même en cas de récursion profonde, le programme ne s'arrêtera pas prématurément
setrecursionlimit(100000)

# Définition d'une classe pour modéliser le gâteau (Cake)
class Cake():

    # Méthode d'initialisation appelée lors de la création d'un objet Cake
    # Prend en entrée : N (nombre de coupes à effectuer), W (largeur initiale), D (longueur initiale)
    def __init__(self, N, W, D):
        # Initialisation d'une liste P, qui servira à enregistrer le parent de chaque morceau (pour représenter l'arbre des découpes)
        # On double la taille pour anticiper le nombre de morceaux après toutes les découpes (chaque découpe pouvant doubler le nombre de morceaux)
        # Chaque valeur est initialisée à -1 pour signaler l'absence de parent (valeur sentinelle)
        self.P = [-1] * 2 * (N+1)

        # De même, initialisation d'une liste L, qui stockera l'indice du morceau de gauche (fils gauche)
        # Valeur initiale à -1 pour indiquer qu'il n'y a pas encore eu de découpe sur ce morceau
        self.L = [-1] * 2 * (N+1)

        # Initialisation de la liste R pour les fils droits, fonctionnement similaire à L
        self.R = [-1] * 2 * (N+1)

        # Initialisation de la liste W qui contiendra la largeur de chaque morceau après chaque découpe
        # On met tous les éléments à 0 puis on place la largeur initiale sur le morceau numéro 1 (indice 1)
        self.W = [0] * 2 * (N+1)
        self.W[1] = W

        # De même, initialisation de la liste D qui contiendra la longueur (ou profondeur) de chaque morceau
        self.D = [0] * 2 * (N+1)
        self.D[1] = D

    # Méthode pour retrouver le numéro (indice) du morceau correspondant à la p-ième pièce non encore découpée
    def find(self, target):
        # On démarre un compteur pour compter les morceaux non découpés (c-à-d n'ayant pas encore de fils gauche)
        count = 0
        # On parcourt tous les indices des morceaux, en commençant à 1 jusqu'à 2*N+1 inclus
        # Cela suffit puisque le nombre de pièces après N découpes ne dépassera jamais 2N+1
        for i in range(1, 2*N+2):
            # Si L[i] vaut -1, cela signifie que le morceau numéro i n'a pas encore été découpé,
            # donc c'est un morceau encore "entier"
            count += (self.L[i] == -1)
            # Quand on a trouvé le p-ième (target) morceau non découpé, on retourne son indice i
            if count == target:
                return i

    # Méthode pour effectuer une découpe sur un morceau spécifique
    # target est l'indice du morceau à découper, s est la position de la coupe, l est l'indice du futur premier nouveau morceau
    def cut(self, target, s, l):
        # On récupère la largeur (w) et la longueur (d) du morceau cible à découper
        w = self.W[target]
        d = self.D[target]
        # On calcule le périmètre total sur lequel on peut faire la découpe (contour du morceau dans ce problème)
        L = w + d
        # On ajuste s pour qu'il soit dans l'intervalle [0, L-1]
        s %= L

        # Si la coupe tombe sur la largeur (première phase du périmètre)
        if s <= w:
            # On divise la largeur en deux morceaux, la coupe étant placée à s (distance depuis le bord)
            nw, nW = s, w-s
            # Si le premier morceau est plus grand que le deuxième, on échange pour garantir l'ordre croissant
            if nw > nW:
                nw, nW = nW, nw
            # Les longueurs restent identiques, car la coupe est parallèle à la largeur
            nd, nD = d, d
        else:
            # Sinon, la découpe est sur la longueur (après la largeur)
            s -= w  # On réajuste la position de la découpe dans la partie longueur
            # On divise la longueur en deux morceaux
            nd, nD = s, d-s
            # On ordonne nd et nD pour que nd soit toujours inférieur ou égal à nD
            if nd > nD:
                nd, nD = nD, nd
            # La largeur reste la même pour les deux nouveaux morceaux
            nw, nW = w, w

        # On effectue des vérifications pour s'assurer que la découpe ne donne pas de morceau de taille nulle ou négative
        assert 0 < nw
        assert 0 < nd

        # Création de deux nouveaux morceaux : les indices utilisés sont l et r (r = l + 1)
        r = l + 1

        # Mise à jour des pointeurs des morceaux dans l'arbre de découpe
        # L'enfant gauche et droit du morceau target deviennent l et r respectivement
        self.L[target], self.R[target] = l, r
        # On enregistre le parent de l et r comme étant target
        self.P[l], self.P[r] = target, target
        # On enregistre les nouvelles largeurs pour les morceaux l et r
        self.W[l], self.W[r] = nw, nW
        # ...ainsi que leurs longueurs
        self.D[l], self.D[r] = nd, nD

    # Méthode pour afficher les aires (surface) de tous les morceaux de gâteau qui n'ont jamais été découpés
    def show(self):
        # Création d'une liste temporaire pour stocker les aires
        tmp = []
        # On parcourt tous les morceaux du gâteau
        for i in range(1, len(self.L)):
            # Si le morceau n'a pas été découpé (L[i] == -1), c'est une feuille de l'arbre des découpes
            if self.L[i] == -1:
                # On calcule l'aire du morceau (largeur * longueur) et on l'ajoute à la liste tmp
                tmp.append(self.W[i] * self.D[i] )
        # On trie la liste des aires dans l'ordre croissant puis on convertit chaque nombre en chaîne et imprime le tout
        print(" ".join(map(str, sorted(tmp))))

# Lecture des paramètres initiaux : N = nombre de découpes à effectuer, W = largeur initiale, D = longueur initiale
N, W, D = map(int, input().split())

# Boucle principale du programme, qui traite plusieurs ensembles de données si nécessaire
while W:
    # Création d'un objet Cake avec les valeurs initiales lues
    cake = Cake(N, W, D)
    # On répète la découpe N fois comme demandé
    for i in range(N):
        # Lecture des paramètres de la découpe : p = position du morceau (selon la numérotation donnée dans find), s = position de la coupe
        p, s = map(int, input().split())
        # Recherche de l'indice du p-ième morceau non encore découpé
        target = cake.find(p)
        # On effectue la coupe, les indices l (et l+1) sont alloués pour les deux nouveaux morceaux crées
        # l = 2*(i+1), c'est-à-dire, pour chaque découpe, on préalloue deux index uniques pour les nouveaux morceaux
        cake.cut(target, s, 2*(i+1))
    # Après toutes les découpes, on affiche les aires des morceaux restants
    cake.show()
    # Lecture du prochain jeu de paramètres pour éventuellement traiter une nouvelle instance du problème
    N, W, D = map(int, input().split())