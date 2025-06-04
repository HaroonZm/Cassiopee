import heapq
from collections import Counter

class HuffmanTreeNode:
    """
    Représente un nœud d'un arbre de Huffman.

    Attributs
    ----------
    char : str
        Le caractère stocké dans le nœud (vide pour les nœuds internes).
    freq : int
        La fréquence d'apparition du caractère ou la somme des fréquences pour les nœuds internes.
    left : HuffmanTreeNode ou None
        Fils gauche du nœud (correspondant au '0' lors de la génération du code).
    right : HuffmanTreeNode ou None
        Fils droit du nœud (correspondant au '1' lors de la génération du code).
    """
    def __init__(self, char, freq):
        """
        Initialise un nœud de l'arbre de Huffman.

        Paramètres
        ----------
        char : str
            Le caractère à stocker dans le nœud.
        freq : int
            La fréquence du caractère.
        """
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None

    def __lt__(self, other):
        """
        Définit le comportement du comparateur < pour les nœuds, basé sur la fréquence.
        Utile pour le bon fonctionnement du tas lors de la construction de l'arbre.

        Paramètres
        ----------
        other : HuffmanTreeNode
            L'autre nœud à comparer.

        Retourne
        -------
        bool
            True si la fréquence de ce nœud est inférieure à celle de l'autre, False sinon.
        """
        return self.freq < other.freq

def huffman_code_helper(root, code='', codes=None):
    """
    Fonction récursive pour traverser l'arbre de Huffman et générer les codes binaires pour chaque caractère.

    Paramètres
    ----------
    root : HuffmanTreeNode
        Racine (ou sous-racine) de l'arbre de Huffman.
    code : str, optionnel
        Le code binaire courant généré lors de la traversée (par défaut '').
    codes : dict ou None, optionnel
        Dictionnaire associant chaque caractère à son code binaire.

    Retourne
    -------
    dict
        Dictionnaire contenant les caractères comme clés et leurs codes Huffman binaires comme valeurs.
    """
    if codes is None:
        codes = {}

    if root is None:
        return codes

    # Si le nœud est une feuille, on assigne le code généré pour ce caractère
    if root.left is None and root.right is None:
        codes[root.char] = code if code else '0'  # Cas particulier si l'arbre n'a qu'un seul caractère
        return codes

    # Parcours à gauche : ajoute '0' au code
    huffman_code_helper(root.left, code + '0', codes)
    # Parcours à droite : ajoute '1' au code
    huffman_code_helper(root.right, code + '1', codes)
    return codes

def huffman_code(text):
    """
    Génère les codes de Huffman pour une chaîne de caractères.

    Paramètres
    ----------
    text : str
        Le texte d'entrée pour lequel générer les codes.

    Retourne
    -------
    dict
        Dictionnaire associant chaque caractère du texte à son code binaire de Huffman.
    """
    # Compte la fréquence d'apparition de chaque caractère dans le texte
    counter = Counter(text)
    heap = []

    # Crée un nœud de feuille pour chaque caractère et l'ajoute dans une structure de tas (heap)
    for char, freq in counter.items():
        heap.append(HuffmanTreeNode(char, freq))
    heapq.heapify(heap)

    # Construit l'arbre de Huffman en fusionnant les deux nœuds les moins fréquents à chaque étape
    while len(heap) > 1:
        left = heapq.heappop(heap)
        right = heapq.heappop(heap)
        merged = HuffmanTreeNode('', left.freq + right.freq)
        merged.left = left
        merged.right = right
        heapq.heappush(heap, merged)

    # La racine de l'arbre est le seul nœud restant dans le tas
    root = heap[0]
    # Génère les codes via une traversée de l'arbre
    return huffman_code_helper(root)

def solution():
    """
    Fonction principale qui lit un texte depuis l'entrée standard, génère les codes de Huffman, encode le texte 
    puis affiche la longueur totale de la chaîne binaire encodée.
    """
    # Lecture du texte de l'utilisateur
    text = input()
    # Génère les codes Huffman pour chaque caractère du texte
    codes = huffman_code(text)
    # Encode chaque caractère du texte avec son code Huffman
    encoded = []
    for char in text:
        encoded.append(codes[char])
    # Affiche la longueur totale du texte encodé en binaire
    print(len(''.join(encoded)))

solution()