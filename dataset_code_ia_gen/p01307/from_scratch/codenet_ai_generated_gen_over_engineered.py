from abc import ABC, abstractmethod
from typing import Tuple, List, Dict

class Player(ABC):
    @abstractmethod
    def name(self) -> str:
        pass

class Fabre(Player):
    def name(self) -> str:
        return "Fabre"

class Audrey(Player):
    def name(self) -> str:
        return "Audrey"

class GameState:
    def __init__(self, number: str):
        self.number = number

    def __hash__(self):
        return hash(self.number)

    def __eq__(self, other):
        if not isinstance(other, GameState):
            return False
        return self.number == other.number

    def is_terminal(self) -> bool:
        return len(self.number) == 1

    def generate_next_states(self) -> List['GameState']:
        # From current number, generate all possible next states according to rules
        next_states = []
        digits = list(map(int, self.number))
        n = len(digits)
        for i in range(n-1):
            # sum of adjacent i and i+1 digits
            s = digits[i] + digits[i+1]
            # create new digits list with i and i+1 replaced by s
            new_digits = digits[:i] + [s] + digits[i+2:]
            new_number_str = "".join(str(d) for d in new_digits)
            next_states.append(GameState(new_number_str))
        return next_states

class Outcome:
    def __init__(self, winner: Player):
        self.winner = winner

class Strategy(ABC):
    @abstractmethod
    def decide_winner(self, state: GameState, is_first_player_turn: bool) -> Player:
        pass

class MinimaxStrategy(Strategy):
    def __init__(self, first_player: Player, second_player: Player):
        self.first_player = first_player
        self.second_player = second_player
        self.memo: Dict[Tuple[str,bool], Player] = {}

    def decide_winner(self, state: GameState, is_first_player_turn: bool) -> Player:
        key = (state.number, is_first_player_turn)
        if key in self.memo:
            return self.memo[key]

        if state.is_terminal():
            # The player who cannot move loses.
            # If it's first player's turn and no moves => first_player loses => second_player wins
            # So winner is the opponent of the current player who cannot move.
            winner = self.second_player if is_first_player_turn else self.first_player
            self.memo[key] = winner
            return winner

        next_states = state.generate_next_states()
        if not next_states:
            # No moves possible; current player loses => opponent wins
            winner = self.second_player if is_first_player_turn else self.first_player
            self.memo[key] = winner
            return winner

        # Current player tries to move so that they can win
        current_player = self.first_player if is_first_player_turn else self.second_player
        opponent = self.second_player if is_first_player_turn else self.first_player

        for nxt in next_states:
            nxt_winner = self.decide_winner(nxt, not is_first_player_turn)
            if nxt_winner == current_player:
                # Current player can force a win
                self.memo[key] = current_player
                return current_player

        # Otherwise, opponent wins
        self.memo[key] = opponent
        return opponent

class Game:
    def __init__(self, initial_number: str, first_player: Player, second_player: Player):
        self.state = GameState(initial_number)
        self.first_player = first_player
        self.second_player = second_player
        # For now, use minimax strategy with memoization
        self.strategy = MinimaxStrategy(first_player, second_player)

    def play(self) -> Player:
        return self.strategy.decide_winner(self.state, True)

class InputParser:
    def __init__(self):
        pass

    def parse_input(self) -> List[str]:
        dataset_count = int(input())
        numbers = []
        for _ in range(dataset_count):
            num_str = input().strip()
            numbers.append(num_str)
        return numbers

class OutputFormatter:
    def __init__(self):
        pass

    def format_winner(self, player: Player) -> str:
        # According to problem statement, add period at end
        return f"{player.name()} wins."

def main():
    parser = InputParser()
    formatter = OutputFormatter()
    player1 = Fabre()
    player2 = Audrey()

    test_numbers = parser.parse_input()

    for number in test_numbers:
        game = Game(number, player1, player2)
        winner = game.play()
        print(formatter.format_winner(winner))

if __name__ == "__main__":
    main()