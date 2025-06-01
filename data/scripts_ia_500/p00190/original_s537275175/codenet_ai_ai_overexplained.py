from math import factorial  # Importe la fonction factorial permettant de calculer la factorielle d'un entier
from Queue import PriorityQueue  # Importe la classe PriorityQueue qui est une file de priorité, utilisée ici pour gérer l'ordre de traitement des états

# Précalcul des factorielles pour éviter de les recalculer à chaque appel, ici pour les entiers de 0 jusqu'à 12 inclus.
# Cela crée une liste FACTORIAL où FACTORIAL[i] = i!
FACTORIAL=[factorial(i) for i in xrange(13)]

# Définition de constantes pour la direction des mouvements : gauche, haut, droite, bas.
LEFT,UP,RIGHT,DOWN=0,1,2,3

# Initialisation d'une liste MOVE qui représentera pour chaque position les indices des positions accessibles dans chaque direction.
# -1 signifie qu'on ne peut pas bouger dans cette direction à partir de la position donnée.
MOVE=[[0] for u in xrange(13)]  # Création d'une liste de 13 éléments contenant chacun une liste d'un élément initialisée à 0

# Remplissage manuel des positions accessibles pour chaque position de 0 à 12 selon les règles du puzzle / jeu représenté
MOVE[0] =[-1,-1,-1, 2]  # Depuis la position 0, on ne peut pas aller à gauche, en haut, à droite, mais on peut aller en bas vers la position 2
MOVE[1] =[-1,-1, 2, 5]
MOVE[2] =[ 1, 0, 3, 6]
MOVE[3] =[ 2,-1,-1, 7] 
MOVE[4] =[-1,-1, 5,-1]
MOVE[5] =[ 4, 1, 6, 9]
MOVE[6] =[ 5, 2, 7,10]
MOVE[7] =[ 6, 3, 8,11]
MOVE[8] =[ 7,-1,-1,-1]
MOVE[9] =[-1, 5,10,-1]
MOVE[10]=[ 9, 6,11,12]
MOVE[11]=[10, 7,-1,-1]
MOVE[12]=[-1,10,-1,-1]

# Le commentaire block ci-dessous explicite les endroits où un déplacement dans une certaine direction est impossible, ce qui correspond aux -1 dans MOVE

"""
MOVE[0][LEFT]=MOVE[1][LEFT]=MOVE[4][LEFT]=MOVE[9][LEFT]=MOVE[12][LEFT]=False
MOVE[0][UP]=MOVE[1][UP]=MOVE[3][UP]=MOVE[4][UP]=MOVE[8][UP]=False
MOVE[0][RIGHT]=MOVE[3][RIGHT]=MOVE[8][RIGHT]=MOVE[11][RIGHT]=MOVE[12][RIGHT]=False
MOVE[4][DOWN]=MOVE[8][DOWN]=MOVE[9][DOWN]=MOVE[11][DOWN]=MOVE[12][DOWN]=False
"""

# Fonction de hachage qui attribue un identifiant unique à une configuration donnée pour pouvoir la stocker efficacement
def hash(cell):
    # Copier la liste donnée en entrée pour ne pas modifier l'original
    work = cell[:]
    hash = 0  # Initialisation de la valeur de hachage
    # Boucle sur les 12 premiers éléments (indices 0 à 11)
    for i in xrange(12):
        # Ajoute à hash la valeur pondérée par la factorielle correspondante (permutation factorielle)
        hash += work[i] * FACTORIAL[13-1-i]
        # Actualisation des éléments subséquents pour tenir compte du décalage des éléments supérieurs (réduction de valeurs)
        for ii in xrange(i+1,13):
            if work[ii]>work[i]:
                work[ii]-=1
    return hash  # Renvoie le nombre entier représentant la configuration

# Fonction inverse de hash, qui transforme un entier (clé) en la configuration correspondante
def dehash(key):
    cell=[]  # Liste qui va contenir la configuration reconstituée
    # Extraction de la configuration en divisant par les factorielles, base factorielle
    for i in xrange(13):
        cell.append(key/FACTORIAL[13-1-i])
        key %= FACTORIAL[13-1-i]
    # Ajustement final pour récupérer la permutation originale
    for i in xrange(13-1,-1,-1):
        for ii in xrange(i+1,13):
            if cell[i]<=cell[ii]:
                cell[ii]+=1
    return cell  # Retourne la liste correspondant à la permutation initiale

# Fonction d'évaluation heuristique d'une configuration, mesure une estimation du "coût" pour atteindre la solution
def evaluate(cell):
    # Coordonnées sur un plan 2D des positions chaque index correspondant à une case
    point=[[0,2],
           [1,1],[1,2],[1,3],
           [2,0],[2,1],[2,2],[2,3],[2,4],
           [3,1],[3,2],[3,3],
           [4,2]]
    eva=0  # Initialisation de la valeur d'évaluation à 0
    # Parcourt toutes les positions
    for i in xrange(0,13):
        # Ne calcule pas la distance si la case contient la valeur 0 ou 12 (probablement vides ou spéciales)
        if not (cell[i]==0 or cell[i]==12):
            # Ajoute la distance de Manhattan entre la position actuelle et la position cible pour cell[i]
            eva+=abs(point[cell[i]][0]-point[i][0])  # différence en x
            eva+=abs(point[cell[i]][1]-point[i][1])  # différence en y
    return eva  # Renvoie l'estimation de distance à la solution

# Préparation d'une liste des hachages des configurations gagnantes (cibles)
ANS_HASH=[hash([0,1,2,3,4,5,6,7,8,9,10,11,12]),hash([12,1,2,3,4,5,6,7,8,9,10,11,0])]          

# Boucle infinie pour traiter les entrées jusqu'à ce que la condition de sortie soit rencontrée
while True:
    p=[input()]  # Lecture d'un entier unique à partir de l'entrée standard, placé dans une liste p
    if p==[-1]:  # Si la valeur lue est -1, stoppe la boucle et donc l'exécution
        break
    # Lecture des 4 lignes suivantes, chacune avec plusieurs chiffres, ajoutés à la liste p
    for u in xrange(4):
        for pp in map(int,raw_input().split()):
            p.append(pp)
    # Remplace la valeur 0 par 12 dans la liste p, probablement pour gérer un emplacement vide spécifique
    p[p.index(0)]=12
    # Création d'une file de priorité pour stocker nos noeuds à explorer dans l'ordre de priorité (évaluation + pas)
    pq = PriorityQueue()
    # On ajoute la configuration initiale avec son évaluation, son hash et un pas à 0
    pq.put([evaluate(p),hash(p),0])
    visited={}  # Dictionnaire pour stocker les configurations déjà visitées et éviter les répétitions
    visited[hash(p)]=True  # Marque la configuration initiale comme visitée
    # Si la configuration initiale est déjà une configuration gagnante, on met ans à 0 sinon à "NA" signifiant non atteint
    ans=0 if hash(p) in ANS_HASH else "NA"

    # Boucle principale d'exploration utilisant la file de priorité pour rechercher la solution
    # cur contient [score d'évaluation, clé de hachage, nombre d'étapes]
    while not pq.empty():
        unused,cur_hash,cur_step=pq.get()  # Extraction de l'élément avec la priorité la plus faible (meilleur score)
        cur_cell=dehash(cur_hash)  # Reconstruire la configuration à partir du hash

        # Si on a dépassé 20 étapes ou si une réponse a été trouvée, on arrête la recherche
        if not (cur_step<20 and ans=="NA"):
            break

        # Boucle sur toutes les positions
        for i in xrange(13):
            # On ne bouge que les cases contenant 0 ou 12 (cases vides probablement)
            if cur_cell[i]==0 or cur_cell[i]==12:
                for ii in [LEFT,UP,RIGHT,DOWN]:  # On regarde toutes les directions possibles
                    if not MOVE[i][ii]==-1:  # Si un déplacement est possible dans cette direction
                        # On échange la case vide avec la case dans la direction ii
                        cur_cell[i],cur_cell[MOVE[i][ii]]=cur_cell[MOVE[i][ii]],cur_cell[i]

                        hashkey=hash(cur_cell)  # Obtention du hash de la nouvelle configuration
                        if not hashkey in visited:  # Si la configuration n'a pas déjà été visitée
                            if hashkey in ANS_HASH:  # Si cette configuration est gagnante
                                ans=cur_step+1  # On met à jour la réponse avec le nombre d'étapes pris
                                break
                            # Sinon on ajoute cette configuration à la file de priorité pour exploration ultérieure
                            pq.put([evaluate(cur_cell)+cur_step+1,hashkey,cur_step+1])
                            visited[hashkey]=True  # Marque comme visitée

                        # On remet la configuration dans son état d'origine (annule l'échange)
                        cur_cell[i],cur_cell[MOVE[i][ii]]=cur_cell[MOVE[i][ii]],cur_cell[i]

    # Affiche la solution trouvée (nombre de déplacement minimum) ou "NA" si aucune solution trouvée dans la limite donnée
    print ans