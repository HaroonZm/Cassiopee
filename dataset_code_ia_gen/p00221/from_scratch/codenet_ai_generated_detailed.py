def is_correct_say(number, say):
    """
    Vérifie si la déclaration 'say' correspond à ce qui devrait être dit pour 'number' selon les règles FizzBuzz.
    Retourne True si c'est correct, False sinon.
    """
    if number % 15 == 0:
        return say == "FizzBuzz"
    elif number % 3 == 0:
        return say == "Fizz"
    elif number % 5 == 0:
        return say == "Buzz"
    else:
        # Le say est censé être le nombre lui-même (en string)
        return say == str(number)

def next_active_player(players, current_index):
    """
    Trouve l'indice du prochain joueur actif (non éliminé) en suivant l'ordre circulaire à partir de current_index+1.
    """
    m = len(players)
    idx = (current_index + 1) % m
    while not players[idx]:
        idx = (idx + 1) % m
    return idx

def count_active_players(players):
    """
    Compte combien de joueurs sont encore actifs (True dans la liste players).
    """
    return sum(1 for p in players if p)

def main():
    import sys
    input_lines = sys.stdin.read().splitlines()
    line_idx = 0
    while True:
        if line_idx >= len(input_lines):
            break
        m_n_line = input_lines[line_idx].strip()
        line_idx += 1
        if not m_n_line:
            continue
        m, n = m_n_line.split()
        m = int(m)
        n = int(n)
        if m == 0 and n == 0:
            # Fin du traitement
            break
        # Lecture des déclarations
        says = []
        for _ in range(n):
            says.append(input_lines[line_idx].strip())
            line_idx += 1

        # Initialisation des joueurs : True signifie non éliminé
        players = [True] * m

        # Indice du joueur qui doit parler, on commence avec joueur 0 (numérotation interne)
        current_player = 0
        # Prochain numéro attendu à dire
        current_number = 1
        # Flag indiquant si le jeu est terminé (quand il ne reste qu'un joueur)
        game_over = False

        # Parcours des déclarations données par l'ordre des joueurs actifs
        i_say = 0
        while i_say < n and not game_over:
            # Si le joueur actuel est éliminé, on saute au joueur actif suivant
            while not players[current_player]:
                current_player = next_active_player(players, current_player)

            # Vérification de la déclaration actuelle du joueur
            correct = is_correct_say(current_number, says[i_say])
            if not correct:
                # Le joueur fait une erreur, il est éliminé
                players[current_player] = False
                # Le prochain joueur à parler doit commencer au nombre suivant au nombre erroné
                current_number += 1
                # Le joueur à parler après l'élimination est le suivant actif (on le trouve ici)
                current_player = next_active_player(players, current_player)

                # On vérifie si un seul joueur reste encore
                if count_active_players(players) == 1:
                    game_over = True
                # On continue sans avancer l'indice i_say car on considère que la déclaration fausse correspond à ce tour
                # On passe au prochain i_say pour suivre le input
                i_say += 1
                continue
            else:
                # Déclaration correcte
                current_number += 1
                current_player = next_active_player(players, current_player)
                i_say += 1
                # On vérifie aussi si après déclaration il ne reste qu'un joueur (cas non probable ici mais pour être sûr)
                if count_active_players(players) == 1:
                    game_over = True

        # Après la fin des déclarations ou du jeu, sortie des joueurs restants
        remaining_players = [str(i+1) for i, active in enumerate(players) if active]
        print(" ".join(remaining_players))

if __name__ == "__main__":
    main()