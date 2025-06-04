class SquarePyramid:
    class Base:
        def __init__(self, side_length: float):
            self.side_length = side_length

        def area(self) -> float:
            return self.side_length ** 2

    class SlantHeightCalculator:
        @staticmethod
        def calculate_slant_height(height: float, base_side: float) -> float:
            # The apex is vertically above the base center,
            # so the slant height is sqrt(h^2 + (x/2)^2)
            return (height ** 2 + (base_side / 2) ** 2) ** 0.5

    class LateralSurface:
        def __init__(self, base_side: float, slant_height: float):
            self.base_side = base_side
            self.slant_height = slant_height

        def area(self) -> float:
            # 4 triangular faces, each = (base_side * slant_height) / 2
            return 4 * (self.base_side * self.slant_height / 2)

    def __init__(self, side_length: float, height: float):
        self.base = self.Base(side_length)
        self.height = height
        self.slant_height = self.SlantHeightCalculator.calculate_slant_height(
            height, side_length
        )
        self.lateral_surface = self.LateralSurface(side_length, self.slant_height)

    def surface_area(self) -> float:
        return self.base.area() + self.lateral_surface.area()


class InputProcessor:
    def __init__(self):
        self.datasets = []

    def read(self):
        while True:
            try:
                x = input().strip()
                if x == '':
                    continue
                h = input().strip()
                if h == '':
                    continue
            except EOFError:
                break
            x_int = int(x)
            h_int = int(h)
            if x_int == 0 and h_int == 0:
                break
            self.datasets.append((x_int, h_int))

    def get_datasets(self):
        return self.datasets


class OutputFormatter:
    @staticmethod
    def format_surface_area(surface_area: float) -> str:
        return f"{surface_area:.6f}"


def main():
    input_processor = InputProcessor()
    input_processor.read()
    for x, h in input_processor.get_datasets():
        pyramid = SquarePyramid(x, h)
        area = pyramid.surface_area()
        print(OutputFormatter.format_surface_area(area))


if __name__ == "__main__":
    main()