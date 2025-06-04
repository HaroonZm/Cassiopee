import sys
import math
from abc import ABC, abstractmethod
from typing import List, Tuple, Iterator

class Point2D:
    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y
        
    def distance_to(self, other: 'Point2D') -> float:
        dx = self.x - other.x
        dy = self.y - other.y
        return math.hypot(dx, dy)
    
    def __repr__(self):
        return f"Point2D({self.x}, {self.y})"

class SweetShop:
    def __init__(self, position: Point2D, velocity: float):
        self.position = position
        self.velocity = velocity
        
    def time_from(self, point: Point2D) -> float:
        return self.position.distance_to(point) / self.velocity
    
    def __repr__(self):
        return f"SweetShop(pos={self.position}, v={self.velocity})"

class OptimalResidenceFinder(ABC):
    def __init__(self, shops: List[SweetShop]):
        self.shops = shops
    
    @abstractmethod
    def find_optimal_location(self) -> Tuple[Point2D, float]:
        pass

class GeometricMedianTimeMinimizer(OptimalResidenceFinder):
    """
    Finds the point which minimizes the maximal time to all sweet shops.
    Uses iterative optimization with early stopping criterion.
    """
    def __init__(self, shops: List[SweetShop]):
        super().__init__(shops)
        self.epsilon = 1e-11
        self.max_iter = 100000
        self.step_initial = 100.0
    
    def find_optimal_location(self) -> Tuple[Point2D, float]:
        # We can restrict search area: all shops coordinates between 0 and 100 per constraints
        # Start in the centroid of all sweet shops
        avg_x = sum(shop.position.x for shop in self.shops) / len(self.shops)
        avg_y = sum(shop.position.y for shop in self.shops) / len(self.shops)
        current_point = Point2D(avg_x, avg_y)
        best_time = self._max_time(current_point)
        
        step = self.step_initial
        directions = [
            (1,0), (-1,0), (0,1), (0,-1),
            (1,1), (-1,1), (1,-1), (-1,-1)
        ]
        
        for _ in range(self.max_iter):
            improved = False
            for dx, dy in directions:
                np = Point2D(current_point.x + dx*step, current_point.y + dy*step)
                candidate_time = self._max_time(np)
                if candidate_time + self.epsilon < best_time:
                    current_point = np
                    best_time = candidate_time
                    improved = True
                    break
            if not improved:
                step /= 2
                if step < self.epsilon:
                    break
        return current_point, best_time
    
    def _max_time(self, point: Point2D) -> float:
        # Computes maximum travel time to all sweet shops from point
        return max(shop.time_from(point) for shop in self.shops)

class InputParser:
    def __init__(self, input_stream: Iterator[str]):
        self.input_stream = input_stream
    
    def parse_testcases(self) -> Iterator[List[SweetShop]]:
        while True:
            try:
                line = next(self.input_stream)
            except StopIteration:
                break
            
            if line.strip() == '':
                continue
            
            N = int(line.strip())
            if N == 0:
                break
            
            shops = []
            for _ in range(N):
                line = next(self.input_stream)
                x_str, y_str, v_str = line.strip().split()
                x, y, v = int(x_str), int(y_str), int(v_str)
                position = Point2D(x,y)
                shop = SweetShop(position, v)
                shops.append(shop)
            yield shops

def main():
    input_lines = iter(sys.stdin.read().strip().split('\n'))
    parser = InputParser(input_lines)
    
    for shops in parser.parse_testcases():
        finder = GeometricMedianTimeMinimizer(shops)
        _, min_max_time = finder.find_optimal_location()
        print(f"{min_max_time:.8f}")

if __name__ == "__main__":
    main()