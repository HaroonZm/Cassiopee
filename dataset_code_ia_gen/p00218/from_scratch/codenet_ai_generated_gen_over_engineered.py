class Score:
    def __init__(self, math: int, english: int, japanese: int):
        self.math = math
        self.english = english
        self.japanese = japanese

    def has_perfect_score(self) -> bool:
        return 100 in (self.math, self.english, self.japanese)

    def average(self) -> float:
        return (self.math + self.english + self.japanese) / 3

    def math_english_average(self) -> float:
        return (self.math + self.english) / 2


class ClassificationRule:
    def __init__(self, check_fn, level: int, class_name: str):
        self.check_fn = check_fn
        self.level = level
        self.class_name = class_name

    def matches(self, score: Score) -> bool:
        return self.check_fn(score)


class Classifier:
    def __init__(self):
        # Defined from highest level (1) to lowest
        self.rules = [
            ClassificationRule(lambda s: s.has_perfect_score(), 1, "A"),
            ClassificationRule(lambda s: s.math_english_average() >= 90, 1, "A"),
            ClassificationRule(lambda s: s.average() >= 80, 1, "A"),
            ClassificationRule(lambda s: s.average() >= 70, 2, "B"),
            ClassificationRule(lambda s: s.average() >= 50 and (s.math >= 80 or s.english >= 80), 2, "B"),
            ClassificationRule(lambda s: True, 3, "C"),
        ]

    def classify(self, score: Score) -> str:
        matched_rules = [rule for rule in self.rules if rule.matches(score)]
        best_rule = min(matched_rules, key=lambda r: r.level)
        return best_rule.class_name


class Dataset:
    def __init__(self, scores: list[Score]):
        self.scores = scores
        self.classifier = Classifier()

    def classify_all(self) -> list[str]:
        return [self.classifier.classify(score) for score in self.scores]


class InputReader:
    def __init__(self):
        pass

    def read_datasets(self) -> list[Dataset]:
        datasets = []
        while True:
            try:
                n = int(input())
            except EOFError:
                break
            if n == 0:
                break
            scores = []
            for _ in range(n):
                pm, pe, pj = map(int, input().split())
                scores.append(Score(pm, pe, pj))
            datasets.append(Dataset(scores))
        return datasets


class SolutionRunner:
    def __init__(self):
        self.reader = InputReader()

    def run(self):
        datasets = self.reader.read_datasets()
        for dataset in datasets:
            results = dataset.classify_all()
            for r in results:
                print(r)


if __name__ == "__main__":
    SolutionRunner().run()