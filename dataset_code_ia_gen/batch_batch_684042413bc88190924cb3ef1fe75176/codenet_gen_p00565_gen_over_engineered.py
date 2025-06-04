class BoardPosition:
    def __init__(self, index: int, is_blocked: bool):
        self.index = index
        self.is_blocked = is_blocked

    def __repr__(self):
        return f"BoardPosition(index={self.index}, blocked={self.is_blocked})"


class SugorokuBoard:
    def __init__(self, positions):
        self.positions = positions
        self.start_index = 0
        self.goal_index = len(positions) - 1

    def is_safe_position(self, index: int) -> bool:
        if index > self.goal_index:
            return True
        return not self.positions[index].is_blocked


class Dice:
    def __init__(self, sides: int):
        self.sides = sides
        self.faces = list(range(1, sides + 1))

    def __repr__(self):
        return f"Dice(sides={self.sides})"


class GameSimulator:
    def __init__(self, board: SugorokuBoard):
        self.board = board

    def can_clear_with_dice(self, dice: Dice) -> bool:
        # Dynamic programming: dp[i] = True if position i is reachable safely
        dp = [False] * len(self.board.positions)
        dp[self.board.start_index] = True

        for pos in range(self.board.start_index + 1, len(self.board.positions)):
            for face in dice.faces:
                prev_pos = pos - face
                if prev_pos < 0:
                    continue
                if dp[prev_pos] and self.board.is_safe_position(pos):
                    dp[pos] = True
                    break

        # Game clear if position >= goal_index is reachable
        return any(dp[self.board.goal_index:])

class SugorokuSolver:
    def __init__(self, cell_values):
        self.board = self._build_board(cell_values)
        self.max_dice_sides = len(self.board.positions) - 1 # N+1 dice max sides

    def _build_board(self, cell_values):
        # Positions: 0 start, 1 to N cells, N+1 goal
        positions = [BoardPosition(0, False)]
        for idx, val in enumerate(cell_values, 1):
            positions.append(BoardPosition(idx, val == 1))
        positions.append(BoardPosition(len(cell_values) + 1, False))
        return SugorokuBoard(positions)

    def solve(self) -> int:
        # Search for minimal dice sides from 1 to max_dice_sides
        for sides in range(1, self.max_dice_sides + 1):
            dice = Dice(sides)
            simulator = GameSimulator(self.board)
            if simulator.can_clear_with_dice(dice):
                return sides
        # If none found (should not occur), return max sides
        return self.max_dice_sides


def main():
    import sys
    input = sys.stdin.readline
    N = int(input())
    cell_values = list(map(int, input().split()))
    solver = SugorokuSolver(cell_values)
    print(solver.solve())

if __name__ == "__main__":
    main()