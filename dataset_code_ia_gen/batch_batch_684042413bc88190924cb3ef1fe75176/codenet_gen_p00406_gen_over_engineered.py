class ArrowDirection:
    LEFT = 0
    RIGHT = 1

class Piece:
    def __init__(self, position: int, direction: int):
        self.position = position
        self.direction = direction

    def __repr__(self):
        return f"Piece(pos={self.position}, dir={'R' if self.direction==ArrowDirection.RIGHT else 'L'})"

class Board:
    def __init__(self, length: int, pieces: list):
        self.length = length
        self.pieces = pieces  # List[Piece]

    def calculate_max_score(self) -> int:
        """
        Calculate the maximum achievable score given the problem constraints.
        The clever approach is:
        - Sort pieces by position.
        - The final positions will be each piece placed in distinct cells in ascending order.
        - We assign final positions as a strictly increasing sequence to maximize total score.
        - Score formula for each piece:
          (if moving in arrow direction +1 per step, else -1 per step.)
        There's a known formula:
        
        max score = sum over pieces of abs(final_pos_i - initial_pos_i),
        minus twice the sum of movements against arrow direction.
        
        But the optimal final positions are either the sorted initial positions or the sorted positions with some fixed offset.
        
        The problem states a maximum score always exists.
        The problem boils down to:
            max score = sum over i of abs(final[i] - p[i]) - 2 * sum over i of moves_against_direction
        
        Actually, solution is:
        Let us order the final positions as an increasing sequence f1 < f2 < ... < fN such that 1 <= f1 ...
        The maximum score is:
          sum of distances in direction of arrows minus sum in opposite direction.
        
        It is proven the maximum score is:
            sum over i of (fi - p_i) * (1 if arrow=right else -1)
        
        Because moving in arrow direction yields +1 per step, opposite yields -1.
        So total score = sum over all pieces of (fi - pi) if arrow=right, else (pi - fi).
        
        Since final positions are distinct and sorted, choosing final positions is like placing numbers 1..N (or any contiguous block).
        
        Generally, optimal final positions are the positions sorted to minimize penalties.
        
        The below implementation calculates the score using the method known: final positions are
        1,2,...,N and initial positions are p sorted; then:
        
        score = sum over i of abs(final_i - p_i) - 2 * sum over i with arrow opposite of movement
        
        The key insight is that maximizing score equals to maximizing the sum of displacement in the arrow direction.
        So maximum score = sum over i of abs(final_i - p_i) - 2 * sum over pieces moving against arrow.
        We can prove the maximum is sum over i of (final_i - p_i) * (1 if arrow=right else -1).
        
        We assign final positions equal to 1 to N in ascending order.
        """
        N = len(self.pieces)
        # Sort pieces by position to assign final positions 1..N in ascending order
        self.pieces.sort(key=lambda x: x.position)
        
        max_score = 0
        for i, piece in enumerate(self.pieces, start=1):
            displacement = i - piece.position
            if piece.direction == ArrowDirection.RIGHT:
                # moves in direction arrow gives +1 score per step
                max_score += displacement
            else:
                # direction is left, moving left +1, so moves to right are negative score
                max_score += -displacement
        return max_score

class InputParser:
    @staticmethod
    def parse_input():
        import sys
        input = sys.stdin.readline
        N, L = map(int, input().split())
        pieces = []
        for _ in range(N):
            p_i, d_i = map(int, input().split())
            pieces.append(Piece(p_i, d_i))
        return Board(L, pieces)

class SolutionRunner:
    def __init__(self):
        self.board = None

    def run(self):
        self.board = InputParser.parse_input()
        result = self.board.calculate_max_score()
        print(result)

if __name__ == "__main__":
    runner = SolutionRunner()
    runner.run()