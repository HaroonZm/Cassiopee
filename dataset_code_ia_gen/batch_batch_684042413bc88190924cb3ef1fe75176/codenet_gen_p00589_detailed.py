# Définition des mappings des touches vers leurs caractères correspondants
# Chaque bouton (1 à 9) est associé à une chaîne de caractères cycle, la position dans cette chaîne
# dépend du nombre de pressions consécutives sur la même touche.
# Le bouton 0 est un cas spécial géré à part.
BUTTON_MAP = {
    '1': "',.?!' ",  # Bouton 1 cycle sur les caractères ',.?!'
    '2': "abcABC",
    '3': "defDEF",
    '4': "ghiGHI",
    '5': "jklJKL",
    '6': "mnoMNO",
    '7': "pqrsPQRS",
    '8': "tuvTUV",
    '9': "wxyzWXYZ"
}

def decode_line(line):
    """
    Décode une ligne de séquence de bouton en texte lisible selon les règles du problème.
    """
    result = []
    i = 0
    n = len(line)

    while i < n:
        current_char = line[i]

        if current_char == '0':
            # Cas du bouton 0
            # On compte le nombre de 0 consécutifs
            zero_count = 1
            i += 1
            while i < n and line[i] == '0':
                zero_count += 1
                i += 1
            # Si plusieurs 0 consécutifs, on affiche (zero_count -1) espaces
            # Sinon un seul 0 isolé n'arrive pas selon l'énoncé (jamais au début)
            # donc ici toujours >=1
            if zero_count == 1:
                # un seul 0, ce cas n'est pas censé arriver selon l'énoncé (il ne pousse jamais 0 au début)
                # mais si cela arrive, on considère que ça active la saisie continue
                # => on ne produit pas de caractère immédiat, on poursuit
                pass
            else:
                spaces_count = zero_count -1
                result.append(' ' * spaces_count)
        else:
            # Boutons 1 à 9
            # Compter le nombre de pressions consécutives sur la même touche
            count = 1
            i += 1
            while i < n and line[i] == current_char:
                count += 1
                i += 1

            # Si la touche précédente est la même que la touche courante,
            # on doit gérer la saisie continue activée par le bouton 0.
            # Or l'énoncé précise que 0 permet d'entrer plusieurs fois la même touche en série.

            # Donc sans 0 entre deux séries de la même touche, on a un seul groupe.
            # Ici on décode simplement en utilisant le nombre de pressions modulo la longueur
            chars = BUTTON_MAP[current_char]
            length = len(chars)
            # La position du caractère est (count-1) modulo la longueur du cycle
            pos = (count - 1) % length
            result.append(chars[pos])

    return ''.join(result)

import sys

for line in sys.stdin:
    line = line.strip()
    if not line:
        continue
    # Ligne décodée
    decoded = decode_line(line)
    print(decoded)