import sys

readline = sys.stdin.readline
write = sys.stdout.write

def solve():
    """
    Résout un cas de l'entrée.
    Lit la hauteur H et le nombre N de pièces, puis lit l'état de la grille H et les N pièces.
    Effectue ensuite une recherche en profondeur (DFS) pour trouver le nombre maximal de lignes complétées.
    Retourne False si H et N sont tous deux nuls (signal de fin de l'entrée), True sinon.
    """
    H, N = map(int, readline().split())  # Lecture de la hauteur du tableau et du nombre de pièces
    if H == N == 0:
        return False  # Terminer si c'est la fin des données

    def get_block():
        """
        Extrait la représentation numérique (4 bits) d'un bloc 2x2 dans la grille.
        Les lignes du bloc sont lues depuis l'entrée standard. Un '#' représente un bloc occupé.
        Renvoie un entier dont les bits décrivent l'occupation du bloc.
        """
        s = readline().strip()  # Première ligne du bloc
        v = (s[0] == '#') + (s[1] == '#')*2
        s = readline().strip()  # Deuxième ligne du bloc
        v += (s[0] == '#')*4 + (s[1] == '#')*8
        return v  # v est un entier dont les bits 0-3 correspondent à la disposition, de gauche à droite et de haut en bas

    # Lecture de la grille de jeu : H lignes, chaque ligne encodée sur 4 bits (colonnes)
    R = []
    for i in range(H):
        R.append(get_block())

    # Ajout de 8 lignes vides pour éviter les dépassements lors de la manipulation des pièces
    R.extend([0]*8)
    H += 8  # Mise à jour de la hauteur totale

    # Lecture des pièces : chaque pièce est définie par deux blocs 2x2 superposés (un "bloc 2x4")
    I = []
    for i in range(N):
        v = get_block()  # partie supérieure de la pièce
        w = get_block()  # partie inférieure de la pièce

        # Si la partie supérieure est vide on inverse (pour normaliser la pièce)
        if v == 0:
            v, w = w, 0

        # Tentative de décalage à droite pour normaliser la pièce si les deux colonnes de gauche sont vides
        if v & 3 == 0 and w & 3 == 0:
            v >>= 2
            w >>= 2
        # Tentative de décalage à droite de 1 colonne si possible
        if v & 5 == 0 and w & 5 == 0:
            v >>= 1
            w >>= 1

        # Ajout de la pièce à la liste sous forme de tuples (partie supérieure, partie inférieure)
        I.append((v, w))

    def dfs(i, R0):
        """
        Propose récursivement toutes les façons possibles de placer les pièces.
        Paramètres:
        i (int): Indice de la pièce en cours de traitement dans la liste I.
        R0 (List[int]): Etat courant de la grille, sous forme de liste d'entiers (4 bits par ligne).
        Retourne le nombre maximal de lignes complétées réalisable à partir de cet état.
        """
        if i == N:
            return 0  # Cas terminal : plus de pièce à placer

        v0, w0 = I[i]  # Récupération de la pièce courante (parties haute et basse)
        r = 0  # Initialise le score maximal pour ce sous-problème à 0

        # Pour chaque position/rotation/décalage possible de la pièce (0 à 3 positions), tentative de placement
        for k, f in ((0, 0), (1, 5), (2, 3), (3, 0)):
            v = v0 << k  # Déplacement horizontal de la partie supérieure
            w = w0 << k  # Déplacement horizontal de la partie inférieure

            # Vérification de dépassement de la grille ou de collision avec la bordure
            if v >= 16 or w >= 16 or v & f or w & f:
                continue

            # Recherche de la hauteur où placer la pièce sans collision avec les blocs existants
            h = H-1
            while h and R0[h-1] & v == 0 and R0[h] & w == 0:
                h -= 1

            # Placement de la pièce sur une copie de la grille
            R = R0[:]
            R[h] |= v     # Ajout de la partie supérieure sur la ligne h
            R[h+1] |= w   # Ajout de la partie inférieure sur la ligne h+1

            c = 0  # Nombre de lignes complétées suite au placement

            # Vérification et suppression de lignes complètes, ligne du dessous en premier
            if R[h+1] == 15:
                for j in range(h+2, H):
                    R[j-1] = R[j]  # Décalage des lignes suivantes vers le haut
                c += 1
            if R[h] == 15:
                for j in range(h+1, H):
                    R[j-1] = R[j]  # Décalage des lignes suivantes vers le haut
                c += 1

            # Appel récursif pour placer la pièce suivante, on garde le max des scores possibles
            r = max(r, dfs(i+1, R) + c)
        return r

    # Démarre la recherche sur la première pièce avec la grille initiale
    write("%d\n" % dfs(0, R))
    return True

# Boucle principale, s'arrête lorsque solve() retourne False
while solve():
    ...