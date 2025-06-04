import sys
import bisect

# Fonction principale de résolution
def solve():
    s = sys.stdin.readline().rstrip()
    t = sys.stdin.readline().rstrip()

    # Prétraitement : pour chaque caractère, construire la liste des positions dans s (1-indexé)
    pos = {}
    for i, ch in enumerate(s, start=1):
        if ch not in pos:
            pos[ch] = []
        pos[ch].append(i)
    
    # Si un caractère de t n'existe pas dans s, on ne peut faire aucune opération
    for ch in t:
        if ch not in pos:
            print(0)
            return

    # Fonction qui pour un substring u, trouve une occurrence de t comme sous-séquence (positions strictement croissantes)
    # en utilisant les positions pré-calculées globales dans s, mais pour l'étape, on va travailler avec u lui-même.
    # Comme on applique l'opération sur différents u, on doit préparer pour u un mapping similaire.
    # Pour cela, on va construire un index pour chaque caractère de u, et récupérer pour t les positions dans u.

    # Cependant, reconstruire des indices à chaque étape serait couteux.
    # Meilleure approche: On traite chaque u en cherchant la première occurrence possible de t en sous-séquence dans u.
    # On procède de gauche à droite dans u en cherchant progressive chaque caractère de t.

    # Cette fonction renvoie None si t n'est pas sous-séquence de u,
    # Sinon renvoie la liste des indices dans u où apparaissent les caractères de t
    def find_subsequence_indices(u, t):
        indices = []
        start = 0
        for ch in t:
            pos_ch = []
            # Pour trouver rapidement la position de ch dans u à partir de start, on recherche linéairement car |t| <= |s| <= 1e5
            # Mais il y a un risque de ralentissement. On optimise en construisant un mapping similaire à pos pour u:
            # Comme |t| est petit par rapport à s, cela reste acceptable.
            # Alternative : On stocke les positions de chaque caractère dans u pour accélérer.
            # On fait ça une seule fois par u:
            # Cette fonction sera appelée plusieurs fois, donc on cache le mapping en closure ?

            # Pour cela, déplacer cette fonction à l'intérieur de solve avec cache.

            # Mais pour simplifier et efficace, on peut scanner u pour t en une passe :
            # On avance dans u à chaque lettre de t. 
            pass

        # Implémentation plus efficace ci-dessous.

    # Version améliorée: cette fonction prend en entrée u,t
    # Cherche la première occurrence de t comme sous-séquence dans u
    # Renvoie les indices des caractères de t dans u
    def find_subsequence_indices(u, t):
        res = []
        pos_in_u = 0
        for ch in t:
            # chercher ch dans u à partir de pos_in_u
            while pos_in_u < len(u) and u[pos_in_u] != ch:
                pos_in_u += 1
            if pos_in_u == len(u):
                return None
            res.append(pos_in_u)
            pos_in_u += 1
        return res

    # Initialisation de l'ensemble A
    A = [s]
    count = 0

    while True:
        B = []
        can_operate = False

        # Pour chaque u dans A, on cherche une sous-séquence égale à t
        for u in A:
            indices = find_subsequence_indices(u, t)
            if indices is None:
                # Pas possible de faire l'opération sur ce u
                # On le garde dans B intact car il ne sera pas transformé
                B.append(u)
            else:
                # On a trouvé la sous-séquence : on découpe u en morceaux séparés par les positions indices
                # positions indices sont positions dans u (0-based)
                can_operate = True
                parts = []
                prev = 0
                for idx in indices:
                    parts.append(u[prev:idx])
                    prev = idx + 1
                parts.append(u[prev:])
                # On ajoute les parties non vides dans B
                for part in parts:
                    B.append(part)
        
        if not can_operate:
            # On ne peut plus faire d'opération
            break

        # On remplace A par B
        A = B
        count += 1

    print(count)

if __name__ == "__main__":
    solve()