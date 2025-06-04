class TravelPath:
    def __init__(self, town_count: int, distances_between_towns: list[int]) -> None:
        self.town_count = town_count
        # Compute prefix sums of distances for O(1) segment distance queries
        self.prefix_distances = self._compute_prefix_distances(distances_between_towns)

    @staticmethod
    def _compute_prefix_distances(distances: list[int]) -> list[int]:
        prefix = [0]
        for dist in distances:
            prefix.append(prefix[-1] + dist)
        return prefix

    def distance(self, start: int, end: int) -> int:
        # start and end are town indices (1-based)
        # Return the absolute distance between start and end towns
        if start < end:
            return self.prefix_distances[end - 1] - self.prefix_distances[start - 1]
        else:
            return self.prefix_distances[start - 1] - self.prefix_distances[end - 1]


class Journey:
    MODULO = 10**5

    def __init__(self, travel_path: TravelPath, daily_moves: list[int]) -> None:
        self.travel_path = travel_path
        self.daily_moves = daily_moves
        self.current_town = 1
        self.total_distance = 0

    def _move_one_day(self, distance_move: int) -> None:
        next_town = self.current_town + distance_move
        # Movement must be within road bounds as per problem statement
        if not (1 <= next_town <= self.travel_path.town_count):
            raise ValueError("Move out of bounds")
        distance = self.travel_path.distance(self.current_town, next_town)
        self.total_distance += distance
        self.current_town = next_town

    def travel(self) -> int:
        for move in self.daily_moves:
            self._move_one_day(move)
        return self.total_distance % self.MODULO


class InputParser:
    @staticmethod
    def parse_input() -> tuple[int, int, list[int], list[int]]:
        import sys
        input = sys.stdin.readline

        n, m = map(int, input().split())
        distances = [int(input()) for _ in range(n - 1)]
        moves = [int(input()) for _ in range(m)]
        return n, m, distances, moves


class TravelController:
    def __init__(self):
        self.n = 0
        self.m = 0
        self.distances = []
        self.moves = []

    def load_data(self) -> None:
        self.n, self.m, self.distances, self.moves = InputParser.parse_input()

    def execute(self) -> None:
        travel_path = TravelPath(self.n, self.distances)
        journey = Journey(travel_path, self.moves)
        result = journey.travel()
        print(result)


if __name__ == '__main__':
    controller = TravelController()
    controller.load_data()
    controller.execute()