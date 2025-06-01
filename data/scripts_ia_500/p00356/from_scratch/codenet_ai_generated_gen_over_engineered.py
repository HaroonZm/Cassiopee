class PanelDimensions:
    def __init__(self, width: int, height: int):
        self.width = width
        self.height = height

class Wall:
    def __init__(self, panels_horizontal: int, panels_vertical: int, panel_dimensions: PanelDimensions):
        self.panels_horizontal = panels_horizontal
        self.panels_vertical = panels_vertical
        self.panel_dimensions = panel_dimensions

    def total_width(self):
        return self.panels_horizontal * self.panel_dimensions.width

    def total_height(self):
        return self.panels_vertical * self.panel_dimensions.height

class WirePath:
    def __init__(self, wall: Wall):
        self.wall = wall

    def gcd(self, a: int, b: int) -> int:
        while b:
            a, b = b, a % b
        return a

    def intersection_points_count(self) -> int:
        # The wire goes from (0, 0) to (total_width, total_height)
        # Since panel boundaries are at each multiple of panel width and height,
        # the number of intersection points is gcd(x, y) + 1
        # where x, y are number of panels.
        g = self.gcd(self.wall.panels_horizontal, self.wall.panels_vertical)
        return g + 1

class InputReader:
    @staticmethod
    def read_input():
        line = input().strip()
        x_str, y_str = line.split()
        return int(x_str), int(y_str)

class OutputWriter:
    @staticmethod
    def print_output(value: int):
        print(value)

class WireIntersectionsApp:
    def __init__(self):
        self.panel_dimensions = PanelDimensions(width=2, height=1)  # fixed by problem statement

    def run(self):
        x, y = InputReader.read_input()
        wall = Wall(x, y, self.panel_dimensions)
        wire_path = WirePath(wall)
        result = wire_path.intersection_points_count()
        OutputWriter.print_output(result)

if __name__ == '__main__':
    app = WireIntersectionsApp()
    app.run()