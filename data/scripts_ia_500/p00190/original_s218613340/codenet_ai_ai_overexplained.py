from math import factorial  # Importation de la fonction factorial permettant de calculer la factorielle d'un entier
from Queue import PriorityQueue  # Importation de la file de priorité (PriorityQueue) utilisée pour gérer les états selon leur coût estimé

# Pré-calcul des factorielles pour les entiers de 0 à 12 (inclus) afin d'optimiser les calculs ultérieurs
FACTORIAL = [factorial(i) for i in xrange(13)]

# Définition de constantes représentant les directions possibles afin d'améliorer la lisibilité du code
LEFT, UP, RIGHT, DOWN = 0, 1, 2, 3

# Initialisation d'une liste MOVE qui va contenir pour chaque position (de 0 à 12) les positions accessibles à gauche, en haut, à droite et en bas
# Ici on utilise une liste de listes: MOVE[i][direction] donne la nouvelle position à partir de i en direction donnée
MOVE = [[0] for u in xrange(13)]  # On crée une liste de 13 sous-listes initialement contenant [0] chacune

# Affectation des positions atteignables pour chaque case; -1 signifie qu'il n'y a pas de case dans cette direction
# Par exemple, depuis la position 0, à gauche (LEFT=0) il n'y a pas d'accès (-1), en haut pareil, mais en bas (DOWN=3) on peut aller à la position 2
MOVE[0] = [-1, -1, -1, 2]
MOVE[1] = [-1, -1, 2, 5]
MOVE[2] = [1, 0, 3, 6]
MOVE[3] = [2, -1, -1, 7]
MOVE[4] = [-1, -1, 5, -1]
MOVE[5] = [4, 1, 6, 9]
MOVE[6] = [5, 2, 7, 10]
MOVE[7] = [6, 3, 8, 11]
MOVE[8] = [7, -1, -1, -1]
MOVE[9] = [-1, 5, 10, -1]
MOVE[10] = [9, 6, 11, 12]
MOVE[11] = [10, 7, -1, -1]
MOVE[12] = [-1, 10, -1, -1]

def hash(cell):
    """
    Fonction de hachage qui transforme une configuration de 'cell' (liste d'entiers) en un entier unique.
    Cette fonction utilise une technique de hachage basée sur les factorielles pour générer un identifiant unique,
    souvent utilisée pour gérer les permutations de positions.
    """
    work = cell[:]  # On crée une copie indépendante de la liste cell pour ne pas modifier l'original
    hash = 0  # Initialisation du hash à zéro
    # Parcours des 12 premiers éléments (indices 0 à 11)
    for i in xrange(12):
        # Ajout au hash de la valeur courante pondérée par la factorielle correspondante
        hash += work[i] * FACTORIAL[13-1 - i]
        # Ajustement des valeurs dans work pour tenir compte des permutations précédentes
        # Cela permet de gérer correctement le calcul du rang de la permutation
        for ii in xrange(i+1, 13):
            if work[ii] > work[i]:
                work[ii] -= 1  # On décrémente la valeur si elle est plus grande que work[i]
    return hash  # On retourne la valeur entière calculée qui correspond au hachage unique

def dehash(key):
    """
    Fonction inverse de hash: elle prend un entier 'key' et reconstitue la liste cell correspondante,
    c'est-à-dire la configuration représentée par ce hash.
    """
    cell = []  # Initialisation d'une liste vide qui contiendra la configuration reconstituée
    # On calcule successivement les valeurs à chaque position
    for i in xrange(13):
        val = key / FACTORIAL[13-1 - i]  # Division entière pour obtenir le coeff à cette position
        cell.append(val)  # On ajoute cette valeur à la configuration
        key %= FACTORIAL[13-1 - i]  # On réduit key pour la prochaine itération
    # On ajuste les valeurs pour retrouver la permutation originale en inversant le procédé de la fonction hash
    for i in xrange(13-1, -1, -1):
        for ii in xrange(i+1, 13):
            if cell[i] <= cell[ii]:
                cell[ii] += 1  # Incrémenter les valeurs plus grandes ou égales pour corriger les indices
    return cell  # Retour de la configuration reconstituée sous forme de liste

def evaluate(cell):
    """
    Fonction d'évaluation heuristique qui calcule la distance totale que chaque élément 'cell[i]' doit parcourir
    pour atteindre sa position cible 'i', en utilisant les coordonnées définies dans 'point'.
    Seules les positions différentes de 0 ou 12 sont évaluées.
    """
    # Définit la position cible (x,y) pour chacun des 13 éléments dans un espace 2D (liste de listes)
    point = [
        [0, 2],
        [1, 1], [1, 2], [1, 3],
        [2, 0], [2, 1], [2, 2], [2, 3], [2, 4],
        [3, 1], [3, 2], [3, 3],
        [4, 2]
    ]
    eva = 0  # Variable accumulant la somme des distances (évaluation) initialisée à zéro
    # Pour chaque position de 0 à 12 (inclus)
    for i in xrange(0, 13):
        # On ignore si la case contient 0 ou 12 (positions spéciales)
        if not (cell[i] == 0 or cell[i] == 12):
            # Calcul de la distance de Manhattan entre la position actuelle et la position cible
            # abs() prend la valeur absolue de la différence de coordonnées x et y
            eva += abs(point[cell[i]][0] - point[i][0])
            eva += abs(point[cell[i]][1] - point[i][1])
    return eva  # Retourne la somme totale des distances pour servir d'heuristique

if __name__ == "__main__":
    # Boucle principale du script; tourne indéfiniment jusqu'à ce qu'on reçoive une entrée spécifique pour arrêter
    while True:
        p = [input()]  # Lecture d'une première entrée utilisateur et création d'une liste contenant cet élément
        if p == [-1]:  # Condition de sortie: arrêter si l'entrée est -1
            break  # Sort de la boucle infinie

        # Lecture de 4 lignes supplémentaires, chaque ligne contenant plusieurs entiers
        for u in xrange(4):
            for pp in map(int, raw_input().split()):  # lit une ligne, la découpe et convertit chaque entrée en entier
                p.append(pp)  # Ajoute ces valeurs à la liste p

        # Remplacement dans la liste p de la valeur 0 par 12, qui représente une position spéciale dans le puzzle
        p[p.index(0)] = 12

        # Création d'une file de priorité pour stocker les états à explorer, triés par leur coût estimé (evaluation)
        pq = PriorityQueue()

        init_hash = hash(p)  # Calcul du hash initial de la configuration p
        init_eva = evaluate(p)  # Calcul de l'évaluation heuristique initiale de la configuration p

        # Ajout de l'état initial dans la file de priorité sous la forme [coût total estimé, hash de la config, nombre d'étapes]
        pq.put([init_eva, init_hash, 0])

        visited = {}  # Dictionnaire servant à mémoriser les états déjà explorés pour éviter les répétitions
        visited[init_hash] = True  # On marque l'état initial comme visité

        # Initialisation de la réponse: si l'évaluation initiale est nulle, on est déjà à la solution, sinon on met "NA"
        ans = 0 if init_eva == 0 else "NA"

        count = 0  # Compteur d'itérations, optionnel pour suivi de progression

        # Boucle principale de l'algorithme de recherche (type A*, Dijkstra...)
        # Chaque itération traite l'état avec le plus petit coût estimé
        while not pq.empty():
            count += 1  # Incrémentation du compteur d'itérations

            cur_eva, cur_hash, cur_step = pq.get()  # Récupération de l'état avec la priorité la plus basse (meilleur estimé)

            cur_cell = dehash(cur_hash)  # Décomposition du hash pour récupérer la configuration correspondante

            # Condition d'arrêt: si l'évaluation dépasse 20 ou si on a déjà trouvé une réponse, on sort
            if not (cur_eva <= 20 and ans == "NA"):
                break  # On sort de la boucle while principale

            # Parcours des 13 positions possibles dans la configuration
            for i in xrange(13):
                # On s'intéresse uniquement aux positions contenant 0 ou 12, qui représentent des cases mobiles spéciales
                if cur_cell[i] == 0 or cur_cell[i] == 12:
                    # Pour chaque direction possible (LEFT, UP, RIGHT, DOWN)
                    for ii in [LEFT, UP, RIGHT, DOWN]:
                        if not MOVE[i][ii] == -1:  # S'il existe un mouvement possible dans cette direction
                            # Échange des valeurs entre la position actuelle et la position cible dans cette direction
                            cur_cell[i], cur_cell[MOVE[i][ii]] = cur_cell[MOVE[i][ii]], cur_cell[i]

                            hashkey = hash(cur_cell)  # Calcul du hash de la nouvelle configuration obtenue

                            # Si cette configuration n'a pas encore été visitée
                            if not hashkey in visited:
                                eva = evaluate(cur_cell)  # Calcul de l'évaluation pour la nouvelle position

                                # Si l'évaluation est nulle, cela signifie que la solution est atteinte
                                if eva == 0:
                                    ans = cur_step + 1  # On mémorise le nombre d'étapes pris pour atteindre cette solution
                                    break  # On arrête la recherche dans cette boucle

                                # Sinon on ajoute cette nouvelle configuration dans la file de priorité avec son coût estimé total
                                # Le coût total = évaluation + nombre d'étapes déjà effectuées + 1 étape pour ce mouvement
                                pq.put([eva + cur_step + 1, hashkey, cur_step + 1])

                                visited[hashkey] = True  # On marque l'état comme visité pour ne pas le revisiter

                            # On annule l'échange précédent pour restaurer l'état courant et essayer d'autres mouvements
                            cur_cell[i], cur_cell[MOVE[i][ii]] = cur_cell[MOVE[i][ii]], cur_cell[i]

        # Affichage du résultat final: nombre minimum de mouvements pour résoudre ou "NA" si aucune solution n'a été trouvée dans la limite
        print ans