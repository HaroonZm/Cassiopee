# Solution complète pour le problème "Where's Wally" en Python avec commentaires détaillés

import sys
import math

# Table de correspondance BASE64 spéciale fournie
base64_table = {}
# 'A'-'Z' 0-25
for i, c in enumerate("ABCDEFGHIJKLMNOPQRSTUVWXYZ"):
    base64_table[c] = i
# 'a'-'z' 26-51
for i, c in enumerate("abcdefghijklmnopqrstuvwxyz", start=26):
    base64_table[c] = i
# '0'-'9' 52-61
for i, c in enumerate("0123456789", start=52):
    base64_table[c] = i
# + 62
base64_table['+'] = 62
# / 63
base64_table['/'] = 63


def decode_line(encoded_line, width):
    """
    Décode une ligne encodée en base64 selon le format donné vers
    une liste de bits (0/1) de longueur width.
    Chaque caractère encode 6 bits, les plus significatifs à gauche.
    
    :param encoded_line: chaîne encodée
    :param width: largeur effective (nombre de bits)
    :return: liste de bits (int 0 ou 1) de longueur width
    """
    bits = []
    for c in encoded_line:
        val = base64_table[c]
        # Extraire bits de poids fort à faible dans le caractère
        for b in reversed(range(6)):  # 5 à 0
            bits.append((val >> b) & 1)
            if len(bits) == width:
                break
        if len(bits) == width:
            break
    # Il se peut que plus de bits soient décodés, on truncate
    return bits[:width]


def rotate_90(mat):
    """
    Rotation 90 degrés dans le sens horaire d'une matrice carrée p x p
    """
    p = len(mat)
    rotated = [[0]*p for _ in range(p)]
    for i in range(p):
        for j in range(p):
            rotated[j][p-1-i] = mat[i][j]
    return rotated


def mirror(mat):
    """
    Retourne une matrice par miroir horizontal
    """
    return [list(reversed(row)) for row in mat]


def generate_transformations(pattern):
    """
    Génère toutes les transformations du pattern : rotations (0°,90°,180°,270°)
    et miroir de chacune, au total 8 variantes.
    Retourne une liste de matrices distinctes.
    """
    variants = []
    current = pattern
    for _ in range(4):
        variants.append(current)
        current = rotate_90(current)
    mirrored = mirror(pattern)
    current = mirrored
    for _ in range(4):
        variants.append(current)
        current = rotate_90(current)
    # On élimine les doublons qui peuvent apparaître (ex: pattern symétrique)
    unique_variants = []
    seen = set()
    for var in variants:
        # convertir la matrice en tuple de tuples pour pouvoir hash
        tup = tuple(tuple(row) for row in var)
        if tup not in seen:
            seen.add(tup)
            unique_variants.append(var)
    return unique_variants


def match_at(image, pattern, start_i, start_j):
    """
    Vérifie si le pattern est exactement égal à la portion de image
    commençant à (start_i, start_j).
    
    :param image: liste de listes d'entiers 0/1
    :param pattern: matrice p x p de 0/1
    :param start_i: ligne de départ dans l'image
    :param start_j: colonne de départ dans l'image
    :return: True si correspondance parfaite, False sinon
    """
    p = len(pattern)
    for i in range(p):
        for j in range(p):
            if image[start_i + i][start_j + j] != pattern[i][j]:
                return False
    return True


def main():
    input_lines = sys.stdin.read().splitlines()
    
    idx = 0
    while True:
        if idx >= len(input_lines):
            break
        line = input_lines[idx].strip()
        idx += 1
        if line == '':
            continue
        w, h, p = map(int, line.split())
        if w == 0 and h == 0 and p == 0:
            break
        
        # Lire image
        image = []
        nchars_image_line = (w + 5) // 6  # nombre de caractères par ligne image
        for _ in range(h):
            encoded_line = input_lines[idx].rstrip()
            idx += 1
            bits_line = decode_line(encoded_line, w)
            image.append(bits_line)
        
        # Lire pattern
        pattern = []
        nchars_pattern_line = (p + 5) // 6
        for _ in range(p):
            encoded_line = input_lines[idx].rstrip()
            idx += 1
            bits_line = decode_line(encoded_line, p)
            pattern.append(bits_line)

        # Générer toutes les transformations distinctes du pattern
        pattern_variants = generate_transformations(pattern)

        # On va scanner l'image sur toutes les positions où un carré p x p est possible
        count = 0
        # Pour accélérer la recherche, on peut utiliser un set pour mémoriser les positions
        # déjà comptées (en théorie un carré ne devrait pas être compté deux fois)
        # mais le problème indique qu'on ne doit pas compter deux fois une même position,
        # même si elle correspond à plusieurs variantes. Donc on ne peut compter qu'une fois par position.
        matched_positions = set()
        
        for i in range(h - p + 1):
            for j in range(w - p + 1):
                # Pour la position (i,j), verifier si elle correspond à un des patterns
                if (i,j) in matched_positions:
                    continue
                matched = False
                for var in pattern_variants:
                    if match_at(image, var, i, j):
                        matched = True
                        break
                if matched:
                    count += 1
                    matched_positions.add((i,j))
        print(count)


if __name__ == "__main__":
    main()