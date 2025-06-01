class Game:
    """Représente une partie individuelle de la prise de pierres."""

    def __init__(self, stones: int, players: int):
        if stones < 2:
            raise ValueError("Le nombre de pierres doit être au moins 2.")
        if players < 2:
            raise ValueError("Le nombre de joueurs doit être au moins 2.")
        self.stones = stones
        self.players = players

    def get_winner(self) -> int:
        """
        Calcule quel joueur gagnera la partie.
        La règle : le dernier à prendre une pierre remporte la partie.
        """
        # Le gagnant correspond à l'indice du joueur qui prend la dernière pierre.
        winner = self.stones % self.players
        # Si le reste est 0, cela signifie que c'est le joueur P (le dernier) qui gagne.
        return winner if winner != 0 else self.players


class Tournament:
    """Gestion d'une série de parties (tournoi)."""

    def __init__(self):
        self.games = []

    def add_game(self, stones: int, players: int):
        game = Game(stones, players)
        self.games.append(game)

    def run(self):
        results = []
        for game in self.games:
            results.append(game.get_winner())
        return results


class InputProcessor:
    """Gestion de l'entrée et parsing."""

    @staticmethod
    def parse_input(input_lines):
        """
        Parse l'entrée multiple.
        Expects:
         - première ligne: nombre de parties N
         - lignes suivantes: K_i P_i (pierres et joueurs)
        """
        try:
            n = int(input_lines[0].strip())
            if not (1 <= n <= 100):
                raise ValueError("Le nombre de parties doit être entre 1 et 100.")

            games_data = []
            for i in range(1, n + 1):
                parts = input_lines[i].strip().split()
                if len(parts) != 2:
                    raise ValueError(f"Format incorrect à la ligne {i+1}")
                k, p = int(parts[0]), int(parts[1])
                if not (2 <= k <= 1000) or not (2 <= p <= 1000):
                    raise ValueError(f"Valeurs hors limites à la ligne {i+1}")
                games_data.append((k, p))
            return games_data
        except Exception as e:
            raise RuntimeError(f"Erreur d'analyse d'entrée: {e}")


class OutputProcessor:
    """Gestion de la sortie."""

    @staticmethod
    def format_output(results):
        """
        Formate la liste des résultats en chaîne à sortie standard.
        """
        return '\n'.join(str(r) for r in results)


def main():
    import sys
    input_lines = sys.stdin.read().strip().split('\n')
    tournament = Tournament()
    games_data = InputProcessor.parse_input(input_lines)
    for stones, players in games_data:
        tournament.add_game(stones, players)
    results = tournament.run()
    print(OutputProcessor.format_output(results))


if __name__ == '__main__':
    main()