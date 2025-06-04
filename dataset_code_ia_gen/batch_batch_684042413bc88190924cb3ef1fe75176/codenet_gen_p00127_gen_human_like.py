# Création d'une table de correspondance entre les codes 2 chiffres et les caractères
code_map = {
    '11': 'a', '12': 'b', '13': 'c', '14': 'd', '15': 'e',
    '21': 'f', '22': 'g', '23': 'h', '24': 'i', '25': 'j',
    '31': 'k', '32': 'l', '33': 'm', '34': 'n', '35': 'o',
    '41': 'p', '42': 'q', '43': 'r', '44': 's', '45': 't',
    '51': 'u', '52': 'v', '53': 'w', '54': 'x', '55': 'y',
    '56': 'z', '61': '.', '62': '?', '63': '!', '64': ' '
}

import sys

for line in sys.stdin:
    msg = line.strip()
    # Vérifier que la longueur est paire, car chaque caractère est codé sur 2 chiffres
    if len(msg) % 2 != 0:
        print("NA")
        continue
    result = []
    invalid = False
    for i in range(0, len(msg), 2):
        code = msg[i:i+2]
        if code not in code_map:
            invalid = True
            break
        result.append(code_map[code])
    if invalid:
        print("NA")
    else:
        print("".join(result))