class SugorokuBoard:
    def __init__(self, cells):
        self.cells = cells
        self.size = len(cells)

    def move(self, position, steps):
        next_pos = position + steps
        if next_pos >= self.size:
            # Reached or passed goal
            return self.size
        # Follow the cell's instruction once
        instruction = self.cells[next_pos]
        moved_pos = next_pos + instruction
        if moved_pos < 0:
            moved_pos = 0  # safeguard but as per problem won't happen
        return moved_pos


class Dice:
    def __init__(self, throws):
        self.throws = throws
        self.index = 0

    def next_throw(self):
        if self.index >= len(self.throws):
            raise IndexError("No more dice throws available")
        val = self.throws[self.index]
        self.index += 1
        return val


class SugorokuGame:
    def __init__(self, board: SugorokuBoard, dice: Dice):
        self.board = board
        self.dice = dice
        self.position = 0  # 0-based index for first cell

    def play_until_goal(self):
        rolls_count = 0
        while self.position < self.board.size - 1:
            roll = self.dice.next_throw()
            rolls_count += 1
            self.position = self.board.move(self.position, roll)
        return rolls_count


class SugorokuFactory:
    @staticmethod
    def create_game(n, m, cells, dice_throws):
        # cells come 0-based but problem is 1-based; just use 0-based internally
        # Validate first cell instruction is zero as per problem statement
        if cells[0] != 0:
            raise ValueError("Start cell instruction must be 0")
        # Validate dice_throws length and first dice throw == 0 as per input format
        if dice_throws[0] != 0:
            raise ValueError("First dice throw must be 0")
        board = SugorokuBoard(cells)
        dice = Dice(dice_throws)
        return SugorokuGame(board, dice)


class SugorokuInputParser:
    def __init__(self):
        self.datasets = []

    def parse_all(self):
        import sys
        lines = sys.stdin.read().strip().split('\n')
        idx = 0
        while idx < len(lines):
            if lines[idx].strip() == '':
                idx += 1
                continue
            n, m = map(int, lines[idx].split())
            idx += 1
            if n == 0 and m == 0:
                break
            cells = []
            for _ in range(n):
                cells.append(int(lines[idx]))
                idx += 1
            dice_throws = []
            for _ in range(m):
                dice_throws.append(int(lines[idx]))
                idx += 1
            self.datasets.append((n, m, cells, dice_throws))


class SugorokuSolver:
    def __init__(self):
        self.parser = SugorokuInputParser()

    def solve(self):
        self.parser.parse_all()
        results = []
        for n, m, cells, dice_throws in self.parser.datasets:
            game = SugorokuFactory.create_game(n, m, cells, dice_throws)
            rolls = game.play_until_goal()
            results.append(str(rolls))
        print('\n'.join(results))


if __name__ == "__main__":
    solver = SugorokuSolver()
    solver.solve()