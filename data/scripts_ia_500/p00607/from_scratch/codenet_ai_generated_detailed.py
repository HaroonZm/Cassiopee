# Solution complète en Python avec commentaires détaillés pour le problème "Emacs-like Editor"

# L'idée est de simuler un éditeur de texte avec curseur et buffer.
# On doit gérer plusieurs lignes de texte, un curseur localisé par (ligne, position)
# et un buffer pouvant contenir une chaîne ou un saut de ligne.
#
# Opérations complexes notamment pour la gestion des coupures, collages et déplacements hors des bords.
#
# On stocke chaque ligne comme une liste de caractères pour faciliter les insertions et suppressions.
# La position du curseur 'pos' est un index dans la liste, pouvant aller de 0 (premier caractère) jusqu'à len(line) (fin de ligne).
# Le buffer peut être:
# - None (vide)
# - 'LF' (linefeed)
# - une string de caractères
#
# Lors d'un 'k' (cut), on doit couper soit tout jusqu'à la fin de la ligne, soit fusionner lignes si curseur en fin de ligne.
# Lors d'un 'y' (paste), on insère soit un saut de ligne, soit une chaîne à la position du curseur.
# Les mouvements doivent respecter les conditions indiquées.

import sys

def main():
    # Lecture du texte
    lines = []
    while True:
        line = sys.stdin.readline()
        if not line:
            break
        line = line.rstrip('\n')
        if line == "END_OF_TEXT":
            break
        lines.append(list(line))  # ligne sous forme de liste de caractères

    # Initialisation du curseur et du buffer
    # curseur = (ligne_index, position_index)
    cur_line = 0
    cur_pos = 0
    buffer = None  # None pour vide, "LF" pour saut de ligne, string pour chaine

    # Fonctions utilitaires
    def move_a():
        # a : curseur début ligne
        nonlocal cur_pos
        cur_pos = 0

    def move_e():
        # e : curseur fin ligne (pointant après le dernier caractère)
        nonlocal cur_pos
        cur_pos = len(lines[cur_line])  # pos juste après dernier char

    def move_p():
        # p : curseur première char de ligne au-dessus (ligne précédente)
        nonlocal cur_line, cur_pos
        if cur_line > 0:
            cur_line -= 1
            # Si ligne vide, curseur est à 0 (fin de ligne)
            cur_pos = 0
        else:
            # pas de ligne au-dessus: curseur reste début ligne courante
            cur_pos = 0

    def move_n():
        # n : curseur première char de ligne en-dessous (ligne suivante)
        nonlocal cur_line, cur_pos
        if cur_line + 1 < len(lines):
            cur_line += 1
            cur_pos = 0
        else:
            cur_pos = 0

    def move_f():
        # f : avancer curseur d'un caractère à droite
        # si en fin de ligne et ligne suivante existe, go début ligne suivante
        nonlocal cur_line, cur_pos
        line_len = len(lines[cur_line])
        if cur_pos < line_len:
            cur_pos += 1
        else:
            # en fin de ligne
            if cur_line + 1 < len(lines):
                cur_line += 1
                cur_pos = 0
            # sinon ne rien faire

    def move_b():
        # b : reculer curseur d'un caractère à gauche
        # si au début et ligne précédente existe, go fin ligne précédente
        nonlocal cur_line, cur_pos
        if cur_pos > 0:
            cur_pos -= 1
        else:
            if cur_line > 0:
                cur_line -= 1
                cur_pos = len(lines[cur_line])
            # sinon ne rien faire

    def command_d():
        # d : delete char à curseur si possible
        # si curseur à la fin de ligne et ligne suivante existe,
        # on fusionne ligne suivante à la ligne courante et supprime la la ligne suivante
        nonlocal cur_line, cur_pos
        line = lines[cur_line]
        if cur_pos < len(line):
            # on supprime le caractère à cur_pos
            del line[cur_pos]
        else:
            # curseur en fin de ligne
            if cur_line + 1 < len(lines):
                # fusionner ligne suivante avec ligne courante
                next_line = lines[cur_line+1]
                line.extend(next_line)
                del lines[cur_line+1]

    def command_k():
        # k : cut et enregistrer dans buffer
        nonlocal cur_line, cur_pos, buffer
        line = lines[cur_line]

        if cur_pos == len(line):
            # curseur en fin de ligne
            if cur_line + 1 < len(lines):
                # cut ligne suivante (fusion de d)
                command_d()
                buffer = 'LF'  # buffer garde un saut de ligne
            # sinon nada (buffer inchangé)
        else:
            # curseur sur un caractère
            # couper de cur_pos à fin de ligne et sauver dans buffer
            cut_chars = line[cur_pos:]
            buffer = ''.join(cut_chars)
            del line[cur_pos:]
            # curseur pointe à la fin de ligne
            cur_pos = len(line)

    def command_y():
        # y : coller le buffer à la position du curseur
        nonlocal cur_line, cur_pos, buffer, lines
        if buffer is None:
            return
        if buffer == 'LF':
            # insérer un saut de ligne à la position du curseur
            line = lines[cur_line]
            # séparer la ligne en 2 parts, insérer nouvelle ligne entre
            first_part = line[:cur_pos]
            second_part = line[cur_pos:]
            # remplacer ligne courante par first_part
            lines[cur_line] = first_part
            # insérer nouvelle ligne après avec second_part
            lines.insert(cur_line+1, second_part)
            # curseur va au début de la nouvelle ligne
            cur_line += 1
            cur_pos = 0
        else:
            # buffer est une chaîne de caractères à insérer à la position curseur
            line = lines[cur_line]
            # insertion
            for i, c in enumerate(buffer):
                line.insert(cur_pos + i, c)
            # curseur reste sur la même position (sur le premier caractère inséré)
            # ou end of line is possible if buffer is empty but it never is here
            # On laisse cur_pos inchangé car spécification demande de pointer sur le caractère ou l'end-of-line originel.
            # Dans ce cas la position reste celle d'origine (curseur devant les caractères insérés)
            # Exemple dans énoncé montre que curseur ne bouge pas (le "y" en second "y" dans l'exemple)
            # Donc rien à changer ici.

    # Dictionnaire des commandes pour appel facile
    commands = {
        'a': move_a,
        'e': move_e,
        'p': move_p,
        'n': move_n,
        'f': move_f,
        'b': move_b,
        'd': command_d,
        'k': command_k,
        'y': command_y,
    }

    # Lecture des commandes
    while True:
        cmd_line = sys.stdin.readline()
        if not cmd_line:
            break
        cmd_line = cmd_line.rstrip('\n')
        if cmd_line == '-':
            break
        if cmd_line in commands:
            commands[cmd_line]()

    # Affichage du texte final
    for line in lines:
        print(''.join(line))


if __name__ == "__main__":
    main()