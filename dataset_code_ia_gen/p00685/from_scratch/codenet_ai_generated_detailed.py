# Solution complète en Python pour le problème décrit.

from sys import stdin
from itertools import combinations, permutations
from collections import deque

def neighbors(pos, rel):
    # Calcule la position cible en ajoutant le vecteur rel à pos
    x, y = pos
    dx, dy = rel
    return (x + dx, y + dy)

def in_board(pos):
    # Vérifie que la position est dans les limites du plateau 4x4
    x, y = pos
    return 0 <= x < 4 and 0 <= y < 4

def position_to_index(pos):
    # Convertit une position (x, y) en un index 0..15 (ligne-major)
    x, y = pos
    return y * 4 + x

def index_to_position(idx):
    # Convertit un index 0..15 en une position (x, y) (ligne-major)
    y = idx // 4
    x = idx % 4
    return (x, y)

def generate_all_pairs():
    # Génère toutes les paires de positions distinctes possibles sur le board 4x4
    all_pos = [(x,y) for y in range(4) for x in range(4)]
    return list(combinations(all_pos, 2))

def canonical_pattern(pairs):
    # Le pattern canonique est la représentation du motif
    # les positions sont fixes, mais on peut permuter les paires
    # On trie les paires pour obtenir une forme canonique
    # Chaque paire est exprimée en index présents en ordre croissant
    pairs_sorted = [tuple(sorted(p)) for p in pairs]
    pairs_sorted.sort()
    return tuple(pairs_sorted)

def remove_pair(pairs, pair_to_remove):
    # Supprime une paire précisée de la liste de paires
    return [p for p in pairs if p != pair_to_remove]

def generate_parings(pos_set, relative_positions):
    # Essaie de produire un appariement valide de toutes les positions du set pos_set
    # avec la contrainte que chaque paire est disjoint et correspond à un des relatifs donnés
    
    # pos_set: set de positions (x,y)
    # relative_positions: liste de 4 tuples (dx, dy)
    
    pos_list = list(pos_set)
    n = len(pos_list)
    # On va rechercher un appariement parfait de paires (matchings)
    
    # Construire un graphe où les sommets sont les positions,
    # une arête représente que deux positions peuvent être formées en paire 
    # selon l'une des positions relatives autorisées
    adj = {p: [] for p in pos_list}
    pos_set = set(pos_list)
    
    for p in pos_list:
        for rel in relative_positions:
            q = neighbors(p, rel)
            # Check q dans pos_set et p<q pour éviter doublons, et que q est valide
            if q in pos_set:
                # Ajouter les deux positions dans une arête ordonnée
                # ordonner par indice pour uniformité
                p_idx = position_to_index(p)
                q_idx = position_to_index(q)
                if p_idx < q_idx:
                    adj[p].append(q)
                else:
                    adj[q].append(p)
    
    # Trouver toutes les appariements parfaits dans ce petit graphe
    # méthode classique backtracking car juste 16 sommets
    used = set()
    pairs = []
    results = []
    
    def backtrack():
        if len(used) == n:
            # On a un appariement parfait, on stocke le pattern canonique
            patterns_pairs = [(position_to_index(p), position_to_index(q)) for (p,q) in pairs]
            patterns_pairs = [tuple(sorted(pair)) for pair in patterns_pairs]
            patterns_pairs.sort()
            results.append(tuple(patterns_pairs))
            return
        # trouver le premier sommet libre
        for p in pos_list:
            if p not in used:
                break
        else:
            return
        for q in adj[p]:
            if q not in used:
                # former une paire p,q
                used.add(p)
                used.add(q)
                pairs.append((p, q))
                backtrack()
                pairs.pop()
                used.remove(p)
                used.remove(q)
    backtrack()
    # éliminer doublons
    results_unique = set(results)
    return results_unique

def main():
    while True:
        line = stdin.readline()
        if not line:
            break
        parts = line.strip().split()
        if len(parts) == 1:
            # fin d'entrée si ce nombre > 4
            x = int(parts[0])
            if x > 4:
                break
            else:
                # invalide (pas dans l'énoncé)
                continue
        # lire 8 entiers = 4 positions relatives
        if len(parts) != 8:
            # invalide ou fin
            break
        relative_positions = []
        for i in range(0, 8, 2):
            dx = int(parts[i])
            dy = int(parts[i+1])
            relative_positions.append((dx, dy))
        
        # On doit compter le nombre de arrangements correspondants par pairs distincts
        # et en comptant les permutations de paires comme un seul motif.
        # On parcourt les appariements parfaits du board 4x4 (16 positions) en paires
        # dans lesquels chaque paire est conforme à un des relative_positions.
        
        # Générer toutes configurations adéquates (patterns)
        # C'est exactement les appariements parfaits du graphe construit avec ces edges.
        
        all_pos = [(x,y) for y in range(4) for x in range(4)]
        pos_set = set(all_pos)
        
        valid_patterns = generate_parings(pos_set, relative_positions)

        # Chaque pattern dans valid_patterns est une combinaison d'appariement 
        # représentée par 8 paires (indices).
        
        # Il faut gérer la double comptabilisation des motifs équivalents par échange des symboles
        # "patterns équivalents" si on permute les paires, mais notre pattern est déjà trié
        # donc on a déjà canonisé.
        
        # Maintenant, il faut éliminer ceux qui sont équivalents par échanges de paires.
        # On normalise nos patterns en triant les paires donc ça élimine l'ordre des paires,
        # mais ça ne gère pas encore l'équivalence par échange de symboles (pairs labels).
        
        # Deux patterns sont équivalents si on peut permuter les paires.
        # mais dans notre canonisation, on a déjà trié les paires (ils sont en ordre),
        # du coup, chaque pattern représente une classe d'isomorphie unique.
        # Pour plus de sûreté, on doit considérer les permutations des paires :
        # Mais si on trie les paires, la forme canonique unique est la représentation.
        # Donc valid_patterns est déjà l'ensemble des patterns uniques.
        
        # On affiche donc simplement le nombre de ces patterns.
        # NB: Le problème de compter les arrangements en distinguant les labels des paires
        # est "résolu" en prenant l'ensemble des appariements parfaits sans distinction de paires.
        # Parce que le problème dit qu'on compte comme identiques ceux qui diffèrent par permutation des appariements,
        # ce que trie + tuple canonical_pattern fait déjà.
        
        print(len(valid_patterns))

if __name__ == "__main__":
    main()