class ScoreDataset:
    def __init__(self, num_students: int, num_subjects: int, scores_matrix: list[list[int]]):
        self.num_students = num_students
        self.num_subjects = num_subjects
        self.scores_matrix = scores_matrix  # m rows, each with n scores

    def total_scores_per_student(self) -> list[int]:
        totals = [0] * self.num_students
        for subject_scores in self.scores_matrix:
            for i, score in enumerate(subject_scores):
                totals[i] += score
        return totals

    def max_total_score(self) -> int:
        return max(self.total_scores_per_student()) if self.num_students > 0 else 0


class ScoreDatasetParser:
    def __init__(self, input_provider):
        self.input_provider = input_provider

    def parse_next_dataset(self) -> ScoreDataset | None:
        line = self.input_provider()
        if line is None:
            return None
        n_m = line.strip().split()
        if len(n_m) != 2:
            return None
        n, m = map(int, n_m)
        if n == 0 and m == 0:
            return None
        scores_matrix = []
        for _ in range(m):
            while True:
                line_scores = self.input_provider()
                if line_scores is None:
                    return None
                scores = list(map(int, line_scores.strip().split()))
                if len(scores) == n:
                    scores_matrix.append(scores)
                    break
        return ScoreDataset(n, m, scores_matrix)


class HighScoreProcessor:
    def __init__(self, parser: ScoreDatasetParser, output_consumer):
        self.parser = parser
        self.output_consumer = output_consumer

    def process_all_datasets(self):
        while True:
            dataset = self.parser.parse_next_dataset()
            if dataset is None:
                break
            max_score = dataset.max_total_score()
            self.output_consumer(str(max_score))


def main():
    import sys
    input_lines = iter(sys.stdin.readline, '')
    def input_provider():
        try:
            return next(input_lines)
        except StopIteration:
            return None
    def output_consumer(output_str):
        print(output_str)
    parser = ScoreDatasetParser(input_provider)
    processor = HighScoreProcessor(parser, output_consumer)
    processor.process_all_datasets()

if __name__ == "__main__":
    main()