class City:
    def __init__(self, name):
        self.name = name
        self.edges = {}  # key: digit '0' or '1', value: City

    def connect(self, digit, city):
        self.edges[digit] = city


class MapGraph:
    def __init__(self):
        self.cities = {}
        self._build_graph()

    def _get_or_create_city(self, name):
        if name not in self.cities:
            self.cities[name] = City(name)
        return self.cities[name]

    def _build_graph(self):
        # Constructs the fixed graph given by the problem's map
        # A市 → X (0), Y (1)
        # X → Z (0), Y (1)
        # Y → Z (0), W (1)
        # Z → W (0), B (1)
        # W → B (0), Y (1)
        # B → X (0), Z (1)

        A = self._get_or_create_city("A")
        X = self._get_or_create_city("X")
        Y = self._get_or_create_city("Y")
        Z = self._get_or_create_city("Z")
        W = self._get_or_create_city("W")
        B = self._get_or_create_city("B")

        A.connect('0', X)
        A.connect('1', Y)

        X.connect('0', Z)
        X.connect('1', Y)

        Y.connect('0', Z)
        Y.connect('1', W)

        Z.connect('0', W)
        Z.connect('1', B)

        W.connect('0', B)
        W.connect('1', Y)

        B.connect('0', X)
        B.connect('1', Z)

        self.start_city = A
        self.goal_city = B

    def follows_path(self, path_str):
        current_city = self.start_city
        for digit in path_str:
            if digit not in current_city.edges:
                return False
            current_city = current_city.edges[digit]
        return current_city == self.goal_city


class AkabekoNavigator:
    def __init__(self):
        self.graph = MapGraph()

    def query(self, path):
        if self.graph.follows_path(path):
            return "Yes"
        else:
            return "No"


class InputHandler:
    def __init__(self, navigator):
        self.navigator = navigator

    def process_inputs(self):
        import sys
        for line in sys.stdin:
            line = line.strip()
            if line == "#":
                break
            if line == "":
                continue
            print(self.navigator.query(line))


if __name__ == "__main__":
    navigator = AkabekoNavigator()
    handler = InputHandler(navigator)
    handler.process_inputs()