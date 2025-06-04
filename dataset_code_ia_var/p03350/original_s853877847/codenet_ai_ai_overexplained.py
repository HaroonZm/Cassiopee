import sys  # Importe le module sys, qui fournit l’accès à certaines variables et fonctions du système
import numpy as np  # Importe la bibliothèque numpy, utilisée pour le calcul scientifique rapide sur des tableaux

def offset(length):
    # Calcule la puissance de deux du paramètre length pour obtenir l'offset adéquat dans l'arbre binaire complet
    # Cela fait un décalage binaire vers la gauche, équivalent à 2 ** length
    return 1 << length

def solve():
    # Lit deux entiers n et k depuis l'entrée standard, séparés par des espaces
    # sys.stdin.buffer.readline() lit la ligne, split() sépare les éléments, map(int, ...) convertit chaque élément en un entier
    n, k = map(int, sys.stdin.buffer.readline().split())
    
    # Lit la suite binaire (ou autre) sous forme de bytes à partir de l'entrée standard (tout ce qui reste, sauf la première ligne)
    # b"0" concatène un zéro initial pour aligner les indices dans la suite à venir
    # .replace(b"\n", b"") supprime tous les retours à la ligne pour obtenir une séquence continue de chiffres
    buf = b"0" + sys.stdin.buffer.read().replace(b"\n", b"")
    
    # Convertit buf en un tableau numpy de bytes (int8), puis en int32 pour des opérations futures
    # np.frombuffer lit buf sans faire de copie mémoire : chaque byte devient une valeur
    # - ord(b"0") permet de transformer les bytes ASCII de chiffres ('0' devient 0, '1' devient 1, etc.)
    table = (np.frombuffer(buf, dtype=np.int8).astype(np.int32) - ord(b"0"))
    
    # Crée un tableau d'entiers de longueur égale à la moitié de table
    # np.ones initialise le tableau avec des uns, dtype=int32 précise le type d’éléments stockés
    offset_table = np.ones(len(table) // 2, dtype=np.int32)
    # Boucle pour remplir offset_table avec des puissances de deux selon les positions de bits
    # La boucle parcourt tous les v de 0 à n - 2 (inclus)
    for v in range(n - 1):
        # Pour chaque v, le segment d'indice [1 << v : 2 << v] est rempli avec la valeur 2 << v (càd 2^(v+1))
        offset_table[1 << v:2 << v] = 2 << v
    
    ret = None  # Initialise la variable de retour (None si aucune réponse trouvée)
    # Première boucle sur toutes les positions de 0 à n inclus
    for pos in range(n + 1):
        # Deuxième boucle sur tous les 'length' supérieurs stricts à 'pos' jusqu’à n inclus
        for length in range(pos + 1, n + 1):
            # Crée une sous-table correspondant aux éléments [offset(length):offset(length+1)]
            # offset(length) donne l’index de début, offset(length + 1) celui de fin pour cette longueur
            subtable = table[offset(length):offset(length + 1)]
            # Reshape subtable pour la transformer en un tableau 2D : chaque ligne a 2^pos colonnes, ordre de remplissage en colonne
            # Puis on fait sum(axis=0) pour sommer chaque colonne (donc chaque motif sur cette longueur)
            # On ajoute cette somme à la portion de table correspondant à l’offset de pos : on propage les comptages
            table[offset(pos):offset(pos + 1)] += subtable.reshape(-1, 1 << pos, order="F").sum(axis=0)
        # Récupère la portion de la table après propagation pour la longueur actuelle : taille 2^pos décalée à l’offset correct
        count_table = table[offset(pos):offset(pos + 1)]
        # np.argmax retourne l’indice du premier élément qui vérifie la condition (ici >= k)
        index = np.argmax(count_table >= k)
        # Si au moins un motif satisfait la condition d’occurrence, on stocke la paie (index, pos)
        if count_table[index] >= k:
            ret = (index, pos)
        else:
            # Sinon, aucune solution plus longue possible donc on retourne la dernière valide
            return ret
        
        # Boucle supplémentaire par longueur croissante pour préparer la prochaine itération et faire des ajustements (transpositions)
        for length in range(pos + 1, n + 1):
            # Calcule la taille totale du motif pour cette longueur : 2^length
            size = 1 << length
            # La différence de longueur
            rest = length - pos
            # Calcule la demi-période (moitié de la période d’un cycle binaire à cette position)
            half_period = 1 << (rest - 1)
            # Crée un tableau d’indices à transformer sur cette portion
            # np.arange crée une séquence d'entiers de (half_period+size) à (half_period+2*size) exclus, sur int32
            # Puis le décalage binaire (>>) ramène chaque indice à une valeur indexée par rest
            trans_table = np.arange(half_period + size, half_period + size * 2, dtype=np.int32) >> rest
            
            # Reshape trans_table en lignes chacun de half_period*2 colonnes : réorganisation mémoire
            trans_reshaped = trans_table.reshape(-1, half_period * 2)
            # Multiplie chaque valeur trans_reshaped par une version étendue de offset_table : d’abord les half_period premiers, puis les half_period premiers à l’envers
            # np.hstack concatène les deux portions, servant de facteur de multiplication
            trans_reshaped *= np.hstack((offset_table[:half_period], offset_table[half_period - 1::-1]))
            # Ajoute à chaque élément trans_reshaped une version roulée (np.roll) d’un tableau allant de -half_period à half_period exclus, roulée de half_period vers la droite
            trans_reshaped += np.roll(np.arange(-half_period, half_period), half_period)
            
            # Somme les occurrences pour la portion concernée et ajoute à la table : cela prépare la structure pour l’itération suivante
            table[trans_table] += table[offset(length):offset(length + 1)]
    # La fonction retourne la dernière réponse valide trouvée (index, longueur)
    return ret

# Appel de la fonction solve : retourne un tuple (index, longueur)
index, length = solve()
# Affiche, sous forme binaire, le motif trouvé de la bonne longueur :
# - format(index, "020b") convertit index en binaire sur 20 chiffres (avec des zéros à gauche)
# - On extrait les chiffres correspondants à la longueur trouvée, en partant de la droite (indice 20-length à la fin)
print(format(index, "020b")[20 - length:])