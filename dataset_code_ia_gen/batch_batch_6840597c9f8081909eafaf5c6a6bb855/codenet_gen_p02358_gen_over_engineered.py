from typing import List, Tuple
from abc import ABC, abstractmethod
import sys

class Coordinate:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

    def __lt__(self, other:'Coordinate') -> bool:
        return (self.x, self.y) < (other.x, other.y)

    def __eq__(self, other:'Coordinate') -> bool:
        return (self.x, self.y) == (other.x, other.y)

class Rectangle:
    def __init__(self, top_left: Coordinate, bottom_right: Coordinate):
        if not (top_left.x < bottom_right.x and top_left.y < bottom_right.y):
            raise ValueError("Invalid rectangle coordinates: top_left must be left and above bottom_right.")
        self.top_left = top_left
        self.bottom_right = bottom_right

    @property
    def x1(self):
        return self.top_left.x

    @property
    def y1(self):
        return self.top_left.y

    @property
    def x2(self):
        return self.bottom_right.x

    @property
    def y2(self):
        return self.bottom_right.y

class EventType:
    ENTER = 1
    LEAVE = -1

class SweepEvent:
    def __init__(self, x: int, y1: int, y2: int, type_: int):
        self.x = x
        self.y1 = y1
        self.y2 = y2
        self.type = type_  # ENTER=1 or LEAVE=-1

    def __lt__(self, other:'SweepEvent'):
        # Sort by x, then ENTER events before LEAVE events to handle same x correctly
        if self.x == other.x:
            return self.type > other.type
        return self.x < other.x

class SegmentTreeNode:
    def __init__(self, left: int, right: int):
        self.left = left
        self.right = right
        self.left_child = None
        self.right_child = None
        self.cover_count = 0   # how many intervals currently fully cover this segment
        self.covered_length = 0

class SegmentTree(ABC):
    def __init__(self, coords: List[int]):
        self.coords = coords
        self.root = self.build(0, len(coords) - 1)

    @abstractmethod
    def build(self, left: int, right: int) -> SegmentTreeNode:
        pass

    @abstractmethod
    def update(self, node: SegmentTreeNode, start: int, end: int, val: int) -> None:
        pass

    @abstractmethod
    def query(self) -> int:
        pass

class YSegmentTree(SegmentTree):
    def build(self, left: int, right: int) -> SegmentTreeNode:
        node = SegmentTreeNode(left, right)
        if right - left > 1:
            mid = (left + right) // 2
            node.left_child = self.build(left, mid)
            node.right_child = self.build(mid, right)
        return node

    def update(self, node: SegmentTreeNode, start: int, end: int, val: int) -> None:
        if node.right <= start or node.left >= end:
            return
        if start <= node.left and node.right <= end:
            node.cover_count += val
        else:
            self.update(node.left_child, start, end, val)
            self.update(node.right_child, start, end, val)
        if node.cover_count > 0:
            node.covered_length = self.coords[node.right] - self.coords[node.left]
        else:
            if node.right - node.left == 1:
                node.covered_length = 0
            else:
                node.covered_length = node.left_child.covered_length + node.right_child.covered_length

    def query(self) -> int:
        return self.root.covered_length

class RectangleUnionAreaCalculator(ABC):
    def __init__(self, rectangles: List[Rectangle]):
        self.rectangles = rectangles

    @abstractmethod
    def compute_area(self) -> int:
        pass

class SweepLineRectangleUnionAreaCalculator(RectangleUnionAreaCalculator):
    def __init__(self, rectangles: List[Rectangle]):
        super().__init__(rectangles)

    def compute_area(self) -> int:
        events: List[SweepEvent] = []
        ys = set()
        for rect in self.rectangles:
            # Top-left (x1,y1), bottom-right (x2,y2)
            # We generate two events per rectangle for sweep line
            # We assume y1<y2 and x1<x2 from problem statement.
            events.append(SweepEvent(rect.x1, rect.y1, rect.y2, EventType.ENTER))
            events.append(SweepEvent(rect.x2, rect.y1, rect.y2, EventType.LEAVE))
            ys.add(rect.y1)
            ys.add(rect.y2)

        coords = sorted(ys)
        y_to_idx = {y:i for i,y in enumerate(coords)}

        events.sort()

        st = YSegmentTree(coords)
        area = 0
        prev_x = events[0].x
        for event in events:
            curr_x = event.x
            covered_length = st.query()
            area += covered_length * (curr_x - prev_x)
            st.update(st.root, y_to_idx[event.y1], y_to_idx[event.y2], event.type)
            prev_x = curr_x

        return area

class InputParser:
    def parse(self) -> List[Rectangle]:
        input_lines = sys.stdin.read().strip().split('\n')
        n = int(input_lines[0])
        rectangles = []
        idx = 1
        for _ in range(n):
            x1, y1, x2, y2 = map(int, input_lines[idx].split())
            idx += 1
            # Coordinates are top-left (x1,y1), bottom-right (x2,y2)
            top_left = Coordinate(x1, y1)
            bottom_right = Coordinate(x2, y2)
            rectangles.append(Rectangle(top_left, bottom_right))
        return rectangles

def main():
    parser = InputParser()
    rectangles = parser.parse()
    calculator = SweepLineRectangleUnionAreaCalculator(rectangles)
    area = calculator.compute_area()
    print(area)

if __name__ == "__main__":
    main()