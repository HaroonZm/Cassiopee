class Score:
    def __init__(self, value: int):
        if not (0 <= value <= 1000):
            raise ValueError("Score must be between 0 and 1000")
        self.value = value

    def __lt__(self, other: 'Score') -> bool:
        return self.value < other.value

    def __le__(self, other: 'Score') -> bool:
        return self.value <= other.value

    def __eq__(self, other: 'Score') -> bool:
        return self.value == other.value

    def __repr__(self):
        return f"Score({self.value})"


class JudgeCollection:
    def __init__(self):
        self.scores = []

    def add_score(self, score: Score):
        self.scores.append(score)

    def validate(self):
        n = len(self.scores)
        if not (3 <= n <= 100):
            raise ValueError("Number of judges must be between 3 and 100")
        for s in self.scores:
            if not (0 <= s.value <= 1000):
                raise ValueError("Scores must be between 0 and 1000")

    def compute_final_score(self) -> int:
        self.validate()
        sorted_scores = sorted(self.scores, key=lambda s: s.value)
        # Remove exactly one minimum and one maximum score, even if duplicates.
        trimmed_scores = sorted_scores[1:-1]
        if not trimmed_scores:
            # If after trimming there's no score left, return 0 as safe fallback
            return 0
        total = sum(s.value for s in trimmed_scores)
        avg = total // len(trimmed_scores)  # truncated down
        return avg


class ICPCScoreProcessor:
    def __init__(self):
        self.datasets = []

    def parse_input(self, lines):
        """
        lines: iterable of strings containing the input lines,
        ending with '0' line which signals the end of all datasets
        """
        lines_iter = iter(lines)
        while True:
            try:
                n_line = next(lines_iter).strip()
                if n_line == '0':
                    break
                n = int(n_line)
                collection = JudgeCollection()
                for _ in range(n):
                    score_line = next(lines_iter).strip()
                    score = Score(int(score_line))
                    collection.add_score(score)
                self.datasets.append(collection)
            except StopIteration:
                # Unexpected EOF
                break

    def process(self):
        results = []
        for dataset in self.datasets:
            score = dataset.compute_final_score()
            results.append(score)
        return results


def main():
    import sys
    processor = ICPCScoreProcessor()
    processor.parse_input(sys.stdin)
    results = processor.process()
    for r in results:
        print(r)


if __name__ == "__main__":
    main()