class GridDimension:
    def __init__(self, height: int, width: int):
        self.height = height
        self.width = width

class CellState:
    CLOUD = 'c'
    CLEAR = '.'

class CloudField:
    def __init__(self, dimension: GridDimension, initial_map: list[str]):
        self.dimension = dimension
        self.initial_map = initial_map
        self.arrival_minutes = [[-1 for _ in range(self.dimension.width)] for _ in range(self.dimension.height)]

    def compute_arrival_times(self):
        # For each row, find clouds positions and compute minutes of arrival for each cell
        for i in range(self.dimension.height):
            cloud_positions = [j for j, ch in enumerate(self.initial_map[i]) if ch == CellState.CLOUD]
            for j in range(self.dimension.width):
                # If cell initially has cloud
                if self.initial_map[i][j] == CellState.CLOUD:
                    self.arrival_minutes[i][j] = 0
                else:
                    # Check if there's any cloud to the west that will arrive
                    candidates = [cloud_j for cloud_j in cloud_positions if cloud_j <= j]
                    if not candidates:
                        self.arrival_minutes[i][j] = -1
                    else:
                        earliest = min(j - cloud_j for cloud_j in candidates)
                        self.arrival_minutes[i][j] = earliest

    def get_arrival_minutes(self):
        return self.arrival_minutes

class WeatherForecasterApp:
    def __init__(self):
        self.dimension = None
        self.cloud_field = None

    def parse_input(self, input_lines: list[str]):
        h, w = map(int, input_lines[0].split())
        self.dimension = GridDimension(h, w)
        initial_map = [line.strip() for line in input_lines[1:h+1]]
        self.cloud_field = CloudField(self.dimension, initial_map)

    def predict(self):
        self.cloud_field.compute_arrival_times()

    def output(self):
        result = []
        for row in self.cloud_field.get_arrival_minutes():
            result.append(' '.join(map(str, row)))
        return '\n'.join(result)

def main():
    import sys
    input_lines = sys.stdin.read().strip().split('\n')
    app = WeatherForecasterApp()
    app.parse_input(input_lines)
    app.predict()
    print(app.output())

if __name__ == "__main__":
    main()