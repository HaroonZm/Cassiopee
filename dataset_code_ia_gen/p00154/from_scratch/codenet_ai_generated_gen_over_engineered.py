class CardType:
    def __init__(self, value: int, count: int):
        self.value = value
        self.count = count

    def __repr__(self):
        return f"CardType(value={self.value}, count={self.count})"

class CardBag:
    def __init__(self, card_types: list[CardType]):
        self.card_types = card_types
        self._max_sum = sum(ct.value * ct.count for ct in card_types)
        self._dp = None
        self._prepared = False

    def prepare_dp(self):
        max_sum = self._max_sum
        # dp[s] will hold the number of ways to make sum s
        dp = [0] * (max_sum + 1)
        dp[0] = 1
        for ct in self.card_types:
            value, count = ct.value, ct.count
            next_dp = dp[:]
            for used in range(1, count + 1):
                add_val = value * used
                for s in range(max_sum - add_val + 1):
                    if dp[s]:
                        next_dp[s + add_val] += dp[s]
            dp = next_dp
        self._dp = dp
        self._prepared = True

    def count_combinations(self, target: int) -> int:
        if not self._prepared:
            self.prepare_dp()
        if target > self._max_sum or target < 0:
            return 0
        return self._dp[target]

class Game:
    def __init__(self, bag: CardBag, targets: list[int]):
        self.bag = bag
        self.targets = targets
        self.results = []

    def play(self):
        for target in self.targets:
            count = self.bag.count_combinations(target)
            self.results.append(count)

    def output_results(self):
        for res in self.results:
            print(res)

class DatasetParser:
    def __init__(self):
        self.datasets = []

    def parse(self):
        import sys
        lines = sys.stdin.read().strip().split('\n')
        idx = 0
        while True:
            if idx >= len(lines):
                break
            m_line = lines[idx].strip()
            idx += 1
            if m_line == '0':
                break
            m = int(m_line)
            card_types = []
            for _ in range(m):
                a_str, b_str = lines[idx].strip().split()
                idx += 1
                card_types.append(CardType(int(a_str), int(b_str)))
            g = int(lines[idx].strip())
            idx += 1
            targets = []
            for _ in range(g):
                targets.append(int(lines[idx].strip()))
                idx += 1
            self.datasets.append((card_types, targets))

    def get_datasets(self):
        return self.datasets

class GameOrchestrator:
    def __init__(self):
        self.parser = DatasetParser()

    def run(self):
        self.parser.parse()
        for card_types, targets in self.parser.get_datasets():
            bag = CardBag(card_types)
            game = Game(bag, targets)
            game.play()
            game.output_results()

if __name__ == "__main__":
    orchestrator = GameOrchestrator()
    orchestrator.run()