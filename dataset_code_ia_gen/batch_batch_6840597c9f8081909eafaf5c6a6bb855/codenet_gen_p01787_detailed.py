import sys

# Fonction pour lire une ligne RLE, retourner une liste de tuples (char, length)
def read_rle_line():
    tokens = sys.stdin.readline().strip().split()
    rle = []
    i = 0
    while i < len(tokens):
        if tokens[i] == '$':
            break
        c = tokens[i]
        l = int(tokens[i+1])
        rle.append([c, l])
        i += 2
    return rle

# Fonction pour dérouler une RLE en une liste complète des caractères
# Attention: les longueurs peuvent être très grandes (jusqu'à 10^8).
# Il est impossible de dérouler complètement la chaîne en mémoire.
# On doit donc faire une approche sans déroulement complet.

# On doit trouver la première occurrence de B dans A, A et B sont en RLE.
# Stratégie:
# - On crée des itérateurs sur A et B qui avancent dans la chaîne caractère par caractère virtuellement.
# - On fait une recherche naïve (à cause des grandes valeurs, pas possible de KMP sur RLE directement)
# - On teste chaque position possible dans A (en virtualisant la chaîne), si ça correspond à B.
# - Une fois qu'on trouve, on remplace la portion correspondante par C, puis on reconstruit le RLE final.

# Implémentation d'un itérateur sur RLE qui permet d'accéder au caractère à la position i
# et aussi aider à reconstruire la RLE partiellement sans dérouler toute la chaîne.

class RLEString:
    def __init__(self, rle):
        # rle : list of [char, length]
        self.rle = rle
        self.total_length = sum(l for _, l in rle)
        # préfixe des longueurs cumulées pour accéder rapidement à un index
        self.prefix = []
        s = 0
        for _, l in rle:
            s += l
            self.prefix.append(s)
    
    # Retourne le caractère à la position pos (0-based)
    def char_at(self, pos):
        # recherche binaire sur prefix
        left, right = 0, len(self.prefix) - 1
        while left < right:
            mid = (left + right) // 2
            if pos < self.prefix[mid]:
                right = mid
            else:
                left = mid + 1
        # left est l'index dans rle contenant la position pos
        return self.rle[left][0]

    # Donne la segmentation RLE partielle de [start, end) positions inclusives start, exclusive end
    # sans dérouler tout en listant plus petits segments RLE.
    # On découpe la RLE pour obtenir précisément le segment [start, end)
    def slice(self, start, end):
        # start, end: indices of substring, 0-based, end exclusive
        if start == end:
            return []
        result = []
        # Trouver l'index dans rle où commence start
        left = 0
        right = len(self.prefix) - 1
        while left < right:
            mid = (left + right) // 2
            if start < self.prefix[mid]:
                right = mid
            else:
                left = mid + 1
        start_block = left

        # Trouver l'index dans rle où commence end-1
        left = 0
        right = len(self.prefix) - 1
        while left < right:
            mid = (left + right) // 2
            if end - 1 < self.prefix[mid]:
                right = mid
            else:
                left = mid + 1
        end_block = left

        # extraire les parties du premier block
        if start_block == 0:
            start_offset = start
        else:
            start_offset = start - self.prefix[start_block -1]
        # extraire les parties du dernier block
        if end_block == 0:
            end_offset = end
        else:
            end_offset = end - self.prefix[end_block -1]

        # Premier block partiel
        c, l = self.rle[start_block]
        first_len = l - start_offset if start_block == end_block else l - start_offset
        if start_block == end_block:
            first_len = end_offset - start_offset
            if first_len > 0:
                result.append([c, first_len])
        else:
            if first_len > 0:
                result.append([c, first_len])
            # blocs complets suivants (sauf dernier)
            for i in range(start_block + 1, end_block):
                result.append([self.rle[i][0], self.rle[i][1]])
            # dernier bloc partiel
            c2, l2 = self.rle[end_block]
            if end_offset > 0:
                result.append([c2, end_offset])

        return result

    # Fonction utilitaire pour fusionner les blocs RLE consécutifs identiques en un seul
    @staticmethod
    def merge_rle_blocks(blocks):
        if not blocks:
            return []
        merged = [blocks[0][:]]  # copier le premier
        for c, l in blocks[1:]:
            if c == merged[-1][0]:
                merged[-1][1] += l
            else:
                merged.append([c, l])
        return merged


def main():
    # Lecture des RLE
    A_rle = read_rle_line()
    B_rle = read_rle_line()
    C_rle = read_rle_line()

    A = RLEString(A_rle)
    B = RLEString(B_rle)
    C = C_rle

    len_A = A.total_length
    len_B = B.total_length

    # Si B est plus grand que A, pas de remplacement possible
    if len_B > len_A:
        # Affichage de A sans changement
        out_rle = A.rle
    else:
        # On recherche la première occurrence de B dans A par parcours naïf
        # Pour chaque position i in [0 .. len_A - len_B], on vérifie substring A[i:i+len_B] == B
        # On compare caractère par caractère avec char_at (pas de déroulement complet!)

        found_pos = -1
        for start_pos in range(len_A - len_B + 1):
            match = True
            for offset in range(len_B):
                if A.char_at(start_pos + offset) != B.char_at(offset):
                    match = False
                    break
            if match:
                found_pos = start_pos
                break

        if found_pos == -1:
            # On ne trouve pas B dans A -> on affiche A sans changement
            out_rle = A.rle
        else:
            # Sinon on remplace la première occurrence de B à found_pos par C
            # Construction du nouveau RLE :
            # Partie avant occurrence: A[0:found_pos)
            # Partie C
            # Partie après occurrence: A[found_pos + len_B : len_A)
            part1 = A.slice(0, found_pos)
            part3 = A.slice(found_pos + len_B, len_A)
            combined = part1 + C + part3
            # Fusionner blocs consécutifs ayant même caractère
            out_rle = RLEString.merge_rle_blocks(combined)

    # Afficher le résultat au format demandé
    for c, l in out_rle:
        print(c, l, end=' ')
    print('$')

if __name__ == '__main__':
    main()