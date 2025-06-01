class GoStone:
    WHITE = 0
    BLACK = 1

    def __init__(self, color: int):
        self.color = color

    def is_white(self) -> bool:
        return self.color == GoStone.WHITE

    def is_black(self) -> bool:
        return self.color == GoStone.BLACK

class StoneBlock:
    def __init__(self, color: int, count: int):
        self.color = color
        self.count = count

    def merge(self, other: 'StoneBlock') -> bool:
        if self.color == other.color:
            self.count += other.count
            return True
        return False

class StoneStack:
    def __init__(self):
        # stack of StoneBlock, each block represents a contiguous run of stones with same color
        self.blocks = []

    def push(self, stone: GoStone):
        if not self.blocks or self.blocks[-1].color != stone.color:
            self.blocks.append(StoneBlock(stone.color, 1))
        else:
            self.blocks[-1].count += 1

    def right_color(self) -> int:
        if not self.blocks:
            raise RuntimeError("Stack is empty")
        return self.blocks[-1].color

    def remove_right_blocks(self, color: int):
        # Remove contiguous blocks of given color from end
        while self.blocks and self.blocks[-1].color == color:
            self.blocks.pop()

    def total_white_stones(self) -> int:
        return sum(block.count for block in self.blocks if block.color == GoStone.WHITE)

class GoTable:
    def __init__(self):
        self.stack = StoneStack()
        self.step = 0

    def place_stone(self, color: int):
        self.step += 1
        stone = GoStone(color)

        # According to rules:
        # If odd step: simply add stone at position i, no replacement
        if self.step % 2 == 1:
            self.stack.push(stone)
            return

        # For even step:
        right_color = self.stack.right_color()
        if stone.color == right_color:
            # Same color as right end: just add stone
            self.stack.push(stone)
        else:
            # Different color
            # Remove right end contiguous stones of the right_color
            self.stack.remove_right_blocks(right_color)
            # Replace with block of stones of the new stone's color equal to the removed count
            # According to problem, number of stones to replace is same as removed count,
            # but problem says remove contiguous stones and replace with stones of new color, but count is not explicitly stated.
            # Actually it says replace the removed contiguous stones with stones of the new color (same number).
            # To implement that, we need count of removed stones.
            # Implement this carefully by tracking number removed.

            # But above remove_right_blocks only removed blocks, so we lost count.

            # To do this correctly, change remove_right_blocks to return the sum of counts removed.

    # To fix above, modify remove_right_blocks to return count removed
class EnhancedStoneStack:
    def __init__(self):
        self.blocks = []

    def push(self, stone: GoStone):
        if not self.blocks or self.blocks[-1].color != stone.color:
            self.blocks.append(StoneBlock(stone.color, 1))
        else:
            self.blocks[-1].count += 1

    def right_color(self) -> int:
        if not self.blocks:
            raise RuntimeError("Stack is empty")
        return self.blocks[-1].color

    def remove_right_blocks(self, color: int) -> int:
        removed_count = 0
        while self.blocks and self.blocks[-1].color == color:
            removed_count += self.blocks[-1].count
            self.blocks.pop()
        return removed_count

    def add_block(self, color: int, count: int):
        if not self.blocks or self.blocks[-1].color != color:
            self.blocks.append(StoneBlock(color, count))
        else:
            self.blocks[-1].count += count

    def total_white_stones(self) -> int:
        return sum(block.count for block in self.blocks if block.color == GoStone.WHITE)

class SophisticatedGoTable:
    def __init__(self):
        self.stack = EnhancedStoneStack()
        self.step = 0

    def place_stone(self, color: int):
        self.step += 1
        stone = GoStone(color)

        if self.step % 2 == 1:
            # odd step no replacement
            self.stack.push(stone)
        else:
            right_color = self.stack.right_color()
            if stone.color == right_color:
                self.stack.push(stone)
            else:
                removed = self.stack.remove_right_blocks(right_color)
                # replace removed stones with stones of new color
                self.stack.add_block(stone.color, removed)
                # place the new stone at right end
                self.stack.push(stone)

    def count_white_stones(self) -> int:
        return self.stack.total_white_stones()

class InputDataParser:
    def __init__(self, input_source):
        self.input_source = input_source

    def read_dataset(self):
        n_line = self.input_source.readline()
        if not n_line:
            return None
        n_line = n_line.strip()
        if not n_line:
            return None
        n = int(n_line)
        if n == 0:
            return None
        stones = []
        for _ in range(n):
            line = self.input_source.readline()
            if not line:
                raise RuntimeError("Unexpected end of input")
            stones.append(int(line.strip()))
        return n, stones

class GoGameController:
    def __init__(self, input_source):
        self.parser = InputDataParser(input_source)
        self.tables = []

    def process_all_datasets(self):
        results = []
        while True:
            dataset = self.parser.read_dataset()
            if dataset is None:
                break
            n, stones = dataset
            table = SophisticatedGoTable()
            for color in stones:
                table.place_stone(color)
            results.append(table.count_white_stones())
        return results

def main():
    import sys
    controller = GoGameController(sys.stdin)
    results = controller.process_all_datasets()
    for res in results:
        print(res)

if __name__ == "__main__":
    main()