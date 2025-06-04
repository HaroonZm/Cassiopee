class RoadGrid:
    def __init__(self, height, width, occupants_matrix):
        self.height = height
        self.width = width
        self.occupants_matrix = occupants_matrix

    def get_occupants(self, i, j):
        return self.occupants_matrix[i - 1][j - 1]  # 1-based indexing adaption


class TrunkRoadSelector:
    def __init__(self, road_grid):
        self.grid = road_grid
        self.cache = {}

    def distance_sum(self, h_road, w_road):
        # Memoization key
        key = (h_road, w_road)
        if key in self.cache:
            return self.cache[key]
        total_distance = 0
        for i in range(1, self.grid.height + 1):
            for j in range(1, self.grid.width + 1):
                occupants = self.grid.get_occupants(i, j)
                dist_to_h = abs(i - h_road)
                dist_to_w = abs(j - w_road)
                total_distance += occupants * min(dist_to_h, dist_to_w)
        self.cache[key] = total_distance
        return total_distance

    def find_optimal_roads(self):
        min_distance = float('inf')
        best_pair = (None, None)
        for h_road in range(1, self.grid.height + 1):
            for w_road in range(1, self.grid.width + 1):
                dist = self.distance_sum(h_road, w_road)
                if dist < min_distance:
                    min_distance = dist
                    best_pair = (h_road, w_road)
        return best_pair, min_distance


class InputManager:
    @staticmethod
    def parse_input():
        import sys
        input_lines = sys.stdin.read().strip().split()
        H, W = int(input_lines[0]), int(input_lines[1])
        occupants_matrix = []
        idx = 2
        for _ in range(H):
            row = list(map(int, input_lines[idx:idx + W]))
            idx += W
            occupants_matrix.append(row)
        return H, W, occupants_matrix


class OutputManager:
    @staticmethod
    def print_result(result):
        print(result)


class JOI2017_TrunkRoadProblem:
    def __init__(self):
        self.input_manager = InputManager()
        self.output_manager = OutputManager()

    def solve(self):
        H, W, occupants_matrix = self.input_manager.parse_input()
        grid = RoadGrid(H, W, occupants_matrix)
        selector = TrunkRoadSelector(grid)
        _, min_dist = selector.find_optimal_roads()
        self.output_manager.print_result(min_dist)


if __name__ == '__main__':
    problem = JOI2017_TrunkRoadProblem()
    problem.solve()