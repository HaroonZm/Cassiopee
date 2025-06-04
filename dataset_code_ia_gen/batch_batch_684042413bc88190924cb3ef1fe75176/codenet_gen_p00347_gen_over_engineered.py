class Position:
    def __init__(self, row: int, col: int):
        self.row = row
        self.col = col

    def __eq__(self, other):
        return self.row == other.row and self.col == other.col

    def __hash__(self):
        return hash((self.row, self.col))

    def is_at(self, max_row: int, max_col: int) -> bool:
        return self.row == max_row and self.col == max_col

    def neighbors(self, max_row: int, max_col: int) -> tuple:
        moves = []
        if self.row < max_row:
            moves.append(Position(self.row + 1, self.col))
        if self.col < max_col:
            moves.append(Position(self.row, self.col + 1))
        return tuple(moves)

class Island:
    def __init__(self, width: int, height: int, grid: list):
        self.width = width
        self.height = height
        self.grid = grid  # 2D list [row][col]

    def territory_score(self, from_pos: Position, to_pos: Position, include_start: bool, include_end: bool) -> int:
        # Compute score inside the rectangle (from_pos) NE to (to_pos) SW
        # Territory is separated by the path boundary:
        # Up-right = first player, down-left = second player.
        # This method allows calculating sums for arbitrary rectangular regions.
        r_start = from_pos.row
        r_end = to_pos.row
        c_start = from_pos.col
        c_end = to_pos.col
        result = 0
        for r in range(r_start, r_end):
            for c in range(c_start, c_end):
                result += self.grid[r][c]
        return result

class MoveStrategyBase:
    def choose_move(self, position: Position, island: Island, dp_cache: dict, max_row: int, max_col: int) -> tuple:
        raise NotImplementedError

class OptimalMoveStrategy(MoveStrategyBase):
    def choose_move(self, position: Position, island: Island, dp_cache: dict, max_row: int, max_col: int) -> tuple:
        # Return tuple(score, next_position) maximized from current position
        # Memoization used for efficiency.
        if position.is_at(max_row, max_col):
            return 0, None

        if position in dp_cache:
            return dp_cache[position]

        candidates = []
        for next_pos in position.neighbors(max_row, max_col):
            score_next, _ = self.choose_move(next_pos, island, dp_cache, max_row, max_col)

            # The path splits the island into two areas:
            # north-east is first player's territory, south-west is second player's territory.
            # We want to maximize difference (first - second) in optimal play.
            # The clever approach is to use minimax with difference tracking.

            candidates.append(score_next)

        if not candidates:
            dp_cache[position] = (0, None)
            return 0, None

        # Turn-based: first player's turn increases difference, second reduces.
        # We alternate turns by parity of steps from start.
        steps_done = position.row + position.col
        is_first_player_turn = (steps_done % 2 == 0)

        if is_first_player_turn:
            max_score = max(candidates)
            best_pos_idx = candidates.index(max_score)
        else:
            max_score = min(candidates)
            best_pos_idx = candidates.index(max_score)

        next_position = position.neighbors(max_row, max_col)[best_pos_idx]
        dp_cache[position] = (max_score, next_position)
        return dp_cache[position]

class GameSimulator:
    def __init__(self, island: Island, strategy: MoveStrategyBase):
        self.island = island
        self.strategy = strategy
        self.dp_cache = {}

    def play(self) -> int:
        # We'll use Dynamic Programming with minimax style:
        # dp[r][c] = best difference starting from (r,c)
        # difference = first_player_score - second_player_score

        max_row = self.island.height
        max_col = self.island.width
        dp = [[None]*(max_col+1) for _ in range(max_row+1)]

        # We preprocess sums for quicker territory score calculation
        prefix_sum = [[0]*(max_col+1) for _ in range(max_row+1)]
        for r in range(1, max_row+1):
            for c in range(1, max_col+1):
                prefix_sum[r][c] = (self.island.grid[r-1][c-1] +
                                    prefix_sum[r-1][c] + prefix_sum[r][c-1] - prefix_sum[r-1][c-1])

        def sum_region(r1, c1, r2, c2):
            return prefix_sum[r2][c2] - prefix_sum[r1][c2] - prefix_sum[r2][c1] + prefix_sum[r1][c1]

        def rec(r, c):
            if r == max_row and c == max_col:
                return 0
            if dp[r][c] is not None:
                return dp[r][c]

            next_positions = []
            if r < max_row:
                next_positions.append((r+1, c))
            if c < max_col:
                next_positions.append((r, c+1))

            step = r + c
            is_first_turn = (step % 2 == 0)
            results = []
            for nr, nc in next_positions:
                val = rec(nr, nc)
                results.append(val)

            if is_first_turn:
                result = max(results)
            else:
                result = min(results)
            dp[r][c] = result
            return result

        # The key is that the difference dp returns is exactly the difference between first and second player scores
        # according to the optimal moves.

        # We use a bottom-up build of difference:
        # Actually, we need to incorporate the score difference when moving.

        from functools import lru_cache

        @lru_cache(maxsize=None)
        def dfs(r, c):
            if r == max_row and c == max_col:
                return 0
            moves = []
            if r < max_row:
                moves.append((r+1, c))
            if c < max_col:
                moves.append((r, c+1))
            step = r + c
            first_player_turn = (step % 2 == 0)
            scores = []
            for nr, nc in moves:
                # The area owned by the players changes with the path
                # The difference is incremented by the score at the cell we cross?
                # No: The difference is cumulative and depends on the path boundary

                # We consider the incremental score:
                # When we move horizontally (r,nc), the column changes, when vertically (nr,c), the row changes.
                # One way: we can compute the difference in territory by summing or subtracting the s[r][c] cell in order.

                # From problem example and explanation we can do:
                # The incremental gain in difference equals s[min(nr,r)][min(nc,c)]
                # Because moving to new cell decides which side it belongs to.

                # But this is complicated, so instead we can convert the problem to minimax over difference dp.

                delta = 0
                if first_player_turn:
                    # Add the cell's score
                    # The boundary moves. Concretely, the cell at (r,c) on the rectangle boundary belongs to which player?

                    # After thinking, the proper method is manual solution below
                    pass

                val = dfs(nr, nc)
                scores.append(val)

            best_val = max(scores) if first_player_turn else min(scores)
            return best_val

        # Because above not trivial, we implement classical DP adapted from editorial:

        # Prepare partial sums for second player (lower left rectangle) scores:
        # Not used here directly, but for clarity.

        # Implement bottom up dp for score difference:
        diff = [[0]*(max_col+1) for _ in range(max_row+1)]

        for r in range(max_row, -1, -1):
            for c in range(max_col, -1, -1):
                if r == max_row and c == max_col:
                    diff[r][c] = 0
                    continue
                step = r + c
                is_first_player_turn = (step % 2 == 0)
                candidates = []
                if r < max_row:
                    gain = self.island.grid[r][c]  # cell at moving down owned by first player next turn
                    val = diff[r+1][c] + (gain if is_first_player_turn else -gain)
                    candidates.append(val)
                if c < max_col:
                    gain = self.island.grid[r][c]
                    val = diff[r][c+1] + (gain if is_first_player_turn else -gain)
                    candidates.append(val)
                if is_first_player_turn:
                    diff[r][c] = max(candidates)
                else:
                    diff[r][c] = min(candidates)

        # diff[0][0] is the difference (first - second) with both playing optimally.
        return abs(diff[0][0])

def main():
    import sys
    input = sys.stdin.readline
    W, H = map(int, input().split())
    grid = [list(map(int, input().split())) for _ in range(H)]
    island = Island(W, H, grid)
    game = GameSimulator(island, OptimalMoveStrategy())
    result = game.play()
    print(result)

if __name__ == "__main__":
    main()