import sys
import math

# On modélise chaque disque par une classe Disc pour plus de clarté
class Disc:
    def __init__(self, x, y, r, c):
        self.x = x      # coordonnée x du centre
        self.y = y      # coordonnée y du centre
        self.r = r      # rayon
        self.c = c      # couleur (indice)
        
# Fonction pour déterminer si un disque i est sur un disque j
# c’est-à-dire s’il recouvre partiellement j et que i<j (i est apparu avant j)
def is_on_top(i, j, discs):
    di = discs[i]
    dj = discs[j]
    # distance entre les centres
    dist = math.sqrt((di.x - dj.x)**2 + (di.y - dj.y)**2)
    # i est sur j ssi la distance est STRICTEMENT inférieure à r_i + r_j (pas tangent)
    # cela signifie que i chevauche j ; et puisque i<j, i est "au-dessus"
    return dist < di.r + dj.r

# Fonction pour calculer l'état "libre" des disques. Un disque est libre s'il n'y a aucun disque 
# sur lui (c'est-à-dire au-dessus). On modélise cela par un graphe d'arêtes i->j signifiant i est sur j.
# Ensuite, on peut calculer le nombre de disques sur chacun, et détecter ceux sans disque au-dessus.
def compute_free(discs, removed):
    n = len(discs)
    # Pour chaque disque, liste des disques directement dessus (i -> j signifie i est dessus)
    on_top = [[] for _ in range(n)]
    # on compte combien de disques sont dessus de j (dans le sous-ensemble non enlevé)
    above_count = [0]*n
    
    for i in range(n):
        if removed[i]:
            continue
        for j in range(i+1, n):
            if removed[j]:
                continue
            if is_on_top(i, j, discs):
                on_top[i].append(j)
                above_count[j] += 1
    # les disques sans disque au-dessus sont libres
    free = [above_count[i] == 0 and (not removed[i]) for i in range(n)]
    return free

# Fonction récursive pour obtenir le maximum de disques pouvant être retirés
# Arg : removed est une liste booléenne indiquant les disques déjà retirés
# On cherche toutes les paires de disques libres de même couleur, on les enlève, on recurse, et maximise la quantité retirée.
def max_removed(discs, removed):
    n = len(discs)
    free = compute_free(discs, removed)
    
    # Trouver toutes les paires libres de même couleur
    color_to_free_indices = {}
    for i in range(n):
        if free[i]:
            c = discs[i].c
            color_to_free_indices.setdefault(c, []).append(i)
    
    # Pas de paires libres possibles -> fin de la récursion
    any_pair = False
    best = 0
    # Pour chaque couleur, essayer toutes les paires possibles parmi les libres
    for c, indices in color_to_free_indices.items():
        length = len(indices)
        if length < 2:
            continue
        # Parcourir toutes les paires
        for i1 in range(length):
            for i2 in range(i1+1, length):
                # essayer d'enlever ces deux disques
                removed[indices[i1]] = True
                removed[indices[i2]] = True
                # on enlève 2 disques maintenant, plus ceux des appels récursifs
                score = 2 + max_removed(discs, removed)
                # remettre comme avant (backtrack)
                removed[indices[i1]] = False
                removed[indices[i2]] = False
                if score > best:
                    best = score
                any_pair = True

    # Si aucune pair n'a été enlevée, c'est 0 (aucun disque retiré dans ce cas)
    return best

def main():
    input_lines = sys.stdin.read().strip().split('\n')
    idx = 0
    while True:
        if idx >= len(input_lines):
            break
        n = int(input_lines[idx].strip())
        idx += 1
        if n == 0:
            # fin de la saisie
            break
        discs = []
        for _ in range(n):
            x, y, r, c = map(int, input_lines[idx].strip().split())
            idx += 1
            discs.append(Disc(x, y, r, c))
        
        # liste booléenne qui indique si le disque a été retiré
        removed = [False]*n
        # calculer puis afficher le résultat
        result = max_removed(discs, removed)
        print(result)

if __name__ == "__main__":
    main()