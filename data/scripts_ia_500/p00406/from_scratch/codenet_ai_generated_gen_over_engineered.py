class Piece:
    def __init__(self, position: int, direction: int):
        self.position = position
        self.direction = direction  # 0: left, 1: right

class Board:
    def __init__(self, length: int, pieces: list):
        self.length = length
        self.pieces = pieces

class ScorerStrategy:
    def __init__(self):
        pass
    def calculate_score(self, board: Board) -> int:
        raise NotImplementedError

class MaxScoreCalculator(ScorerStrategy):
    def calculate_score(self, board: Board) -> int:
        # Sort pieces by position for structured processing
        pieces = sorted(board.pieces, key=lambda p: p.position)
        max_gain = 0

        # We'll process the pieces by aggregating how much each can move
        # considering all others to maximize the positive moves and minimize negative.

        # Let's gather all positions and directions separately
        positions = [p.position for p in pieces]
        directions = [p.direction for p in pieces]

        # The core insight (from editorial of similar problem):
        # The maximum score is sum of:
        #   - sum of distances moved right on right-facing pieces (+1 per step)
        #   - sum of distances moved left on left-facing pieces (+1 per step)
        # Since moves to opposite direction subtract points, best is to
        # move each piece towards a target position that maximizes the sum
        #
        # Because pieces can move left/right, and can be moved arbitrarily
        # but one step at a time, and no overlaps allowed,
        # we can think of final positions of pieces as a permutation of initial positions
        #
        # The target final positions must be distinct and between 1 and L.
        # The problem ensures a max score exists.
        #
        # We try to assign final positions so as to increase score.
        #
        # The maximal possible score corresponds to sum of displacement weighted by direction
        #
        # Approach:
        # For each piece i, define p_i initial position, d_i direction
        # Score contribution = (final_pos_i - p_i) if direction == 1 (right face)
        #                      (p_i - final_pos_i) if direction == 0 (left face)
        #
        # Our goal: find final_pos_i in [1..L], distinct, maximize sum over i of above.
        #
        # We can rewrite as:
        # sum_i [ (2 * d_i - 1) * (final_pos_i - p_i) ]
        #
        # = sum_i [ (2 d_i - 1) final_pos_i ] - sum_i [ (2 d_i - 1) p_i ]
        #
        # sum_i [ (2 d_i - 1) p_i ] is fixed, so we want to maximize
        # sum_i [ (2 d_i - 1) final_pos_i ]
        #
        # So final positions should maximize weighted sum with weights w_i=(2 d_i - 1)
        #
        # Because final positions are assigned distinct integers,
        # sorting w_i in descending order and assigning positions increasing or decreasing accordingly maximize sum
        #
        # We'll pair (weight, piece index), sort by weight descending
        # assign final positions in descending order for positive weights, ascending order for negative
        #
        # Since positions must be distinct and in 1..L,
        # the best is to assign final positions in the order of 1..L
        #
        # Because N <= L and positions must be distinct,
        # we assign final positions to piece with highest positive weight to highest position,
        # then decreasing weights to decreasing positions.
        #
        # Implementation detail:
        #   - Sort by weight descending
        #   - Assign final position from L down to L - N +1 in that order
        #
        # Compute score from that assignment.

        N = len(pieces)
        weights = [(2 * d -1, i) for i, d in enumerate(directions)]
        weights.sort(reverse=True, key=lambda x: x[0])

        assigned_positions = [0]*N
        # Assign final positions starting from highest L downwards
        position_cursor = board.length
        for w, i in weights:
            assigned_positions[i] = position_cursor
            position_cursor -= 1

        score = 0
        for i in range(N):
            w = 2 * directions[i] - 1
            score += w * (assigned_positions[i] - positions[i])

        return score

class SolutionFramework:
    def __init__(self, scorer: ScorerStrategy):
        self.scorer = scorer

    def run(self, N: int, L: int, piece_data: list) -> int:
        pieces = [Piece(pos, dir) for pos, dir in piece_data]
        board = Board(L, pieces)
        return self.scorer.calculate_score(board)

def parse_input():
    import sys
    input_iter = iter(sys.stdin.read().strip().split())
    N = int(next(input_iter))
    L = int(next(input_iter))
    piece_data = []
    for _ in range(N):
        p = int(next(input_iter))
        d = int(next(input_iter))
        piece_data.append((p,d))
    return N, L, piece_data

def main():
    N, L, piece_data = parse_input()
    solver = SolutionFramework(MaxScoreCalculator())
    print(solver.run(N,L,piece_data))

if __name__ == "__main__":
    main()