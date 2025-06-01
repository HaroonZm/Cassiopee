class Player:
    O = 'o'
    X = 'x'
    Draw = 'd'
    Empty = 's'

class Cell:
    def __init__(self, symbol: str):
        if symbol not in (Player.O, Player.X, Player.Empty):
            raise ValueError(f"Invalid cell symbol: {symbol}")
        self.symbol = symbol

    def is_empty(self) -> bool:
        return self.symbol == Player.Empty

    def __eq__(self, other):
        if not isinstance(other, Cell):
            return False
        return self.symbol == other.symbol

    def __repr__(self):
        return f"Cell('{self.symbol}')"

class Board:
    def __init__(self, cells: list):
        if len(cells) != 9:
            raise ValueError("Board must have exactly 9 cells")
        self.cells = cells  # list of Cell objects

    @classmethod
    def from_string(cls, s: str):
        if len(s) != 9:
            raise ValueError("Input string must be length 9")
        return cls([Cell(ch) for ch in s])

    def _winning_lines(self):
        # Indices of winning lines (rows, columns, diagonals)
        return [
            (0,1,2), (3,4,5), (6,7,8),    # rows
            (0,3,6), (1,4,7), (2,5,8),    # columns
            (0,4,8), (2,4,6)              # diagonals
        ]

    def winner(self) -> str:
        # returns Player.O if O wins, Player.X if X wins, Player.Draw otherwise
        for line in self._winning_lines():
            line_cells = [self.cells[i].symbol for i in line]
            if line_cells[0] != Player.Empty and line_cells[0] == line_cells[1] == line_cells[2]:
                return line_cells[0]
        return Player.Draw

    def __repr__(self):
        rows = [''.join(cell.symbol for cell in self.cells[i*3:(i+1)*3]) for i in range(3)]
        return "\n".join(rows)

class GameController:
    def __init__(self):
        self.boards = []

    def parse_input(self, lines: list):
        for line in lines:
            line = line.strip()
            if line:
                board = Board.from_string(line)
                self.boards.append(board)

    def evaluate_all(self) -> list:
        results = []
        for board in self.boards:
            result = board.winner()
            results.append(result)
        return results

class TicTacToeApp:
    def __init__(self):
        self.controller = GameController()

    def run(self):
        import sys
        input_lines = sys.stdin.read().strip().splitlines()
        self.controller.parse_input(input_lines)
        results = self.controller.evaluate_all()
        for res in results:
            print(res)

if __name__ == "__main__":
    TicTacToeApp().run()