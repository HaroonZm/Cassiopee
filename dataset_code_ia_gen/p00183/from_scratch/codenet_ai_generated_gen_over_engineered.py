from abc import ABC, abstractmethod
from typing import List, Optional


class Stone:
    BLACK = 'b'
    WHITE = 'w'
    EMPTY = '+'


class Board:
    SIZE = 3

    def __init__(self, rows: List[str]) -> None:
        if len(rows) != self.SIZE or any(len(row) != self.SIZE for row in rows):
            raise ValueError("Board rows must be 3 strings of length 3.")
        self.grid: List[List[str]] = [list(row) for row in rows]

    def get_cell(self, row: int, col: int) -> str:
        return self.grid[row][col]

    def lines(self) -> List[List[str]]:
        # Returns all lines to check: rows, columns, diagonals
        lines = []
        # Rows
        for r in range(self.SIZE):
            lines.append([self.grid[r][c] for c in range(self.SIZE)])
        # Columns
        for c in range(self.SIZE):
            lines.append([self.grid[r][c] for r in range(self.SIZE)])
        # Diagonals
        lines.append([self.grid[i][i] for i in range(self.SIZE)])
        lines.append([self.grid[i][self.SIZE - 1 - i] for i in range(self.SIZE)])
        return lines


class WinConditionChecker(ABC):
    @abstractmethod
    def check(self, board: Board) -> Optional[str]:
        pass


class TicTacToeWinnerChecker(WinConditionChecker):
    def __init__(self, stone_to_check: str) -> None:
        self.stone = stone_to_check

    def check(self, board: Board) -> Optional[str]:
        # Check if this stone has a winning line
        for line in board.lines():
            if all(cell == self.stone for cell in line):
                return self.stone
        return None


class GameResultResolver:
    def __init__(self, board: Board) -> None:
        self.board = board
        self.checkers = [
            TicTacToeWinnerChecker(Stone.BLACK),
            TicTacToeWinnerChecker(Stone.WHITE),
        ]

    def resolve_winner(self) -> str:
        winner = None
        for checker in self.checkers:
            res = checker.check(self.board)
            if res:
                if winner is not None:
                    # According to the problem statement, cannot both win simultaneously.
                    raise RuntimeError("Invalid board: multiple winners detected.")
                winner = res
        if winner is None:
            return "NA"
        return winner


class InputProcessor:
    def __init__(self) -> None:
        self.datasets: List[Board] = []

    def read_boards(self) -> None:
        while True:
            rows = []
            for _ in range(Board.SIZE):
                line = input()
                if line == '0' and len(rows) == 0:
                    return
                rows.append(line)
            # Validate and add the board
            self.datasets.append(Board(rows))


class OutputProcessor:
    @staticmethod
    def print_results(results: List[str]) -> None:
        for result in results:
            print(result)


def main() -> None:
    input_processor = InputProcessor()
    input_processor.read_boards()

    results: List[str] = []
    for board in input_processor.datasets:
        resolver = GameResultResolver(board)
        results.append(resolver.resolve_winner())

    OutputProcessor.print_results(results)


if __name__ == "__main__":
    main()