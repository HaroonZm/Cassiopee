import sys
import re

# Bon, la fonction de chiffrement Caesar, je la mets là
def shift_text(line, n):
    # Attention, c'est juste pour les minuscules
    return re.sub(r"\w", lambda x: chr((ord(x.group(0)) - 97 + n) % 26 + 97), line)

for line in sys.stdin:
    # Heu, on va chercher combien il faut décaler
    offset = 0
    while not re.search(r"th(e|is|at)", shift_text(line, offset)):
        offset = offset + 1 # Incrémente jusqu'à trouver "the", "this" ou "that"
        if offset > 26: # on ne devrait jamais arriver là, mais bon
            break

    # Voilà, c'est déchiffré... enfin j'espère
    # On imprime sans espaces en trop
    print(shift_text(line, offset).strip())