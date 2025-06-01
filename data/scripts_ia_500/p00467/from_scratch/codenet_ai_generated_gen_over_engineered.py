class SugorokuBoard:
    def __init__(self, instructions):
        self.instructions = instructions
        self.size = len(instructions)

    def apply_instruction(self, position):
        # position is 1-based
        move = self.instructions[position - 1]
        new_pos = position + move
        if new_pos < 1:
            new_pos = 1  # per problem statement, no instruction sends before 1
        return new_pos


class DiceRolls:
    def __init__(self, rolls):
        self.rolls = rolls
        self.index = 0

    def next_roll(self):
        if self.index < len(self.rolls):
            val = self.rolls[self.index]
            self.index += 1
            return val
        else:
            raise IndexError("No more dice rolls available.")


class SugorokuGame:
    def __init__(self, board, dice):
        self.board = board
        self.dice = dice
        self.position = 1
        self.turns = 0

    def play_to_goal(self):
        while True:
            roll = self.dice.next_roll()
            self.turns += 1
            next_pos = self.position + roll
            if next_pos >= self.board.size:
                # Reached or exceeded goal position
                return self.turns
            # Move to next_pos and apply instruction
            next_pos = self.board.apply_instruction(next_pos)
            self.position = next_pos


class SugorokuParser:
    def __init__(self):
        self.datasets = []

    def parse(self):
        while True:
            line = input().strip()
            if not line:
                continue
            N, M = map(int, line.split())
            if N == 0 and M == 0:
                break
            instructions = []
            for _ in range(N):
                instructions.append(int(input().strip()))
            rolls = []
            for _ in range(M):
                rolls.append(int(input().strip()))
            self.datasets.append((N, M, instructions, rolls))


class SugorokuSolver:
    def __init__(self, datasets):
        self.datasets = datasets

    def solve_all(self):
        results = []
        for N, M, instructions, rolls in self.datasets:
            board = SugorokuBoard(instructions)
            dice = DiceRolls(rolls)
            game = SugorokuGame(board, dice)
            result = game.play_to_goal()
            results.append(result)
        return results


def main():
    parser = SugorokuParser()
    parser.parse()
    solver = SugorokuSolver(parser.datasets)
    results = solver.solve_all()
    for res in results:
        print(res)


if __name__ == "__main__":
    main()