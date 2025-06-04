class Number:
    def __init__(self, value: int):
        self.value = value
    def __eq__(self, other):
        if isinstance(other, Number):
            return self.value == other.value
        return False
    def __hash__(self):
        return hash(self.value)
    def __repr__(self):
        return f"Number({self.value})"

class Player:
    def __init__(self, idx: int, numbers: list[Number]):
        self.idx = idx
        self.numbers = numbers
        self.scores = [0,0,0]
    def record_score(self, round_idx: int, score: int):
        self.scores[round_idx] = score
    def total_score(self):
        return sum(self.scores)
    def __repr__(self):
        return f"Player({self.idx}, {self.numbers}, {self.scores})"

class Round:
    def __init__(self, round_idx: int, players: list[Player]):
        self.round_idx = round_idx
        self.players = players
        self.submissions = []
        self._collect_submissions()
    def _collect_submissions(self):
        # Collect each player's number for this round
        for p in self.players:
            self.submissions.append(p.numbers[self.round_idx])
    def calculate_scores(self):
        # Count appearance of numbers
        counts = {}
        for num in self.submissions:
            counts[num] = counts.get(num, 0) + 1
        # Award points only if unique
        for p in self.players:
            num = p.numbers[self.round_idx]
            if counts[num] == 1:
                p.record_score(self.round_idx, num.value)
            else:
                p.record_score(self.round_idx, 0)

class NumberGuessGameEngine:
    def __init__(self, players: list[Player], rounds: int = 3):
        self.players = players
        self.rounds_count = rounds
        self.rounds = []
    @staticmethod
    def from_input(input_lines: list[str]) -> "NumberGuessGameEngine":
        n = int(input_lines[0].strip())
        players = []
        for i in range(n):
            nums = [Number(int(x)) for x in input_lines[i+1].strip().split()]
            players.append(Player(i+1, nums))
        return NumberGuessGameEngine(players)
    def run(self):
        for round_idx in range(self.rounds_count):
            rnd = Round(round_idx, self.players)
            rnd.calculate_scores()
            self.rounds.append(rnd)
    def results(self) -> list[int]:
        return [p.total_score() for p in self.players]

def main():
    import sys
    lines = sys.stdin.read().strip().split('\n')
    engine = NumberGuessGameEngine.from_input(lines)
    engine.run()
    for score in engine.results():
        print(score)

if __name__ == "__main__":
    main()