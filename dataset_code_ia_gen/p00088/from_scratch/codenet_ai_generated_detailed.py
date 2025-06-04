# Codage des caractères selon la première table (caractère -> code binaire)
char_to_code = {
    ' ': '101',
    '\'': '000000',
    ',': '000011',
    '-': '10010001',
    '.': '010001',
    '?': '000001',
    'A': '100101',
    'B': '10011010',
    'C': '0101',
    'D': '0001',
    'E': '110',
    'F': '01001',
    'G': '10011011',
    'H': '010000',
    'I': '0111',
    'J': '10011000',
    'K': '0110',
    'L': '00100',
    'M': '10011001',
    'N': '10011110',
    'O': '00101',
    'P': '111',
    'Q': '10011111',
    'R': '1000',
    'S': '00110',
    'T': '00111',
    'U': '10011100',
    'V': '10011101',
    'W': '000010',
    'X': '10010010',
    'Y': '10010011',
    'Z': '10010000'
}

# Décodage de la deuxième table (code binaire 5 bits -> caractère)
code_to_char = {
    '00000': 'A',
    '00001': 'B',
    '00010': 'C',
    '00011': 'D',
    '00100': 'E',
    '00101': 'F',
    '00110': 'G',
    '00111': 'H',
    '01000': 'I',
    '01001': 'J',
    '01010': 'K',
    '01011': 'L',
    '01100': 'M',
    '01101': 'N',
    '01110': 'O',
    '01111': 'P',
    '10000': 'Q',
    '10001': 'R',
    '10010': 'S',
    '10011': 'T',
    '10100': 'U',
    '10101': 'V',
    '10110': 'W',
    '10111': 'X',
    '11000': 'Y',
    '11001': 'Z',
    '11010': ' ',
    '11011': '.',
    '11100': ',',
    '11101': '-',
    '11110': '\'',
    '11111': '?'
}

import sys

for line in sys.stdin:
    line = line.rstrip('\n')
    if not line:
        continue

    # 1. Conversion du texte en code binaire concaténé
    binary_str = ""
    for ch in line:
        # Ajouter le code correspondant au caractère
        # Tous les caractères sont supposés être inclus dans la table selon l'énoncé
        binary_str += char_to_code[ch]

    # 2. Découpage en morceaux de 5 bits
    # Si le dernier morceau est incomplet, on complète avec des '0'
    remainder = len(binary_str) % 5
    if remainder != 0:
        padding = 5 - remainder
        binary_str += '0' * padding
    else:
        padding = 0

    # 3. Décoder chaque segment de 5 bits en un caractère selon la deuxième table
    result = ""
    for i in range(0, len(binary_str), 5):
        five_bits = binary_str[i:i+5]
        # Correspondance garantie par la table, donc directement décoder
        result += code_to_char[five_bits]

    # 4. Affichage du résultat
    print(result)