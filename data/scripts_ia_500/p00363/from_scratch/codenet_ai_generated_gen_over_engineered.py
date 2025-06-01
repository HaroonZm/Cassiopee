class FlagDimension:
    def __init__(self, width: int, height: int):
        if width < 3 or width > 21 or height < 3 or height > 21:
            raise ValueError("Width and height must be between 3 and 21")
        if width % 2 == 0 or height % 2 == 0:
            raise ValueError("Width and height must be odd numbers")
        self.width = width
        self.height = height

    @property
    def center(self):
        return (self.width // 2, self.height // 2)

class FlagCharacter:
    CORNER = '+'
    HORIZONTAL = '-'
    VERTICAL = '|'
    BACKGROUND = '.'

class FlagCanvas:
    def __init__(self, dimension: FlagDimension, letter: str):
        self.dimension = dimension
        self.letter = letter
        self.pixels = [[FlagCharacter.BACKGROUND for _ in range(dimension.width)] for _ in range(dimension.height)]

    def draw_edges(self):
        w, h = self.dimension.width, self.dimension.height
        # corners
        self.pixels[0][0] = FlagCharacter.CORNER
        self.pixels[0][w - 1] = FlagCharacter.CORNER
        self.pixels[h - 1][0] = FlagCharacter.CORNER
        self.pixels[h - 1][w - 1] = FlagCharacter.CORNER
        # top and bottom lines
        for x in range(1, w - 1):
            self.pixels[0][x] = FlagCharacter.HORIZONTAL
            self.pixels[h - 1][x] = FlagCharacter.HORIZONTAL
        # left and right lines
        for y in range(1, h - 1):
            self.pixels[y][0] = FlagCharacter.VERTICAL
            self.pixels[y][w - 1] = FlagCharacter.VERTICAL

    def put_center_letter(self):
        cx, cy = self.dimension.center
        self.pixels[cy][cx] = self.letter

    def render(self):
        return '\n'.join(''.join(row) for row in self.pixels)

class FlagFactory:
    @staticmethod
    def create_flag(width: int, height: int, letter: str) -> FlagCanvas:
        dimension = FlagDimension(width, height)
        canvas = FlagCanvas(dimension, letter)
        canvas.draw_edges()
        canvas.put_center_letter()
        return canvas

class FlagApp:
    def __init__(self):
        self.flag = None

    def read_input(self):
        import sys
        parts = []
        while len(parts) < 3:
            line = sys.stdin.readline()
            if not line:
                break
            parts += line.split()
        if len(parts) != 3:
            raise ValueError("Input requires exactly three values: W H c")
        w, h = int(parts[0]), int(parts[1])
        c = parts[2]
        if len(c) != 1 or not c.isupper():
            raise ValueError("The character must be a single uppercase letter")
        self.flag = FlagFactory.create_flag(w, h, c)

    def run(self):
        self.read_input()
        if self.flag is not None:
            print(self.flag.render())

if __name__ == "__main__":
    app = FlagApp()
    app.run()