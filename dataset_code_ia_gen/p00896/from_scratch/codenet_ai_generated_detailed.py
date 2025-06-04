# Solution complète en Python avec commentaires détaillés

def solve():
    import sys

    # Fonction de backtracking pour retrouver le texte en clair
    def backtrack(cipher_words, candidate_lists, idx, forward_map, backward_map, result):
        # Si on a traité tous les mots ciphertext, on a trouvé une solution valide
        if idx == len(cipher_words):
            return True

        cword = cipher_words[idx]
        candidates = candidate_lists[idx]

        for pword in candidates:
            # Essayer d'établir la correspondance entre cword et pword en respectant les contraintes
            temp_forward = forward_map.copy()
            temp_backward = backward_map.copy()
            consistent = True

            for c_char, p_char in zip(cword, pword):
                # Si la lettre ciphertext est déjà mappée
                if c_char in temp_forward:
                    if temp_forward[c_char] != p_char:
                        consistent = False
                        break
                else:
                    # Si la lettre plaintext est déjà utilisée par une autre lettre ciphertext
                    if p_char in temp_backward:
                        consistent = False
                        break
                    temp_forward[c_char] = p_char
                    temp_backward[p_char] = c_char

            if consistent:
                # Réessayer avec cette correspondance étendue
                if backtrack(cipher_words, candidate_lists, idx + 1, temp_forward, temp_backward, result):
                    result[idx] = pword
                    return True

        return False

    input_lines = sys.stdin.read().strip('\n').split('\n')
    pos = 0

    while True:
        if pos >= len(input_lines):
            break
        n = input_lines[pos].strip()
        pos += 1
        if n == '0':
            # Fin de tous les jeux de données
            break

        n = int(n)
        candidate_words = []
        for _ in range(n):
            candidate_words.append(input_lines[pos].strip())
            pos += 1

        # Lecture de la séquence chiffrée, se termine par un '.'
        sequence_line = input_lines[pos].strip()
        pos += 1
        # La séquence se termine par un point, on le supprime
        if sequence_line.endswith('.'):
            sequence_line = sequence_line[:-1]
        cipher_words = sequence_line.strip().split()

        # Préparation d'une liste candidate_lists où pour chaque mot ciphertext on aura la liste
        # des mots candidats possibles (de même longueur que le mot ciphertext)
        candidate_lists = []
        for cword in cipher_words:
            filtered = [w for w in candidate_words if len(w) == len(cword)]
            candidate_lists.append(filtered)

        # On cherche à trouver une solution unique: backtracking + détection d'ambiguïté
        # Pour cela on va faire un backtracking et compter le nombre de solutions trouvées.
        # Dès qu'on trouve une deuxième solution, on arrête (ambigu).

        solutions = []
        def backtrack_all(cipher_words, candidate_lists, idx, forward_map, backward_map, current_solution):
            if idx == len(cipher_words):
                # solution complète trouvée
                solutions.append(current_solution[:])
                # s'il y a plus d'une solution, on peut arrêter
                return len(solutions) < 2

            cword = cipher_words[idx]
            candidates = candidate_lists[idx]

            for pword in candidates:
                temp_forward = forward_map.copy()
                temp_backward = backward_map.copy()
                consistent = True

                for c_char, p_char in zip(cword, pword):
                    if c_char in temp_forward:
                        if temp_forward[c_char] != p_char:
                            consistent = False
                            break
                    else:
                        if p_char in temp_backward:
                            consistent = False
                            break
                        temp_forward[c_char] = p_char
                        temp_backward[p_char] = c_char

                if consistent:
                    current_solution.append(pword)
                    can_continue = backtrack_all(cipher_words, candidate_lists, idx + 1, temp_forward, temp_backward, current_solution)
                    current_solution.pop()
                    if not can_continue:
                        return False
            return True

        backtrack_all(cipher_words, candidate_lists, 0, {}, {}, [])

        # Si on a zero solution ou plus d'une solution, on imprime -.
        # Sinon, on affiche la solution trouvée
        if len(solutions) != 1:
            print("-.")
        else:
            print(' '.join(solutions[0]) + '.')


if __name__ == "__main__":
    solve()