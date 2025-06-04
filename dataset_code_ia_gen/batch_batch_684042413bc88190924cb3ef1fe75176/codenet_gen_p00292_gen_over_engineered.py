class Game:
    def __init__(self, stones: int, players: int):
        self.stones = stones
        self.players = players

    def winner(self) -> int:
        # The winner is the player who picks the last stone.
        # Since players take stones in order until stones run out,
        # the winner is the (stones % players)th player, with wrap-around to players if remainder is 0.
        remainder = self.stones % self.players
        return remainder if remainder != 0 else self.players


class GameFactory:
    @staticmethod
    def create_game(stones: int, players: int) -> Game:
        return Game(stones, players)


class GameSession:
    def __init__(self, game_data: list[tuple[int, int]]):
        self.games = [GameFactory.create_game(stones, players) for stones, players in game_data]

    def run(self) -> list[int]:
        return [game.winner() for game in self.games]


class InputParser:
    def __init__(self, raw_input: str):
        self.raw_input = raw_input

    def parse(self) -> tuple[int, list[tuple[int, int]]]:
        lines = self.raw_input.strip().splitlines()
        n = int(lines[0])
        game_data = []
        for line in lines[1:n+1]:
            k_str, p_str = line.split()
            game_data.append((int(k_str), int(p_str)))
        return n, game_data


class OutputFormatter:
    @staticmethod
    def format(results: list[int]) -> str:
        return "\n".join(str(winner) for winner in results)


class GameController:
    def __init__(self, raw_input: str):
        self.parser = InputParser(raw_input)
        self.formatter = OutputFormatter()

    def execute(self) -> str:
        _, game_data = self.parser.parse()
        session = GameSession(game_data)
        results = session.run()
        return self.formatter.format(results)


def main():
    import sys
    raw_input = sys.stdin.read()
    controller = GameController(raw_input)
    print(controller.execute())


if __name__ == "__main__":
    main()