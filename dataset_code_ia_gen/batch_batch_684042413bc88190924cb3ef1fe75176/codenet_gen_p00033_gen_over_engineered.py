class Ball:
    def __init__(self, number: int):
        self.number = number

    def __lt__(self, other: 'Ball') -> bool:
        return self.number < other.number

    def __repr__(self) -> str:
        return f"Ball({self.number})"


class Tube:
    def __init__(self, name: str):
        self.name = name
        self.stack: list[Ball] = []

    def can_place(self, ball: Ball) -> bool:
        # A ball can be placed if the stack is empty or the top ball number is greater than the new ball
        if not self.stack:
            return True
        return self.stack[-1] > ball

    def place(self, ball: Ball):
        if not self.can_place(ball):
            raise ValueError(f"Cannot place {ball} on tube {self.name} due to ordering constraints.")
        self.stack.append(ball)

    def __repr__(self) -> str:
        return f"Tube({self.name}, stack={self.stack})"


class Board:
    def __init__(self):
        # Although in the problem the board rotates left or right (to put balls in either tube B or C),
        # we model this as an abstraction layer for future extensibility.
        self.left_tube = Tube('B')
        self.right_tube = Tube('C')

    def drop_ball(self, ball: Ball) -> bool:
        """
        Decide which tube to put the ball in.
        Returns True if placed successfully, False otherwise.

        The heuristic tries to place in left tube first, if possible, else right tube.
        """
        if self.left_tube.can_place(ball):
            self.left_tube.place(ball)
            return True
        elif self.right_tube.can_place(ball):
            self.right_tube.place(ball)
            return True
        else:
            return False

    def reset(self):
        self.left_tube = Tube('B')
        self.right_tube = Tube('C')


class BallContainerSimulator:
    def __init__(self):
        self.board = Board()

    def simulate(self, balls: list[int]) -> str:
        self.board.reset()
        ball_objects = [Ball(num) for num in balls]

        for ball in ball_objects:
            if not self.board.drop_ball(ball):
                return "NO"
        return "YES"


class InputParser:
    def __init__(self, input_lines: list[str]):
        self.lines = input_lines
        self.index = 0

    def next_line(self) -> str:
        if self.index >= len(self.lines):
            raise StopIteration
        line = self.lines[self.index].strip()
        self.index += 1
        return line

    def parse(self) -> tuple[int, list[list[int]]]:
        n = int(self.next_line())
        data_sets = []
        for _ in range(n):
            data = list(map(int, self.next_line().split()))
            data_sets.append(data)
        return n, data_sets


def main():
    import sys
    parser = InputParser(sys.stdin.read().strip().split('\n'))
    n, data_sets = parser.parse()

    simulator = BallContainerSimulator()
    for data_set in data_sets:
        print(simulator.simulate(data_set))


if __name__ == "__main__":
    main()