class BeatPanelGame:
    def __init__(self, n: int, c: int, lights: list[list[int]], presses: list[list[int]]):
        self.n = n
        self.c = c
        self.lights = [self._list_to_bitmask(row) for row in lights]
        self.presses = [self._list_to_bitmask(row) for row in presses]

    @staticmethod
    def _list_to_bitmask(buttons: list[int]) -> int:
        mask = 0
        for i, b in enumerate(buttons):
            if b:
                mask |= 1 << i
        return mask

    def maximize_score(self) -> int:
        from functools import lru_cache

        # dp(i, lit): max score from beat i with lit buttons bitmask
        @lru_cache(maxsize=None)
        def dp(i: int, lit: int) -> int:
            if i == self.n:
                return 0
            # update lit with new lights that turn on (or remain on if already on)
            new_lit = lit | self.lights[i]

            best = 0
            for press_mask in self.presses:
                # buttons turned off are those lit and pressed
                cleared = new_lit & press_mask
                # score is count of cleared bits + best from next step
                score = bin(cleared).count('1') + dp(i + 1, new_lit & (~cleared))
                if score > best:
                    best = score
            return best

        return dp(0, 0)


class InputParser:
    def __init__(self):
        self._input_cache = None

    def read_input(self):
        import sys
        for line in sys.stdin:
            line = line.strip()
            if not line:
                continue
            yield line

    def parse_datasets(self):
        lines = self.read_input()
        while True:
            try:
                line = next(lines)
            except StopIteration:
                break
            if line == '0 0':
                break
            n, c = map(int, line.split())
            lights = [list(map(int, next(lines).split())) for _ in range(n)]
            presses = [list(map(int, next(lines).split())) for _ in range(c)]
            yield n, c, lights, presses


class BeatPanelSolver:
    def __init__(self):
        self.parser = InputParser()

    def solve(self):
        for n, c, lights, presses in self.parser.parse_datasets():
            game = BeatPanelGame(n, c, lights, presses)
            print(game.maximize_score())


if __name__ == "__main__":
    BeatPanelSolver().solve()