from typing import List, Tuple, Dict, Set
from collections import deque
import sys

# Abstract Point class to encapsulate coordinate operations
class Point:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

    def __eq__(self, other):
        return isinstance(other, Point) and self.x == other.x and self.y == other.y

    def __hash__(self):
        return hash((self.x, self.y))

    def neighbors_4(self) -> List['Point']:
        return [
            Point(self.x+1, self.y),
            Point(self.x-1, self.y),
            Point(self.x, self.y+1),
            Point(self.x, self.y-1)
        ]


# Grid class for representation of the paper and operations on it
class Grid:
    def __init__(self, width: int, height: int):
        self.width = width
        self.height = height
        self.cells = [[False]*width for _ in range(height)]

    def mark_line(self, p1: Point, p2: Point):
        # line is always horizontal or vertical or a point
        if p1.x == p2.x:
            x = p1.x
            y_start = min(p1.y, p2.y)
            y_end = max(p1.y, p2.y)
            for y in range(y_start, y_end+1):
                self.cells[y][x] = True
        elif p1.y == p2.y:
            y = p1.y
            x_start = min(p1.x, p2.x)
            x_end = max(p1.x, p2.x)
            for x in range(x_start, x_end+1):
                self.cells[y][x] = True
        else:
            # According to the spec, this should never happen.
            pass

    def is_marked(self, p: Point) -> bool:
        if 0 <= p.y < self.height and 0 <= p.x < self.width:
            return self.cells[p.y][p.x]
        return False


# Abstract Character class to implement character traits and recognition interface
class Character:
    # character grid patterns to be overridden by subclasses
    pattern: List[str]
    char_repr: str

    # dimensions of pattern
    height: int
    width: int

    def __init__(self, occupied_points: Set[Point]):
        # occupied_points: all points painted for this character on the grid
        self.occupied_points = occupied_points
        self.bounding_box = self.calc_bounding_box()

    def calc_bounding_box(self) -> Tuple[int, int, int, int]:
        # returns (min_x, min_y, max_x, max_y)
        xs = [p.x for p in self.occupied_points]
        ys = [p.y for p in self.occupied_points]
        return min(xs), min(ys), max(xs), max(ys)

    def width(self) -> int:
        min_x, _, max_x, _ = self.bounding_box
        return max_x - min_x + 1

    def height(self) -> int:
        _, min_y, _, max_y = self.bounding_box
        return max_y - min_y + 1

    @staticmethod
    def match_pattern(points: Set[Point], min_x: int, min_y: int, max_x: int, max_y: int,
                      pattern: List[str]) -> bool:
        # pattern is list of strings of '1' or '0'
        # check if points match pattern exactly in bounding box
        ph = len(pattern)
        pw = len(pattern[0])
        if (max_x - min_x + 1) != pw or (max_y - min_y + 1) != ph:
            return False
        for dy in range(ph):
            for dx in range(pw):
                p = Point(min_x + dx, min_y + dy)
                should_be_black = (pattern[dy][dx] == '1')
                actual_black = (p in points)
                if should_be_black != actual_black:
                    return False
        return True


# Concrete character classes for each symbol. Patterns are carefully designed to match described characters.
# Because problem states characters are always drawn as given, no variations.
class Digit0(Character):
    pattern = [
        "111",
        "101",
        "101",
        "101",
        "111"
    ]
    char_repr = '0'

    @classmethod
    def try_match(cls, points: Set[Point]) -> bool:
        if not points:
            return False
        min_x = min(p.x for p in points)
        min_y = min(p.y for p in points)
        max_x = max(p.x for p in points)
        max_y = max(p.y for p in points)
        return cls.match_pattern(points, min_x, min_y, max_x, max_y, cls.pattern)


class Digit1(Character):
    pattern = [
        "010",
        "110",
        "010",
        "010",
        "111"
    ]
    char_repr = '1'

    @classmethod
    def try_match(cls, points: Set[Point]) -> bool:
        if not points:
            return False
        min_x = min(p.x for p in points)
        min_y = min(p.y for p in points)
        max_x = max(p.x for p in points)
        max_y = max(p.y for p in points)
        return cls.match_pattern(points, min_x, min_y, max_x, max_y, cls.pattern)


class Digit2(Character):
    pattern = [
        "111",
        "001",
        "111",
        "100",
        "111"
    ]
    char_repr = '2'

    @classmethod
    def try_match(cls, points: Set[Point]) -> bool:
        if not points:
            return False
        min_x = min(p.x for p in points)
        min_y = min(p.y for p in points)
        max_x = max(p.x for p in points)
        max_y = max(p.y for p in points)
        return cls.match_pattern(points, min_x, min_y, max_x, max_y, cls.pattern)

class Digit3(Character):
    pattern = [
        "111",
        "001",
        "111",
        "001",
        "111"
    ]
    char_repr = '3'

    @classmethod
    def try_match(cls, points: Set[Point]) -> bool:
        if not points:
            return False
        min_x = min(p.x for p in points)
        min_y = min(p.y for p in points)
        max_x = max(p.x for p in points)
        max_y = max(p.y for p in points)
        return cls.match_pattern(points, min_x, min_y, max_x, max_y, cls.pattern)

class Digit4(Character):
    pattern = [
        "101",
        "101",
        "111",
        "001",
        "001"
    ]
    char_repr = '4'

    @classmethod
    def try_match(cls, points: Set[Point]) -> bool:
        if not points:
            return False
        min_x = min(p.x for p in points)
        min_y = min(p.y for p in points)
        max_x = max(p.x for p in points)
        max_y = max(p.y for p in points)
        return cls.match_pattern(points, min_x, min_y, max_x, max_y, cls.pattern)


class Digit5(Character):
    pattern = [
        "111",
        "100",
        "111",
        "001",
        "111"
    ]
    char_repr = '5'

    @classmethod
    def try_match(cls, points: Set[Point]) -> bool:
        if not points:
            return False
        min_x = min(p.x for p in points)
        min_y = min(p.y for p in points)
        max_x = max(p.x for p in points)
        max_y = max(p.y for p in points)
        return cls.match_pattern(points, min_x, min_y, max_x, max_y, cls.pattern)

class Digit6(Character):
    pattern = [
        "111",
        "100",
        "111",
        "101",
        "111"
    ]
    char_repr = '6'
    @classmethod
    def try_match(cls, points: Set[Point]) -> bool:
        if not points:
            return False
        min_x = min(p.x for p in points)
        min_y = min(p.y for p in points)
        max_x = max(p.x for p in points)
        max_y = max(p.y for p in points)
        return cls.match_pattern(points, min_x, min_y, max_x, max_y, cls.pattern)


class Digit7(Character):
    pattern = [
        "111",
        "001",
        "010",
        "100",
        "100"
    ]
    char_repr = '7'
    @classmethod
    def try_match(cls, points: Set[Point]) -> bool:
        if not points:
            return False
        min_x = min(p.x for p in points)
        min_y = min(p.y for p in points)
        max_x = max(p.x for p in points)
        max_y = max(p.y for p in points)
        return cls.match_pattern(points, min_x, min_y, max_x, max_y, cls.pattern)

class Digit8(Character):
    pattern = [
        "111",
        "101",
        "111",
        "101",
        "111"
    ]
    char_repr = '8'
    @classmethod
    def try_match(cls, points: Set[Point]) -> bool:
        if not points:
            return False
        min_x = min(p.x for p in points)
        min_y = min(p.y for p in points)
        max_x = max(p.x for p in points)
        max_y = max(p.y for p in points)
        return cls.match_pattern(points, min_x, min_y, max_x, max_y, cls.pattern)

class Digit9(Character):
    pattern = [
        "111",
        "101",
        "111",
        "001",
        "111"
    ]
    char_repr = '9'
    @classmethod
    def try_match(cls, points: Set[Point]) -> bool:
        if not points:
            return False
        min_x = min(p.x for p in points)
        min_y = min(p.y for p in points)
        max_x = max(p.x for p in points)
        max_y = max(p.y for p in points)
        return cls.match_pattern(points, min_x, min_y, max_x, max_y, cls.pattern)


# Plus sign: Horizontal line middle + vertical line middle
class Plus(Character):
    pattern = [
        "010",
        "010",
        "111",
        "010",
        "010"
    ]
    char_repr = '+'

    @classmethod
    def try_match(cls, points: Set[Point]) -> bool:
        if not points:
            return False
        # The plus sign is a 5x3 pattern, with 3 in middle row, and middle column vertical line
        min_x = min(p.x for p in points)
        min_y = min(p.y for p in points)
        max_x = max(p.x for p in points)
        max_y = max(p.y for p in points)
        return cls.match_pattern(points, min_x, min_y, max_x, max_y, cls.pattern)


# Minus sign: a horizontal line at center row
class Minus(Character):
    pattern = [
        "000",
        "000",
        "111",
        "000",
        "000"
    ]
    char_repr = '-'

    @classmethod
    def try_match(cls, points: Set[Point]) -> bool:
        if not points:
            return False
        min_x = min(p.x for p in points)
        min_y = min(p.y for p in points)
        max_x = max(p.x for p in points)
        max_y = max(p.y for p in points)
        return cls.match_pattern(points, min_x, min_y, max_x, max_y, cls.pattern)


# Dot (multiplication symbol '・'): a single dot (or small square) in the middle
class Dot(Character):
    pattern = [
        "000",
        "010",
        "000"
    ]
    char_repr = '・'

    @classmethod
    def try_match(cls, points: Set[Point]) -> bool:
        # a small 3x3 with only center is black method
        if not points:
            return False
        min_x = min(p.x for p in points)
        min_y = min(p.y for p in points)
        max_x = max(p.x for p in points)
        max_y = max(p.y for p in points)
        # dot must be 3x3 bounding box size
        if (max_x - min_x +1) != 3 or (max_y - min_y +1)!=3:
            return False
        return cls.match_pattern(points, min_x, min_y, max_x, max_y, cls.pattern)


# Factory that tries to identify character from points by trying all known characters
class CharacterFactory:
    char_classes = [
        Digit0, Digit1, Digit2, Digit3, Digit4, Digit5, Digit6, Digit7, Digit8, Digit9,
        Plus, Minus, Dot
    ]

    @classmethod
    def identify(cls, points: Set[Point]) -> str:
        for char_cls in cls.char_classes:
            if char_cls.try_match(points):
                return char_cls.char_repr
        # If fail to identify, raise error (should not happen)
        raise ValueError(f"Unknown character pattern with points: {points}")


# Expression class for storing tokenized expression and evaluation
class Expression:
    def __init__(self, tokens: List[str]):
        self.tokens = tokens

    def __str__(self):
        return ''.join(self.tokens)

    def evaluate(self) -> int:
        # parse and calculate expression with given + - and ・ operators
        # operator precedence:  ・(mul) > + > -
        # We implement a proper parser with precedence

        def precedence(op: str) -> int:
            if op == '・':
                return 2
            elif op == '+' or op == '-':
                return 1
            else:
                return 0

        def apply_op(a: int, b: int, op: str) -> int:
            if op == '+':
                return a + b
            elif op == '-':
                return a - b
            elif op == '・':
                return a * b
            else:
                raise ValueError(f'Invalid operator {op}')

        # Shunting yard algorithm to convert to Reverse Polish Notation (RPN)
        output_queue = []
        operator_stack = []

        # token iterator and buffer for multi-digit numbers
        i = 0
        n = len(self.tokens)

        while i < n:
            tok = self.tokens[i]
            if tok.isdigit():
                # accumulate consecutive digits to make number
                num_str = tok
                i += 1
                while i < n and self.tokens[i].isdigit():
                    num_str += self.tokens[i]
                    i += 1
                output_queue.append(int(num_str))
                continue
            elif tok in ('+', '-', '・'):
                while operator_stack and precedence(operator_stack[-1]) >= precedence(tok):
                    op = operator_stack.pop()
                    b = output_queue.pop()
                    a = output_queue.pop()
                    output_queue.append(apply_op(a, b, op))
                operator_stack.append(tok)
            else:
                raise ValueError(f"Unknown token {tok}")
            i += 1

        while operator_stack:
            op = operator_stack.pop()
            b = output_queue.pop()
            a = output_queue.pop()
            output_queue.append(apply_op(a, b, op))

        return output_queue[0]


# Main processing class handling input, detection, parsing and evaluation
class CheatCaseSolver:
    def __init__(self, line_segments: List[Tuple[int, int, int, int]]):
        self.line_segments = line_segments
        self.grid = Grid(201, 201)  # specs max 0..200
        self.visited = [[False]*201 for _ in range(201)]

    def build_grid(self):
        for (x1, y1, x2, y2) in self.line_segments:
            self.grid.mark_line(Point(x1, y1), Point(x2, y2))

    def find_char_regions(self) -> List[Set[Point]]:
        # BFS to find connected components of marked cells
        regions = []
        for y in range(self.grid.height):
            for x in range(self.grid.width):
                if self.grid.cells[y][x] and not self.visited[y][x]:
                    region = self.bfs(Point(x,y))
                    regions.append(region)
        return regions

    def bfs(self, start: Point) -> Set[Point]:
        q = deque([start])
        region = set()
        self.visited[start.y][start.x] = True

        while q:
            p = q.popleft()
            region.add(p)

            for n in p.neighbors_4():
                if (0 <= n.x < self.grid.width and 0 <= n.y < self.grid.height
                    and self.grid.cells[n.y][n.x]
                    and not self.visited[n.y][n.x]):
                    self.visited[n.y][n.x] = True
                    q.append(n)
        return region

    def identify_characters(self, regions: List[Set[Point]]) -> List[Tuple[int, str]]:
        # Each region corresponds to a character.
        # The position to sort on is the minimal x of region (smallest X in region)
        identified = []
        for region in regions:
            min_x = min(p.x for p in region)
            char = CharacterFactory.identify(region)
            identified.append((min_x, char))
        # sort by position x ascending
        identified.sort(key=lambda x: x[0])
        return identified

    def parse_expression(self, char_list: List[str]) -> List[str]:
        # Simply return the list of characters as tokens.
        # The problem states the characters are properly formed expressions.
        return char_list

    def solve(self) -> int:
        self.build_grid()
        regions = self.find_char_regions()
        identified = self.identify_characters(regions)
        tokens = [c for (_, c) in identified]
        expr = Expression(tokens)
        return expr.evaluate()


def main():
    input = sys.stdin.readline
    N = int(input())
    segs = []
    for _ in range(N):
        x1,y1,x2,y2 = map(int, input().split())
        segs.append((x1,y1,x2,y2))
    solver = CheatCaseSolver(segs)
    print(solver.solve())


if __name__ == '__main__':
    main()