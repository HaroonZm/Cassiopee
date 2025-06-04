def calc_scores(serve_record):
    scores = {'A': 0, 'B': 0}
    winner_scores = []
    current_server = None
    game_number = 1
    idx = 0
    n = len(serve_record)
    while game_number <= 3:
        scores = {'A': 0, 'B': 0}
        # Determine first server of current game
        if game_number == 1:
            first_server = 'A'
        else:
            # first server is previous game's winner
            first_server = winner
        current_server = first_server

        while True:
            if idx >= n:
                # No more serves in the record, break
                break
            server = serve_record[idx]
            idx += 1
            # The point goes to the server
            scores[server] += 1
            # After point, server is point winner
            current_server = server
            a = scores['A']
            b = scores['B']
            # Check if game finished
            if (a >= 11 or b >= 11) and abs(a - b) >= 2:
                winner = 'A' if a > b else 'B'
                winner_scores.append((a, b))
                game_number += 1
                break
            # Check deuce (>=10-10) rule
            if a >= 10 and b >= 10:
                if abs(a - b) >= 2:
                    winner = 'A' if a > b else 'B'
                    winner_scores.append((a, b))
                    game_number += 1
                    break
    return winner_scores


def main():
    import sys
    lines = []
    for line in sys.stdin:
        line = line.strip()
        if line == '0':
            break
        lines.append(line)

    for i in range(0, len(lines), 3):
        game1 = lines[i]
        game2 = lines[i+1]
        game3 = lines[i+2]
        scores = []
        scores.extend(calc_scores(game1))
        scores.extend(calc_scores(game2))
        scores.extend(calc_scores(game3))
        # Actually, calc_scores receives a single string with all serves for 3 games,
        # but problem input gives 3 lines per dataset, each is one game's serves.
        # So we need to call calc_scores only for one game per call.
        # The above code was doing full three games at once, so rewrite main accordingly.

def main():
    import sys
    lines = []
    for line in sys.stdin:
        line = line.strip()
        if line == '0':
            break
        lines.append(line)

    for i in range(0, len(lines), 3):
        game1 = lines[i]
        game2 = lines[i+1]
        game3 = lines[i+2]

        # For each game, run calc_scores on that single game's serve record (partial)
        # But calc_scores expects 3 games at once, so write helper to process single game

        def calc_single_game(serve_record, first_server):
            scores = {'A':0, 'B':0}
            current_server = first_server
            for s in serve_record:
                scores[s] += 1
                current_server = s
                a = scores['A']
                b = scores['B']
                if (a >= 11 or b >= 11) and abs(a - b) >= 2:
                    return scores['A'], scores['B'], 'A' if a > b else 'B'
                if a >= 10 and b >= 10:
                    if abs(a - b) >= 2:
                        return scores['A'], scores['B'], 'A' if a > b else 'B'
            # If no winner found (should not happen), return current scores and last server as winner
            if scores['A'] > scores['B']:
                return scores['A'], scores['B'], 'A'
            else:
                return scores['A'], scores['B'], 'B'

        # Game 1 first server is A
        a1, b1, w1 = calc_single_game(game1, 'A')
        # Game 2 first server is previous winner
        a2, b2, w2 = calc_single_game(game2, w1)
        # Game 3 first server is previous winner
        a3, b3, w3 = calc_single_game(game3, w2)

        print(a1, b1)
        print(a2, b2)
        print(a3, b3)

if __name__ == '__main__':
    main()