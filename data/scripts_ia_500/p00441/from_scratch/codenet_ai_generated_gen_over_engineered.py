from typing import List, Tuple, Set, Iterator
import sys
import math


class Point:
    __slots__ = ('x', 'y')
    
    def __init__(self, x: int, y: int) -> None:
        self.x = x
        self.y = y
    
    def __add__(self, other: 'Point') -> 'Point':
        return Point(self.x + other.x, self.y + other.y)
    
    def __sub__(self, other: 'Point') -> 'Point':
        return Point(self.x - other.x, self.y - other.y)
    
    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Point):
            return False
        return self.x == other.x and self.y == other.y
    
    def __hash__(self) -> int:
        return hash((self.x, self.y))
    
    def rotated90(self) -> 'Point':
        # Rotate 90 degrees counter-clockwise around origin
        return Point(-self.y, self.x)
    
    def dist_squared(self, other: 'Point') -> int:
        dx = self.x - other.x
        dy = self.y - other.y
        return dx * dx + dy * dy


class SquareFinder:
    def __init__(self, points: List[Point]) -> None:
        self.points = points
        self.point_set: Set[Point] = set(points)
    
    def find_max_square_area(self) -> int:
        n = len(self.points)
        max_area = 0
        for i in range(n):
            for j in range(i + 1, n):
                p1 = self.points[i]
                p2 = self.points[j]
                v = p2 - p1
                # Rotate vector v by 90 degrees to get perpendicular vector
                v90 = v.rotated90()
                
                p3 = p2 + v90
                p4 = p1 + v90
                if p3 in self.point_set and p4 in self.point_set:
                    area = v.dist_squared(p1)
                    if area > max_area:
                        max_area = area
                
                # Also consider the square rotated -90 degrees (other orientation)
                v_90_neg = Point(v.y, -v.x)
                p3_neg = p2 + v_90_neg
                p4_neg = p1 + v_90_neg
                if p3_neg in self.point_set and p4_neg in self.point_set:
                    area = v.dist_squared(p1)
                    if area > max_area:
                        max_area = area
        return max_area


class InputParser:
    def __init__(self, stream: Iterator[str]) -> None:
        self.stream = stream
    
    def parse(self) -> Iterator[List[Point]]:
        while True:
            line = next(self.stream).strip()
            if line == '0':
                break
            n = int(line)
            points = []
            for _ in range(n):
                x, y = map(int, next(self.stream).strip().split())
                points.append(Point(x, y))
            yield points


class Solution:
    def __init__(self, input_lines: Iterator[str]) -> None:
        self.parser = InputParser(input_lines)
    
    def run(self) -> None:
        for points in self.parser.parse():
            finder = SquareFinder(points)
            max_area = finder.find_max_square_area()
            print(max_area)


def main():
    solution = Solution(iter(sys.stdin))
    solution.run()


if __name__ == '__main__':
    main()