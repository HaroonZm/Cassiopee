from typing import List, Optional, Tuple
import itertools

class Player:
    def __init__(self, identifier: int, value: int):
        self.id = identifier
        self.value = value

    def __repr__(self):
        return f"Player(id={self.id}, value={self.value})"


class ProductValidator:
    """
    Validator class to check whether the product of two player values
    results in a string of digits which are strictly increasing consecutive.
    """
    @staticmethod
    def is_strictly_increasing_consecutive(num: int) -> bool:
        s = str(num)
        if len(s) == 1:
            # Single digit is trivially strictly increasing consecutive
            return True
        for i in range(1, len(s)):
            prev_digit = int(s[i-1])
            curr_digit = int(s[i])
            if curr_digit != prev_digit + 1:
                return False
        return True


class TournamentRules:
    """
    Encapsulates the game's rules for pair formation and validation.
    """
    def __init__(self, players: List[Player]):
        self.players = players
        self.validator = ProductValidator()

    def valid_pair_product(self, p1: Player, p2: Player) -> Optional[int]:
        prod = p1.value * p2.value
        if self.validator.is_strictly_increasing_consecutive(prod):
            return prod
        else:
            return None


class PairMatcher:
    """
    Responsible for determining the largest valid product among all pairs.
    Employs combinatorics and rules validation.
    """
    def __init__(self, rules: TournamentRules):
        self.rules = rules

    def find_best_matched_pair_product(self) -> int:
        max_product = -1
        players = self.rules.players
        # Iterate over all distinct pairs (i < j)
        for p1, p2 in itertools.combinations(players, 2):
            product = self.rules.valid_pair_product(p1, p2)
            if product is not None and product > max_product:
                max_product = product
        return max_product


class InputProcessor:
    """
    Reads and parses the problem input, producing Player objects.
    """
    @staticmethod
    def read_input() -> List[Player]:
        n = int(input())
        values = list(map(int, input().strip().split()))
        players = [Player(i, v) for i, v in enumerate(values)]
        return players


class OutputManager:
    """
    Responsible for producing output in required format.
    """
    @staticmethod
    def print_result(result: int) -> None:
        print(result)


class BestMatchedPairGame:
    """
    High-level orchestrator class for the problem.
    """
    def __init__(self):
        self.players: List[Player] = []

    def run(self) -> None:
        self.players = InputProcessor.read_input()
        rules = TournamentRules(self.players)
        matcher = PairMatcher(rules)
        best_product = matcher.find_best_matched_pair_product()
        OutputManager.print_result(best_product)


if __name__ == "__main__":
    game = BestMatchedPairGame()
    game.run()