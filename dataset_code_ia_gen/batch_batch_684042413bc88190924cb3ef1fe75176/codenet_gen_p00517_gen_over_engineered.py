class Coordinate:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

    def manhattan(self, other: 'Coordinate') -> int:
        return abs(self.x - other.x) + abs(self.y - other.y)

    def chebyshev(self, other: 'Coordinate') -> int:
        return max(abs(self.x - other.x), abs(self.y - other.y))


class GridGraph:
    """
    Represents the grid with specific movement rules.
    Movement allowed:
    - Up, Down, Left, Right (if within bounds)
    - Diagonal NE (i-1, j-1) and SW (i+1, j+1) edges as per problem
    """

    def __init__(self, width: int, height: int):
        self.width = width
        self.height = height

    def distance(self, start: Coordinate, goal: Coordinate) -> int:
        """
        Computes the minimum number of edges between start and goal nodes.
        Movement cost is uniform (1 per edge).

        Due to the specific edges, the shortest path distance is derived based on the grid properties:
        You can move in 4 orthogonal directions and 2 diagonal directions:
        NE (i-1, j-1), SW (i+1, j+1)

        The problem reduces to:
        minimal steps = max(|x1 - x2|, |y1 - y2|)
        Explanation:
        - Diagonal moves allowed only if both coordinates move consistently. So you can move diagonally
          in the direction where both coordinates increase or decrease simultaneously.
        - For other coordinate differences (e.g. x increases and y decreases), you must compensate with orthogonal moves.
        
        The minimal distance is the Chebyshev distance.
        """
        return start.chebyshev(goal)


class TourPlan:
    def __init__(self, spots: list[Coordinate], graph: GridGraph):
        self.spots = spots
        self.graph = graph

    def minimal_total_distance(self) -> int:
        """
        Calculates the total minimal distance traveling through the spots in order given.
        """
        total = 0
        for i in range(len(self.spots) - 1):
            dist = self.graph.distance(self.spots[i], self.spots[i + 1])
            total += dist
        return total


class InputParser:
    @staticmethod
    def parse() -> tuple[GridGraph, list[Coordinate]]:
        import sys
        input_line = sys.stdin.readline
        W, H, N = map(int, input_line().split())
        graph = GridGraph(W, H)
        spots = []
        for _ in range(N):
            x, y = map(int, input_line().split())
            spots.append(Coordinate(x, y))
        return graph, spots


class SolutionCoordinator:
    def __init__(self):
        self.graph: GridGraph
        self.spots: list[Coordinate]

    def read_input(self):
        self.graph, self.spots = InputParser.parse()

    def solve(self):
        tour = TourPlan(self.spots, self.graph)
        print(tour.minimal_total_distance())

def main():
    sc = SolutionCoordinator()
    sc.read_input()
    sc.solve()

if __name__ == "__main__":
    main()