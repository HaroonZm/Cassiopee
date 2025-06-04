def decrypt_swap_cipher():
    import sys

    # Fonction pour reculer un caractère c de 'diff' positions dans l'alphabet circulaire
    def shift_back(c, diff):
        # Convertir le caractère en son rang alphabétique (0 pour 'a', 25 pour 'z')
        pos = ord(c) - ord('a')
        # Reculer de diff positions avec wrap-around modulo 26
        new_pos = (pos - diff) % 26
        return chr(new_pos + ord('a'))

    input_lines = sys.stdin.read().strip().split('\n')
    idx = 0
    while True:
        if idx >= len(input_lines):
            break
        N_line = input_lines[idx].strip()
        idx += 1
        if N_line == '0':
            # Fin des données
            break

        N = int(N_line)
        # Message chiffré
        message = list(input_lines[idx].strip())
        idx += 1

        # Lire les opérations de swap
        swaps = []
        for _ in range(N):
            a_str, b_str = input_lines[idx].split()
            idx += 1
            a = int(a_str)
            b = int(b_str)
            swaps.append((a, b))

        # Pour déchiffrer, il faut appliquer l'inverse des opérations dans l'ordre inverse
        # Puisqu'en chiffrement on swap et ensuite on recule les lettres du diff,
        # pour déchiffrer on avance les lettres du diff (le « inverse » du recul), puis swap à nouveau.

        # Ici, on va appliquer le déchiffrement en partant du dernier swap vers le premier.
        # Le déchiffrement:
        # 1. Avancer les lettres aux positions a_i, b_i du diff (pour annuler le recul)
        # 2. Swap ces deux lettres

        # Cependant, dans l'énoncé, "アルファベット順で、'a'の前は'z'とする。" pour le recul, donc inverse: avancer correspond au recul négatif avec wrap.

        for a, b in reversed(swaps):
            diff = b - a
            # Les indices dans la liste sont a-1, b-1
            a_idx = a - 1
            b_idx = b - 1

            # Avancer les deux lettres du diff (car en chiffrement on a reculé, donc inverse est avancer)
            # Avancer : c → c+diff modulo, mais comme on a fait reculer dans le chiffrement,
            # ici on fait avancer.
            # Mais dans l'exemple, recul est "戻す" qui signifie revenir en arrière, donc inverse est avancer
            # Avancer le caractère
            def shift_forward(c, diff):
                pos = ord(c) - ord('a')
                new_pos = (pos + diff) % 26
                return chr(new_pos + ord('a'))

            message[a_idx] = shift_forward(message[a_idx], diff)
            message[b_idx] = shift_forward(message[b_idx], diff)

            # Ensuite swap à nouveau
            message[a_idx], message[b_idx] = message[b_idx], message[a_idx]

        # Afficher le message déchiffré
        print(''.join(message))


if __name__ == "__main__":
    decrypt_swap_cipher()