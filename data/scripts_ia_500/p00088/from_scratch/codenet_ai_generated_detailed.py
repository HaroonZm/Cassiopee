# Définition des tables de correspondance données dans l'énoncé

# Table de conversion du premier code:
first_code_map = {
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
    'Z': '10010000',
}

# Table inverse de correspondance du second code:
second_code_map = {
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
    '11111': '?',
}

import sys

def encode_first_code(line):
    """
    Transforme chaque caractère de la ligne en son code binaire à partir de first_code_map
    puis concatène tous les codes en une seule chaîne.
    """
    result_bits = []
    for ch in line:
        code = first_code_map[ch]
        result_bits.append(code)
    return ''.join(result_bits)

def split_and_pad_bits(bits):
    """
    Sépare la chaîne binaire en sous-chaînes de longueur 5.
    Si la dernière sous-chaîne a moins de 5 caractères,
    complète avec des '0' jusqu'à 5 caractères.
    """
    chunks = []
    for i in range(0, len(bits), 5):
        chunk = bits[i:i+5]
        if len(chunk) < 5:
            chunk = chunk + '0' * (5 - len(chunk))
        chunks.append(chunk)
    return chunks

def decode_second_code(chunks):
    """
    Pour chaque groupe de 5 bits (chunk), récupère le caractère correspondant dans la table second_code_map.
    Concatène les caractères décodés et retourne la chaîne finale.
    """
    decoded_chars = []
    for c in chunks:
        decoded_chars.append(second_code_map[c])
    return ''.join(decoded_chars)

def main():
    for line in sys.stdin:
        line = line.strip()
        if not line:
            continue
        # Étape 1 : encoder la ligne en chaîne binaire selon first_code_map
        bits = encode_first_code(line)
        # Étape 2 : découper en groupes de 5 bits et compléter avec des zéros si nécessaire
        chunks_5 = split_and_pad_bits(bits)
        # Étape 3 : décoder avec second_code_map chaque groupe de 5 bits
        result = decode_second_code(chunks_5)
        print(result)

if __name__ == "__main__":
    main()