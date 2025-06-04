from abc import ABC, abstractmethod
from typing import List, Optional, Iterator

class PlayerSymbol(str):
    O = 'o'
    X = 'x'
    S = 's'  # space/empty

class GameResult(str):
    O_WIN = 'o'
    X_WIN = 'x'
    DRAW = 'd'

class Board:
    SIZE = 3

    def __init__(self, cells: List[List[PlayerSymbol]]):
        if len(cells) != self.SIZE or any(len(row) != self.SIZE for row in cells):
            raise ValueError("Board must be 3x3.")
        self._cells = cells

    @classmethod
    def from_string(cls, s: str) -> 'Board':
        if len(s) != cls.SIZE * cls.SIZE:
            raise ValueError(f"Input string length must be {cls.SIZE * cls.SIZE}.")
        cells: List[List[PlayerSymbol]] = []
        for r in range(cls.SIZE):
            row = list(s[r*cls.SIZE:(r+1)*cls.SIZE])
            # Validate characters
            for c in row:
                if c not in (PlayerSymbol.O, PlayerSymbol.X, PlayerSymbol.S):
                    raise ValueError(f"Invalid cell character '{c}' found.")
            cells.append(row)
        return cls(cells)

    def get_cell(self, row: int, col: int) -> PlayerSymbol:
        return self._cells[row][col]

    def lines(self) -> Iterator[List[PlayerSymbol]]:
        # Rows
        for r in range(self.SIZE):
            yield [self._cells[r][c] for c in range(self.SIZE)]
        # Columns
        for c in range(self.SIZE):
            yield [self._cells[r][c] for r in range(self.SIZE)]
        # Diagonals
        yield [self._cells[i][i] for i in range(self.SIZE)]
        yield [self._cells[i][self.SIZE - 1 - i] for i in range(self.SIZE)]

class WinConditionChecker(ABC):
    @abstractmethod
    def check(self, board: Board) -> Optional[GameResult]:
        pass

class ThreeInLineChecker(WinConditionChecker):
    def __init__(self, symbol: PlayerSymbol):
        self._symbol = symbol

    def check(self, board: Board) -> Optional[GameResult]:
        for line in board.lines():
            if all(cell == self._symbol for cell in line):
                if self._symbol == PlayerSymbol.O:
                    return GameResult.O_WIN
                elif self._symbol == PlayerSymbol.X:
                    return GameResult.X_WIN
        return None

class GameEvaluator:
    def __init__(self, checkers: List[WinConditionChecker]):
        self._checkers = checkers

    def evaluate(self, board: Board) -> GameResult:
        for checker in self._checkers:
            result = checker.check(board)
            if result is not None:
                return result
        return GameResult.DRAW

class InputLoader:
    def __init__(self, max_datasets:int = 50):
        self._max_datasets = max_datasets

    def load_boards(self) -> Iterator[Board]:
        count = 0
        while count < self._max_datasets:
            try:
                line = input()
            except EOFError:
                break
            line = line.strip()
            if not line:
                continue
            yield Board.from_string(line)
            count += 1

class TicTacToeApplication:
    def __init__(self):
        self._board_loader = InputLoader()
        self._evaluator = GameEvaluator([
            ThreeInLineChecker(PlayerSymbol.O),
            ThreeInLineChecker(PlayerSymbol.X)
        ])

    def run(self) -> None:
        for board in self._board_loader.load_boards():
            result = self._evaluator.evaluate(board)
            print(result)

if __name__ == '__main__':
    app = TicTacToeApplication()
    app.run()