class StoneColor:
    WHITE = 0
    BLACK = 1

    _symbols = {
        WHITE: '○',
        BLACK: '●'
    }

    @classmethod
    def symbol(cls, c):
        return cls._symbols[c]

    @classmethod
    def opposite(cls, c):
        return cls.BLACK if c == cls.WHITE else cls.WHITE


class StoneGroup:
    def __init__(self, color: int, count: int):
        self.color = color
        self.count = count

    def __repr__(self):
        return f"{StoneColor.symbol(self.color)}*{self.count}"


class Table:
    def __init__(self):
        self.groups = []
        self.white_count = 0

    def place_stone(self, color: int, index: int):
        # index 1-based, but unused for internal logic except parity rule
        if index % 2 == 1:
            # odd i: just place stone at i-th position, no groups replacement
            # Implemented by appending this stone alone (conceptually)
            # But we must maintain the stack of groups for efficiency.
            self._add_stone(color)
        else:
            # even i:
            if not self.groups:
                # no stone placed yet, just add
                self._add_stone(color)
                return

            right_color = self.groups[-1].color
            if right_color == color:
                # same color as right end, just place stone
                self._add_stone(color)
            else:
                # different color: remove all continuous stones of right end color from right,
                # replace by stones with new color with the same count, then place new stone of the same color.
                removed_count = self._pop_right_color_sequence()
                # add replaced stones with new color (count = removed_count)
                self._add_group(color, removed_count)
                # add final stone
                self._add_stone(color)

    def _add_stone(self, color: int):
        # Append one stone to the right end
        if self.groups and self.groups[-1].color == color:
            self.groups[-1].count += 1
        else:
            self.groups.append(StoneGroup(color, 1))
        if color == StoneColor.WHITE:
            self.white_count += 1

    def _pop_right_color_sequence(self) -> int:
        # Remove all continuous stones on right end having same color
        if not self.groups:
            return 0
        right_color = self.groups[-1].color
        count = 0
        while self.groups and self.groups[-1].color == right_color:
            group = self.groups.pop()
            count += group.count
            if right_color == StoneColor.WHITE:
                self.white_count -= group.count
        return count

    def _add_group(self, color: int, count: int):
        # Add a group of stones of same color at right end
        if count == 0:
            return
        if self.groups and self.groups[-1].color == color:
            self.groups[-1].count += count
        else:
            self.groups.append(StoneGroup(color, count))
        if color == StoneColor.WHITE:
            self.white_count += count

    def get_white_count(self) -> int:
        return self.white_count


class InputProcessor:
    def __init__(self):
        self.datasets = []

    def read_datasets(self):
        while True:
            n = self._read_integer()
            if n == 0:
                break
            colors = [self._read_integer() for _ in range(n)]
            self.datasets.append((n, colors))

    @staticmethod
    def _read_integer() -> int:
        import sys
        while True:
            line = sys.stdin.readline()
            if line == '':
                return 0
            line = line.strip()
            if line == '':
                continue
            return int(line)


class OutputProcessor:
    @staticmethod
    def output_white_count(count: int):
        print(count)


class GosekiGame:
    def __init__(self, n: int, colors: list[int]):
        self.n = n
        self.colors = colors
        self.table = Table()

    def play(self):
        for i, color in enumerate(self.colors, start=1):
            self.table.place_stone(color, i)

    def get_result(self):
        return self.table.get_white_count()


def main():
    input_processor = InputProcessor()
    input_processor.read_datasets()
    for n, colors in input_processor.datasets:
        game = GosekiGame(n, colors)
        game.play()
        result = game.get_result()
        OutputProcessor.output_white_count(result)


if __name__ == '__main__':
    main()