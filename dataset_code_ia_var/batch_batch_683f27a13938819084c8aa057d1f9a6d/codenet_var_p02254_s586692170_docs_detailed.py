from heapq import heapify, heappop, heappush

class Node:
    """
    Classe représentant un nœud de l'arbre de Huffman.
    
    Attributs:
        key (int): La fréquence totale des caractères sous ce nœud.
        char (str): Chaîne de caractères représentée par ce nœud (utile pour les feuilles).
        pare (Node): Le parent de ce nœud dans l'arbre (None si racine).
    """
    def __init__(self, key, char=None):
        """
        Initialise le nœud avec sa fréquence et éventuellement l'ensemble de caractères.
        
        Args:
            key (int): Fréquence du nœud.
            char (str, optionnel): Caractère ou concaténation de caractères.
        """
        self.key = key
        self.char = char
        self.pare = None

# Lecture de la chaîne d'entrée
st = input()

# Liste unique des caractères présents
unique_chars = list(set(st))

# Construction de la liste des couples (fréquence, caractère)
freq_list = []
for ch in unique_chars:
    freq_list.append((st.count(ch), ch))

# Transformation de la liste fréquence-caractère en tas min (min-heap)
heapify(freq_list)

# Création d'un dictionnaire pour référencer chaque caractère et son nœud associé
node = {}
for cnt, char in freq_list:
    node[char] = Node(cnt, char)

# Construction de l'arbre de Huffman à partir du heap
while len(freq_list) > 1:
    # Extraction des deux éléments les plus petits
    cnt1, chars1 = heappop(freq_list)
    cnt2, chars2 = heappop(freq_list)
    # Création du nouveau nœud interne
    merged_node = Node(cnt1 + cnt2, chars1 + chars2)
    node[chars1 + chars2] = merged_node
    # Assignation des parents
    node[chars1].pare = merged_node
    node[chars2].pare = merged_node
    # On remet le nœud fusionné dans le tas
    heappush(freq_list, (cnt1 + cnt2, chars1 + chars2))
    # Si c'était la dernière fusion, on définit la racine
    if len(freq_list) == 1:
        root = merged_node

def dfs(cur_node, cnt=1):
    """
    Calcule la profondeur du nœud courant dans l'arbre de Huffman.

    Args:
        cur_node (Node): Le nœud à partir duquel on part.
        cnt (int, optionnel): La profondeur actuelle (par défaut 1).

    Returns:
        int: Profondeur par rapport à la racine.
    """
    if cur_node.pare is None:
        return cnt
    return dfs(cur_node.pare, cnt + 1)

# Calcul du nombre total de bits nécessaires selon Huffman
total_bits = 0
for ch in unique_chars:
    cur = node[ch]
    depth = dfs(cur)
    total_bits += depth * cur.key

print(total_bits)