from typing import List, Tuple, Optional, Union, Iterator
from enum import Enum, auto


class Direction(Enum):
    NORTH = auto()
    EAST = auto()
    SOUTH = auto()
    WEST = auto()

    def turn_left(self) -> "Direction":
        order = [Direction.NORTH, Direction.WEST, Direction.SOUTH, Direction.EAST]
        return order[(order.index(self) + 1) % 4]

    def turn_right(self) -> "Direction":
        order = [Direction.NORTH, Direction.EAST, Direction.SOUTH, Direction.WEST]
        return order[(order.index(self) + 1) % 4]

    def vector(self) -> Tuple[int, int]:
        return {
            Direction.NORTH: (-1, 0),
            Direction.EAST: (0, 1),
            Direction.SOUTH: (1, 0),
            Direction.WEST: (0, -1),
        }[self]


class Cell(Enum):
    WALL = '#'
    EMPTY = '.'
    START = 's'
    GOAL = 'g'


class ConditionType(Enum):
    NORTH = 'N'
    EAST = 'E'
    SOUTH = 'S'
    WEST = 'W'
    FRONT_IS_WALL = 'C'
    TRUE = 'T'


class Condition:
    negated: bool
    cond_type: ConditionType

    def __init__(self, raw_cond: str):
        if raw_cond.startswith('~'):
            self.negated = True
            self.cond_type = ConditionType(raw_cond[1])
        else:
            self.negated = False
            self.cond_type = ConditionType(raw_cond[0])

    def evaluate(self, state: "RobotState") -> bool:
        base_value = self._evaluate_base(state)
        return not base_value if self.negated else base_value

    def _evaluate_base(self, state: "RobotState") -> bool:
        if self.cond_type == ConditionType.NORTH:
            return state.direction == Direction.NORTH
        if self.cond_type == ConditionType.EAST:
            return state.direction == Direction.EAST
        if self.cond_type == ConditionType.SOUTH:
            return state.direction == Direction.SOUTH
        if self.cond_type == ConditionType.WEST:
            return state.direction == Direction.WEST
        if self.cond_type == ConditionType.FRONT_IS_WALL:
            dr, dc = state.direction.vector()
            nr, nc = state.row + dr, state.col + dc
            if not (0 <= nr < state.board.height and 0 <= nc < state.board.width):
                return True
            return state.board.is_wall(nr, nc)
        if self.cond_type == ConditionType.TRUE:
            return True
        raise RuntimeError("Unreachable condition type")

    def __str__(self) -> str:
        return ('~' if self.negated else '') + self.cond_type.value


class ProgramNode:
    def execute(self, env: "ExecutionEnvironment") -> Optional[bool]:
        """
        Execute node, returning True if execution should continue,
        False if execution should terminate early (goal reached).
        """
        raise NotImplementedError


class ActionNode(ProgramNode):
    action: str  # one of '^', 'v', '<', '>'

    def __init__(self, action: str):
        self.action = action

    def execute(self, env: "ExecutionEnvironment") -> Optional[bool]:
        env.increment_action_counter()
        state = env.state
        if self.action == '^':
            # move forward
            dr, dc = state.direction.vector()
            nr, nc = state.row + dr, state.col + dc
            if not env.board.is_wall(nr, nc):
                state.row, state.col = nr, nc
                if env.board.is_goal(nr, nc):
                    env.goal_reached = True
                    return False  # stop execution
        elif self.action == 'v':
            # move backward
            dr, dc = state.direction.vector()
            nr, nc = state.row - dr, state.col - dc
            if not env.board.is_wall(nr, nc):
                state.row, state.col = nr, nc
                if env.board.is_goal(nr, nc):
                    env.goal_reached = True
                    return False
        elif self.action == '<':
            state.direction = state.direction.turn_left()
        elif self.action == '>':
            state.direction = state.direction.turn_right()
        else:
            raise RuntimeError(f"Unknown action {self.action}")
        return True


class IfNode(ProgramNode):
    condition: Condition
    program: List[ProgramNode]

    def __init__(self, condition: Condition, program: List[ProgramNode]):
        self.condition = condition
        self.program = program

    def execute(self, env: "ExecutionEnvironment") -> Optional[bool]:
        if self.condition.evaluate(env.state):
            for node in self.program:
                cont = node.execute(env)
                if cont is False:
                    return False
        return True


class WhileNode(ProgramNode):
    condition: Condition
    program: List[ProgramNode]

    def __init__(self, condition: Condition, program: List[ProgramNode]):
        self.condition = condition
        self.program = program

    def execute(self, env: "ExecutionEnvironment") -> Optional[bool]:
        while self.condition.evaluate(env.state):
            for node in self.program:
                cont = node.execute(env)
                if cont is False:
                    return False
        return True


class Parser:
    program: str
    pos: int
    length: int

    def __init__(self, program: str):
        self.program = program
        self.pos = 0
        self.length = len(program)

    def parse_program(self) -> List[ProgramNode]:
        nodes = []
        while self.pos < self.length:
            node = self.parse_statement()
            if node is None:
                break
            nodes.append(node)
        return nodes

    def peek(self) -> Optional[str]:
        if self.pos < self.length:
            return self.program[self.pos]
        return None

    def consume(self, ch: str) -> bool:
        if self.peek() == ch:
            self.pos += 1
            return True
        return False

    def expect(self, ch: str):
        if not self.consume(ch):
            raise RuntimeError(f"Expected '{ch}' at pos {self.pos}")

    def parse_statement(self) -> Optional[ProgramNode]:
        c = self.peek()
        if c is None:
            return None
        if c == '[':
            return self.parse_if()
        if c == '{':
            return self.parse_while()
        if c in "^v<>":
            self.pos += 1
            return ActionNode(c)
        # Invalid char at statement start
        return None

    def parse_if(self) -> IfNode:
        self.expect('[')
        cond = self.parse_condition()
        body = self.parse_program_until(']')
        self.expect(']')
        return IfNode(cond, body)

    def parse_while(self) -> WhileNode:
        self.expect('{')
        cond = self.parse_condition()
        body = self.parse_program_until('}')
        self.expect('}')
        return WhileNode(cond, body)

    def parse_condition(self) -> Condition:
        start = self.pos
        # condition is optional ~ plus one char from N E S W C T
        if self.peek() == '~':
            self.pos += 1
        c = self.peek()
        if c not in {'N','E','S','W','C','T'}:
            raise RuntimeError(f"Invalid condition char '{c}' at pos {self.pos}")
        self.pos += 1
        return Condition(self.program[start:self.pos])

    def parse_program_until(self, terminator: str) -> List[ProgramNode]:
        nodes = []
        while True:
            c = self.peek()
            if c is None:
                raise RuntimeError(f"Unexpected end of input while looking for {terminator}")
            if c == terminator:
                break
            node = self.parse_statement()
            if node is None:
                raise RuntimeError(f"Invalid statement before {terminator} at pos {self.pos}")
            nodes.append(node)
        return nodes


class Board:
    height: int
    width: int
    cells: List[List[Cell]]
    goal_pos: Tuple[int, int]
    start_pos: Tuple[int, int]

    def __init__(self, H: int, W: int, lines: List[str]):
        self.height = H
        self.width = W
        self.cells = [[Cell(line[j]) for j in range(W)] for line in lines]
        self.start_pos = (-1, -1)
        self.goal_pos = (-1, -1)
        for i in range(H):
            for j in range(W):
                if self.cells[i][j] == Cell.START:
                    self.start_pos = (i, j)
                elif self.cells[i][j] == Cell.GOAL:
                    self.goal_pos = (i, j)
        if self.start_pos == (-1, -1):
            raise RuntimeError("No start position found")
        if self.goal_pos == (-1, -1):
            raise RuntimeError("No goal position found")

    def is_wall(self, r: int, c: int) -> bool:
        return self.cells[r][c] == Cell.WALL

    def is_goal(self, r: int, c: int) -> bool:
        return (r, c) == self.goal_pos


class RobotState:
    row: int
    col: int
    direction: Direction
    board: Board

    def __init__(self, row: int, col: int, board: Board):
        self.row = row
        self.col = col
        self.direction = Direction.NORTH
        self.board = board


class ExecutionEnvironment:
    state: RobotState
    board: Board
    action_count: int
    goal_reached: bool

    def __init__(self, state: RobotState, board: Board):
        self.state = state
        self.board = board
        self.action_count = 0
        self.goal_reached = False

    def increment_action_counter(self):
        self.action_count += 1


class RobotSimulator:
    board: Board
    program: List[ProgramNode]
    env: ExecutionEnvironment

    def __init__(self, board: Board, program: List[ProgramNode]):
        self.board = board
        self.env = ExecutionEnvironment(
            RobotState(board.start_pos[0], board.start_pos[1], board),
            board,
        )
        self.program = program

    def run(self) -> int:
        # Program executes sequentially until goal reached or end
        cont = True
        for node in self.program:
            cont = node.execute(self.env)
            if cont is False:  # goal reached
                break
        else:
            # If not reached goal after all statements once, robot halts naturally
            # But problem condition: robot stops when goal reached, else all run out means unreachable
            if self.env.goal_reached:
                return self.env.action_count
            else:
                return -1

        # If loop ended early due to goal reached
        return self.env.action_count


def main() -> None:
    import sys
    input = sys.stdin.readline
    H, W = map(int, input().split())
    lines = [input().rstrip('\n') for _ in range(H)]
    program_str = input().rstrip('\n')

    board = Board(H, W, lines)
    parser = Parser(program_str)
    program = parser.parse_program()

    simulator = RobotSimulator(board, program)
    result = simulator.run()
    print(result)


if __name__ == "__main__":
    main()