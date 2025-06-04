from typing import List, Tuple, Iterator, Any
from functools import cached_property

class Panel:
    __slots__ = ('name', 'x1', 'y1', 'x2', 'y2', 'children')

    def __init__(self, name: str, points: List[int], children: List['Panel']):
        self.name = name
        self.x1, self.y1, self.x2, self.y2 = points
        self.children = children

    @cached_property
    def child_cnt(self) -> int:
        return len(self.children)

    def search(self, x: int, y: int) -> Tuple[Any, ...]:
        if not (self.x1 <= x <= self.x2 and self.y1 <= y <= self.y2):
            return ("OUT", "OF", "MAIN", "PANEL", "1")
        for child in self.children:
            if child.x1 <= x <= child.x2 and child.y1 <= y <= child.y2:
                return child.search(x, y)
        return (self.name, self.child_cnt)

def parse_tag_structure(s: str, pointer: int) -> Tuple['Panel', int]:
    name, pointer = parse_begin_tag(s, pointer)
    points, pointer = parse_tag_value(s, pointer)
    children = []
    while True:
        if s[pointer + 1] == "/":
            break
        child, pointer = parse_tag_structure(s, pointer)
        children.append(child)
    pointer = parse_end_tag(s, pointer)
    return Panel(name, points, children), pointer

def parse_begin_tag(s: str, pointer: int) -> Tuple[str, int]:
    pointer += 1
    end = s.index(">", pointer)
    return s[pointer:end], end + 1

def parse_tag_value(s: str, pointer: int) -> Tuple[List[int], int]:
    vals = []
    for _ in range(4):
        start = pointer
        while s[pointer].isdigit():
            pointer += 1
        vals.append(int(s[start:pointer]))
        pointer += 1
    return vals, pointer - 1

def parse_end_tag(s: str, pointer: int) -> int:
    return s.index(">", pointer) + 1

def main():
    import sys
    input_iter = iter(sys.stdin.read().splitlines())
    while True:
        try:
            n = int(next(input_iter))
        except StopIteration:
            break
        if n == 0:
            break
        s = next(input_iter)
        panel, _ = parse_tag_structure(s, 0)
        for _ in range(n):
            x, y = map(int, next(input_iter).split())
            print(*panel.search(x, y))
main()