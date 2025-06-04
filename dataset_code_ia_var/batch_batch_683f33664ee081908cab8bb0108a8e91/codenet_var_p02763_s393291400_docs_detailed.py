def initialize(N):
    """
    Initialise le segment tree utilisé pour effectuer les opérations efficacement sur la chaîne de caractères.
    
    Args:
        N (int): La longueur de la chaîne initiale.
        
    Returns:
        tuple: 
            - Un tableau SEG initialisé de taille (2 * puissance de 2 supérieure ou égale à N) - 1, rempli de zéros.
            - La taille d (puissance de 2) qui couvre N.
    """
    i = 1
    # Trouve la puissance de 2 supérieure ou égale à N
    while i < N:
        i *= 2
    # SEG a une taille de 2*i-1 pour représenter complètement le segment tree
    return [0] * (2 * i - 1), i

def update(i, x):
    """
    Met à jour la lettre à la position i de la chaîne dans l'arbre segmentaire.
    
    Args:
        i (int): L'indice (0-based) du caractère à modifier.
        x (str): Le nouveau caractère à placer à la position i.
        
    Effet de bord:
        Modifie SEG pour refléter le changement de caractère.
    """
    # Met à jour la feuille correspondante dans l'arbre segmentaire
    global SEG, d
    i += d - 1  # Passage à l'indice de la feuille dans SEG
    bit = ord(x) - 97  # Obtient la position de la lettre (0 pour 'a', 1 pour 'b', etc.)
    SEG[i] = 1 << bit  # Mets à jour avec le bit correspondant à la lettre
    # Met à jour les noeuds ancêtres
    while i > 0:
        i = (i - 1) // 2
        SEG[i] = SEG[2 * i + 1] | SEG[2 * i + 2]  # Union des deux enfants

def find(a, b, k, l, r):
    """
    Effectue une requête pour obtenir l'union des bits dans l'intervalle [a, b) dans la chaîne,
    ce qui permet de connaitre les lettres distinctes dans cette plage.
    
    Args:
        a (int): Début de l'intervalle (inclus).
        b (int): Fin de l'intervalle (exclu).
        k (int): Numéro du noeud courant dans l'arbre segmentaire.
        l (int): Début du segment couvert par ce noeud.
        r (int): Fin du segment couvert par ce noeud.
        
    Returns:
        int: Un entier dont les bits à 1 représentent les lettres présentes dans l'intervalle [a, b).
    """
    # Aucun recouvrement
    if r <= a or b <= l:
        return 0
    # Entièrement couvert
    if a <= l and r <= b:
        return SEG[k]
    else:
        # Recouvre partiellement, doit interroger les enfants
        c1 = find(a, b, 2 * k + 1, l, (l + r) // 2)
        c2 = find(a, b, 2 * k + 2, (l + r) // 2, r)
        return c1 | c2

# Lecture des entrées
N = int(input())           # Longueur de la chaîne
S = input()                # La chaîne de caractères
Q = int(input())           # Nombre de requêtes

# Initialisation du segment tree
SEG, d = initialize(N)
for i in range(N):
    update(i, S[i])        # Initialise le segment tree avec les caractères de la chaîne

# Traitement des requêtes
for _ in range(Q):
    com, s, t = map(str, input().split())
    if com == '1':
        # Modification d'un caractère
        update(int(s) - 1, t)
    else:
        # Demande du nombre de lettres distinctes dans l'intervalle [int(s)-1, int(t))
        cnt = 0
        bit = find(int(s) - 1, int(t), 0, 0, d)
        # Compte le nombre de bits à 1 dans le résultat (nombre de lettres distinctes)
        while bit > 0:
            if bit & 1:
                cnt += 1
            bit //= 2
        print(cnt)