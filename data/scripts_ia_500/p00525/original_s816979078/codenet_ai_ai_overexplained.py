import math

# Définition d'une classe appelée seg_tree, qui représente un arbre de segment (une structure de données efficace pour les requêtes de plages)
class seg_tree:
    # Initialisation de l'arbre de segment avec un paramètre n, qui représente la taille de la donnée originale
    def __init__(self, n):
        # Calcul de la profondeur de l'arbre (nombre de niveaux) en prenant le logarithme base 2 de n, puis en arrondissant vers le haut
        self.depth = math.ceil(math.log(n, 2))
        # Calcul de la taille réelle de l'arbre en décalant 1 à gauche de depth bits (équivalent à 2 puissance depth)
        self.size = 1 << self.depth
        # Initialisation d'une liste bit de taille double de size, remplie de zéros, qui stockera les valeurs cumulées aux feuilles et nœuds
        self.bit = [0] * 2 * self.size
        # Initialisation d'une autre liste renew de la même taille, pour marquer certains intervalles comme "à renouveler" (un indicateur binaire)
        self.renew = [0] * 2 * self.size

    # Fonction pour ajouter une valeur v à la position p (dans l'arbre)
    def add(self, p, v):
        # On déplace p à la position correspondant aux feuilles (décalage)
        p += self.size
        # Tant que p n'est pas nul (tant que l'on n'a pas atteint la racine)
        while p:
            # On ajoute la valeur v à la position p dans bit
            self.bit[p] += v
            # On remonte d'un niveau dans l'arbre en effectuant un décalage à droite (division par 2 entière)
            p >>= 1

    # Fonction pour interroger la somme des valeurs dans l'intervalle [l, r)
    def query(self, l, r):
        # On décale les indices l et r vers les feuilles
        l += self.size
        r += self.size
        # Initialisation du résultat à zéro (variable accumulatrice)
        ret = 0

        # Tant que la borne gauche est strictement inférieure à la borne droite
        while l < r:
            # Si l est impair (dernier bit à 1), on ajoute la valeur à bit[l] puis on décale l vers la droite
            if l & 1:
                ret += self.bit[l]
                l += 1
            # Si r est impair (position juste avant r-1), on décrémente r et ajoute bit[r]
            if r & 1:
                r -= 1
                ret += self.bit[r]
            # Remonter d'un niveau dans l'arbre (division entière par 2)
            l >>= 1
            r >>= 1
        # Retourner la somme cumulative calculée pour l'intervalle
        return ret

    # Fonction pour marquer un intervalle [l, r) comme à renouveler dans renew
    def set_renew(self, l, r):
        # Décalage des indices vers la feuille correspondante
        l += self.size
        r += self.size

        # Tant que l < r, on parcourt l'arbre en touchant les intervalles correspondants
        while l < r:
            # Si l est impair, on marque la position l dans renew comme 1 (renouveler)
            if l & 1:
                self.renew[l] = 1
                l += 1
            # Si r est impair, on décrémente r et marque renew[r] comme 1 également
            if r & 1:
                r -= 1
                self.renew[r] = 1
            # On remonte dans l'arbre pour l et r
            l >>= 1
            r >>= 1

    # Fonction qui vérifie si une position p doit être renouvelée
    def is_renew(self, p):
        # Décalage de p vers la feuille
        p += self.size
        # Tant que p n'a pas atteint la racine
        while p:
            # Si la position p dans renew est marquée, retourne True immédiatement
            if self.renew[p]:
                return True
            # Sinon, remonte d'un niveau dans l'arbre (division entière par 2)
            p >>= 1
        # Aucune marque trouvée, retourne False
        return False

    # Fonction pour enlever la marque de renouvellement d'une position p, et propager les modifications dans renew
    def unset_renew(self, p):
        # Décalage p vers la feuille correspondante
        p += self.size
        # On itère des niveaux supérieurs à la position p, de la profondeur-1 jusqu'à 1
        for i in range(self.depth - 1, 0, -1):
            # On obtient la position de l'ancêtre à ce niveau (p >> i)
            if self.renew[p >> i]:
                # Si cet ancêtre est marqué dans renew, on enlève cette marque
                self.renew[p >> i] = 0
                # Et on marque ses deux enfants directs comme devant être renouvelés
                self.renew[(p >> i) * 2] = 1
                self.renew[(p >> i) * 2 + 1] = 1
        # Finalement, on enlève la marque de renouvellement pour la position p elle-même
        self.renew[p] = 0

    # Fonction pour trouver la plus grande position à gauche inférieure à r qui contient une valeur non nulle dans bit
    def get_lf(self, r):
        # l est initialisé à la taille de l'arbre (le niveau feuille le plus à gauche)
        l = self.size
        # Décalage de la borne r vers la feuille
        r += self.size
        # Tant que l est strictement inférieur à r
        while l < r:
            # Si r est impair (cad la position avant r est candidate)
            if r & 1:
                r -= 1
                # Si bit[r] est non nul (alors on a trouvé un élément significatif)
                if self.bit[r]:
                    # On va descendre dans l'arbre pour trouver la feuille exacte sur cette branche droite
                    while r < self.size:
                        r <<= 1
                        # Si le fils droit a une valeur, on se décale à droite (pour toujours chercher la feuille la plus à droite)
                        if self.bit[r + 1]:
                            r += 1
                    # Retourne l'indice correspondant à la feuille (décalage pour obtenir l'indice dans la base des données originales)
                    return r - self.size
            # Si l est impair, on l'incrémente pour passer au frère suivant
            if l & 1:
                l += 1
            # On remonte d'un niveau pour l et r (division entière par 2)
            l >>= 1
            r >>= 1
        # Si aucun index trouvé, retourne -1 pour signifier absence d'éléments valides
        return -1


# Importation de la classe UserList qui permet de créer une liste personnalisée
from collections import UserList

# Définition d'une classe union_find qui étend UserList, pour gérer une structure d'union-find (ou arbre disjoint)
class union_find(UserList):
    # Initialisation, utilise celle de UserList
    def __init__(self):
        UserList.__init__(self)

    # Fonction racine (root), trouve la racine représentant l'ensemble contenant l'élément p
    def root(self, p):
        # Si la valeur à la position p est négative, c'est une racine et sa valeur représente la taille négative de l'ensemble
        if self.data[p] < 0:
            return p
        # Sinon, la valeur stockée pointe vers un parent indirect, on applique récursivement root (compression de chemin)
        self.data[p] = self.root(self.data[p])
        # Retourner le représentant de l'ensemble (racine)
        return self.data[p]

    # Fonction pour unir les ensembles contenant p et q
    def join(self, p, q):
        # Trouver les racines des deux éléments
        p, q = self.root(p), self.root(q)

        # Si elles sont identiques, fusion impossible, retourne False
        if p == q:
            return False
        # Assurer que p est la plus petite racine (en terme de taille négative) pour équilibrer
        if self.data[p] < self.data[q]:
            p, q = q, p
        # Fusionner les ensembles en mettant p comme enfant de q, et mettre à jour la taille
        self.data[p], self.data[q] = self.data[q], p
        # Retourner True parce que la fusion a eu lieu
        return True

# Fonction bisect qui réalise une recherche dichotomique dans une liste triée a pour trouver la position d'insertion de v
def bisect(a, v):
    # Initialisation des bornes gauche (l) et droite (r)
    l, r = 0, len(a)
    # Tant que l est inférieur à r
    while l < r:
        # Calcul du milieu m, division entière
        m = (l + r) // 2
        # Si l'élément du milieu est strictement inférieur à v on avance la borne gauche
        if a[m] < v:
            l = m + 1
        else:
            # Sinon on décale la borne droite vers m
            r = m
    # Retourne la position d'insertion trouvée
    return l

# Fonction adjust qui adapte l'arbre segment et l'union-find pour un certain index p selon la condition is_renew
def adjust(seg, uf, target, p):
    # Si la position p est marquée pour renouvellement dans l'arbre segment
    if seg.is_renew(p):
        # On ajoute un nouvel ensemble isolé dans union-find (initialisé à -1 donc racine)
        uf.append(-1)
        # On enlève la marque de renouvellement pour p
        seg.unset_renew(p)
        # On met à jour le tableau target pour p avec l'indice du nouvel ensemble créé
        target[p] = len(uf) - 1

# Importation de itemgetter pour trier plus facilement
from operator import itemgetter

# Fonction principale qui traite l'entrée pour générer le résultat demandé
def main(f):
    # Lecture des entiers w, h et n représentant respectivement largeur, hauteur et nombre de segments (rectangles)
    w, h, n = map(int, f.readline().split())
    # Lecture d'une liste de listes contenant 4 entiers par ligne (représente abscisses et ordonnées de segments)
    abcd = [list(map(int, line.split())) for line in f]

    # Ajout à abcd des 4 segments représentant les bords du rectangle global (cadre)
    abcd.extend([
        [0, 0, w, 0],
        [0, 0, 0, h],
        [w, 0, w, h],
        [0, h, w, h]
    ])

    # Construction d'un dictionnaire xs qui mappe chaque coordonnée x unique à un indice ordinal à partir d'un ensemble trié
    xs = {x: i for i, x in enumerate(sorted(set([abcdi[0] for abcdi in abcd] + [abcdi[2] for abcdi in abcd] + [-1])))}
    # Remplacement dans abcd des abscisses (a, c) par leurs indices normalisés via xs pour uniformiser et faciliter les opérations sur les indices
    abcd = [(xs[a], b, xs[c], d) for a, b, c, d in abcd]

    # Initialisation de la liste target avec -1 pour 2 * n éléments (destinée à stocker des indices d'ensemble uf associés aux positions)
    target = [-1] * n * 2
    # Ciblage spécifique de target[0] à 0 (point de départ spécial)
    target[0] = 0

    # Initialisation d'un union-find
    uf = union_find()
    # Ajout d'un ensemble isolé initial avec valeur -1
    uf.append(-1)

    # Création d'un arbre segment de taille nombre d'abscisses uniques
    seg = seg_tree(len(xs))
    # Ajout d'une valeur 1 à l'indice 0 (initialisation dans l'arbre segment)
    seg.add(0, 1)

    # Création d'une liste a, qui va contenir des évènements
    a = []
    # Parcours de chaque segment dans abcd
    for x1, y1, x2, y2 in abcd:
        # Si le segment est vertical (même abscisse de départ et d'arrivée)
        if x1 == x2:
            # Ajouter à la liste des évènements de début et fin d'intervalle vertical
            a.append((y1, 0, x1, -1))  # 0 indique début
            a.append((y2, 2, x1, -1))  # 2 indique fin
        else:
            # Sinon, segment horizontal, ajouter un évènement d'action 1 avec les bornes horizontales
            a.append((y1, 1, x1, x2))
    # Trie les événements par la première clé y puis action act (pour garder un ordre stable dans les traitements)
    a.sort(key=itemgetter(0, 1))

    # Initialisation d'un compteur ret qui va accumuler le résultat final
    ret = 0
    # Parcours de chaque événement trié
    for _, act, left, right in a:
        # Si action est 0 (début segment vertical)
        if act == 0:
            # Trouver la plus grande position à gauche inférieure à left contenant une valeur dans le segment tree
            lf = seg.get_lf(left)

            # Adapter la structure pour les deux indices
            adjust(seg, uf, target, lf)
            adjust(seg, uf, target, left)
            # Affecter target[left] à target[lf], crée une forme de liaison d'ensemble
            target[left] = target[lf]

            # Ajouter 1 dans l'arbre segment à la position left
            seg.add(left, 1)

        # Si action est 1 (segment horizontal)
        elif act == 1:
            # Comptage du nombre d'éléments dans l'intervalle [left, right + 1]
            count = seg.query(left, right + 1)
            # Si la quantité est inférieure à 2, aucun processus n'est nécessaire
            if count < 2:
                continue
            # Sinon, augmenter ret de count - 1 (en fait on compte les connexions supplémentaires)
            ret += count - 1

            # Marque l'intervalle [left, point trouvé par get_lf(right + 1)) comme renouvelé dans l'arbre segment
            seg.set_renew(left, seg.get_lf(right + 1))

        # Si action est 2 (fin segment vertical)
        elif act == 2:
            # Retrouver la position à gauche inférieure à left
            lf = seg.get_lf(left)
            # Ajuster structure pour ces positions
            adjust(seg, uf, target, lf)
            adjust(seg, uf, target, left)
            # Si les ensembles représentés par target[lf] et target[left] peuvent être fusionnés, diminuer ret (car suppression de recouvrement)
            if uf.join(target[lf], target[left]):
                ret -= 1
            # Soustraire 1 dans l'arbre segment à la position left (indiquant fin du segment vertical)
            seg.add(left, -1)

    # Affiche le résultat final calculé
    print(ret)

# Importation du module sys pour lire l'entrée standard
import sys
# Assignation du flux d'entrée standard à la variable f
f = sys.stdin

# Lancement de la fonction principale avec le flux d'entrée f
main(f)