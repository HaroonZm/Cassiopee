class City:
    def __init__(self, name):
        self.name = name
        self.paths = {}

    def add_path(self, bit, city):
        self.paths[bit] = city

    def next_city(self, bit):
        return self.paths.get(bit, None)

class RouteValidator:
    def __init__(self):
        self._build_map()

    def _build_map(self):
        # Create cities
        self.cities = {}
        for name in ['A', 'X', 'Y', 'Z', 'W', 'B']:
            self.cities[name] = City(name)
        A = self.cities['A']
        X = self.cities['X']
        Y = self.cities['Y']
        Z = self.cities['Z']
        W = self.cities['W']
        B = self.cities['B']
        # Build paths with bits as keys for transitions
        # According to problem statement and sample path 0100 is A->X->Z->W->B
        # We infer A: 0->X,1->Y
        A.add_path('0', X)
        A.add_path('1', Y)
        # X: 0->Z,1->B
        X.add_path('0', Z)
        X.add_path('1', B)
        # Y: 0->X,1->B
        Y.add_path('0', X)
        Y.add_path('1', B)
        # Z: 0->W,1->B
        Z.add_path('0', W)
        Z.add_path('1', B)
        # W: 0->B,1->Y
        W.add_path('0', B)
        W.add_path('1', Y)
        # B: no outgoing edges (end)
        self.start_city = A
        self.target_city = B

    def validate_path(self, path_pattern):
        current_city = self.start_city
        for bit in path_pattern:
            next_city = current_city.next_city(bit)
            if next_city is None:
                return False
            current_city = next_city
        return current_city == self.target_city

class InputProcessor:
    def __init__(self):
        self.validator = RouteValidator()

    def process(self):
        import sys
        for line in sys.stdin:
            p = line.strip()
            if p == '#':
                break
            if self.validator.validate_path(p):
                print("Yes")
            else:
                print("No")

if __name__ == "__main__":
    InputProcessor().process()