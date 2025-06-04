class Block:
    def __init__(self, length: int, width: int, height: int):
        self.length = length  # Always 1
        self.width = width
        self.height = height

    def base_area(self):
        # Base area for sorting/stability check (length * width)
        return self.length * self.width

    def __repr__(self):
        return f"Block(l={self.length}, w={self.width}, h={self.height})"


class TowerBuilder:
    def __init__(self, blocks):
        self.blocks = blocks
        self.memo = {}

    def max_height(self) -> int:
        # Preprocessing blocks: as length is always 1, order by width descending
        # to try put bigger width blocks at bottom
        sorted_blocks = sorted(self.blocks, key=lambda b: b.width, reverse=True)
        return self._compute_max_height(sorted_blocks)

    def _compute_max_height(self, blocks):
        n = len(blocks)
        dp = [0] * n

        # Compute max height tower with block i at the bottom
        for i in range(n):
            dp[i] = blocks[i].height

        for i in range(n):
            for j in range(i):
                # Strictly decreasing width for upper block
                if blocks[i].width < blocks[j].width:
                    dp[i] = max(dp[i], dp[j] + blocks[i].height)
        return max(dp) if dp else 0


class InputParser:
    def __init__(self, raw_input):
        self.raw_input = raw_input.strip().split('\n')
        self.index = 0

    def read_int(self):
        val = int(self.raw_input[self.index])
        self.index += 1
        return val

    def read_ints(self):
        vals = list(map(int, self.raw_input[self.index].split()))
        self.index += 1
        return vals


class DangerousTowerSolver:
    def __init__(self, input_lines):
        self.parser = InputParser(input_lines)
        self.blocks = []

    def parse_input(self):
        n = self.parser.read_int()
        for _ in range(n):
            a, b = self.parser.read_ints()
            # length is fixed to 1, A_i is width, B_i is height (or vice versa)
            block = Block(length=1, width=a, height=b)
            self.blocks.append(block)

    def solve(self):
        self.parse_input()
        builder = TowerBuilder(self.blocks)
        ans = builder.max_height()
        print(ans)


def main():
    import sys
    solver = DangerousTowerSolver(sys.stdin.read())
    solver.solve()


if __name__ == "__main__":
    main()