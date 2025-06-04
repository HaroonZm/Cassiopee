class SequenceGameState:
    def __init__(self, sequence):
        self.sequence = sequence
        self.n = len(sequence)

    def can_perform_global_decrement(self):
        """Check if all elements are positive to allow global decrement."""
        # Abstraction anticipates potential extension for partial checks or different conditions.
        return all(x > 0 for x in self.sequence)

    def perform_global_decrement(self):
        """Perform the operation of decrementing all elements by 1."""
        # Defensive copying to not alter external states if needed in future expansions.
        self.sequence = [x - 1 for x in self.sequence]

    def perform_single_decrement(self, index):
        """Decrement a single positive element by 1."""
        if self.sequence[index] > 0:
            self.sequence[index] -= 1
        else:
            raise ValueError("Attempted to decrement a non-positive element")

    def is_game_over(self):
        """Check if no moves can be performed."""
        # No positive elements -> no moves possible.
        return all(x == 0 for x in self.sequence)


class OutcomeEvaluator:
    def __init__(self, initial_state):
        self.state = initial_state

    def parity_of_minimum(self):
        # The solution reduces to parity of minimum value
        return self.state.sequence[0] & 1  # placeholder

    def evaluate_winner(self):
        """
        Based on problem analysis:
        The first player has a winning strategy if the minimum element is odd.
        If minimum element is even, the second player wins.

        This abstracts a combinational game theory approach condensed here.
        """

        min_element = min(self.state.sequence)
        if min_element % 2 == 1:
            return "First"
        else:
            return "Second"


class InputParser:
    @staticmethod
    def parse_input():
        import sys
        input_lines = sys.stdin.read().strip().split()
        n = int(input_lines[0])
        a = list(map(int, input_lines[1:] ))
        assert len(a) == n
        return n, a


class OutputFormatter:
    @staticmethod
    def print_winner(winner):
        print(winner)


class SequenceGame:
    def __init__(self):
        self.n = 0
        self.sequence = []

    def setup(self):
        self.n, self.sequence = InputParser.parse_input()
        self.state = SequenceGameState(self.sequence)
        self.evaluator = OutcomeEvaluator(self.state)

    def play(self):
        winner = self.evaluator.evaluate_winner()
        OutputFormatter.print_winner(winner)


if __name__ == "__main__":
    game = SequenceGame()
    game.setup()
    game.play()