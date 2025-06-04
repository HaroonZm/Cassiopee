import sys
sys.setrecursionlimit(10**7)

# Fonction pour parser l'arbre depuis la chaîne d'entrée.
# La structure est soit un noeud interne ( ( gauche droite ) )
# soit une feuille (un entier).
# On renvoie (arbre, position_fin_parse)
def parse_tree(s, pos=0):
    # Ignore les espaces
    while pos < len(s) and s[pos] == ' ':
        pos += 1
    # Si c'est une feuille (un chiffre), on le lit
    if s[pos].isdigit():
        num = 0
        while pos < len(s) and s[pos].isdigit():
            num = num * 10 + int(s[pos])
            pos += 1
        return ('leaf', num), pos
    # Sinon c'est un noeud interne qui commence par '('
    if s[pos] == '(':
        pos += 1
        left, pos = parse_tree(s, pos)
        # ignore un espace après la sous-arbre gauche
        while pos < len(s) and s[pos] == ' ':
            pos += 1
        right, pos = parse_tree(s, pos)
        while pos < len(s) and s[pos] == ' ':
            pos += 1
        # doit se terminer par ')'
        if pos < len(s) and s[pos] == ')':
            pos += 1
        else:
            # la donnée d'entrée doit respecter le format, on ne gère pas l'erreur
            pass
        return ('node', left, right), pos
    # Cas non prévu (par exemple END)
    return None, pos

# Fonction pour calculer le nombre de façons d'écrire les caractères 'A', 'O', 'X' dans les noeuds internes
# pour obtenir l'ensemble complet {a,b,c,d} = {0,1,2,3}
# L'approche:
# - Chaque feuille a un ensemble déjà défini.
# - Un noeud interne a 3 choix possibles: A (intersection), O (union), X (symétrique différence) sur les ensembles des enfants.
# - Pour chaque noeud interne, on fait un dfs en mémorisant (memo) les nombre de façons d'obtenir chaque sous-ensemble.
# - Le résultat final est le nombre de façons d'obtenir {0,1,2,3} (= 15 en bitmask 0b1111) au noeud racine.

# Les ensembles d'éléments a,b,c,d seront représentés sous forme d'entiers 4 bits:
# bit 0 = a, bit 1 = b, bit 2 = c, bit 3 = d

class TreeNode:
    def __init__(self, node_type):
        self.type = node_type  # 'leaf' ou 'node'
        if node_type == 'leaf':
            self.idx = None  # index du subset
        else:
            self.left = None
            self.right = None

def build_tree(parsed_tree):
    # conversion du tuple en objet TreeNode pour plus de commodité
    if parsed_tree[0] == 'leaf':
        leaf = TreeNode('leaf')
        leaf.idx = parsed_tree[1]
        return leaf
    else:
        node = TreeNode('node')
        node.left = build_tree(parsed_tree[1])
        node.right = build_tree(parsed_tree[2])
        return node

def set_operations(op, s1, s2):
    # s1, s2 sont des sets représentés par int (4 bits)
    # Retourne le résultat selon l'opération : A=intersection, O=union, X=symm diff
    if op == 'A':
        return s1 & s2
    elif op == 'O':
        return s1 | s2
    elif op == 'X':
        return s1 ^ s2
    else:
        return 0  # pas attendu

def count_ways(node, subsets, memo):
    # node: TreeNode, subsets: list de sets bits, memo: dict (node_id, set) -> nombre de façons
    # On attribue un id unique à chaque noeud afin d'utiliser memo
    # Pour ce faire, on peut définir une fonction qui génère une id unique par noeud basée sur l'objet id()
    node_id = id(node)
    # Si c'est une feuille, le seul ensemble possible est celui donné par subset[node.idx-1]
    # Car idx est 1-based dans l'énoncé
    if node.type == 'leaf':
        s = subsets[node.idx - 1]
        # On renvoie un dict {ensemble: nombre_de_façons}
        # Ici, 1 façon pour le sous-ensemble défini, 0 pour les autres
        return {s: 1}
    else:
        # Calcul des distributions pour les sous-arbres gauche et droit
        left_dist = count_ways(node.left, subsets, memo)
        right_dist = count_ways(node.right, subsets, memo)

        # Pour le noeud actuel, on veut la distribution (ensemble -> nombre de façons)
        dist = {}
        # Pour chaque couple d'ensembles possibles encodés dans left_dist et right_dist
        # on calcule le résultat possible avec 'A','O','X'
        # puis on cumule le nombre de façons
        for sl, ways_l in left_dist.items():
            for sr, ways_r in right_dist.items():
                for op in ['A','O','X']:
                    res = set_operations(op, sl, sr)
                    dist[res] = dist.get(res, 0) + ways_l * ways_r
        return dist

def main():
    input_lines = sys.stdin.read().splitlines()
    idx = 0
    while True:
        if idx >= len(input_lines):
            break
        line = input_lines[idx].strip()
        if line == 'END':
            break
        # Parse tree
        parsed_tree, pos = parse_tree(line)
        idx += 1
        # Nombre N
        N = int(input_lines[idx].strip())
        idx += 1
        subsets = []
        for _ in range(N):
            bits = list(map(int, input_lines[idx].strip().split()))
            idx += 1
            s = 0
            for i, b in enumerate(bits):
                if b == 1:
                    s |= (1 << i)
            subsets.append(s)
        # Construire arbre d'objets
        root = build_tree(parsed_tree)
        # Calcul du nombre de façons d'obtenir l'ensemble complet {a,b,c,d}, soit 0b1111 = 15
        dist = count_ways(root, subsets, {})
        print(dist.get(15, 0))

if __name__ == '__main__':
    main()