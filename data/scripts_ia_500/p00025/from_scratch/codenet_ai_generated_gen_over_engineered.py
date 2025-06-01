class NumberSet:
    def __init__(self, numbers):
        if len(numbers) != 4:
            raise ValueError("Exactly four numbers are required")
        if len(set(numbers)) != 4:
            raise ValueError("Numbers must be unique")
        if any(not(0 <= n <= 9) for n in numbers):
            raise ValueError("Numbers must be between 0 and 9")
        self._numbers = tuple(numbers)

    def __getitem__(self, index):
        return self._numbers[index]

    def __contains__(self, item):
        return item in self._numbers

    def __iter__(self):
        return iter(self._numbers)

    def __len__(self):
        return len(self._numbers)


class HitBlowEvaluator:
    def __init__(self, imagined: NumberSet, guessed: NumberSet):
        self.imagined = imagined
        self.guessed = guessed

    def evaluate(self):
        hit = self._count_hits()
        blow = self._count_blows(hit)
        return hit, blow

    def _count_hits(self) -> int:
        return sum(1 for i in range(4) if self.imagined[i] == self.guessed[i])

    def _count_blows(self, hits_count: int) -> int:
        # Blow counts digits present in imagined but in different position
        imagined_set = set(self.imagined)
        guessed_set = set(self.guessed)
        common = imagined_set.intersection(guessed_set)
        total_common = len(common)
        # Blows can't include the hits, so subtract hits_count from total_common
        # But since digits are unique, total_common is number of digits common in both, hits may overlap
        # We need to count how many digits are common but not hits
        # So compute all positions which are common but not hits
        blow = total_common - hits_count
        return blow


class HitBlowGameProcessor:
    def __init__(self):
        self.datasets = []

    def add_dataset(self, imagined_nums, guessed_nums):
        imagined = NumberSet(imagined_nums)
        guessed = NumberSet(guessed_nums)
        self.datasets.append((imagined, guessed))

    def process(self):
        results = []
        for imagined, guessed in self.datasets:
            evaluator = HitBlowEvaluator(imagined, guessed)
            hit, blow = evaluator.evaluate()
            results.append((hit, blow))
        return results

import sys

class InputReader:
    def __init__(self, stream):
        self.stream = stream

    def read_datasets(self):
        datasets = []
        while True:
            line1 = self._read_non_empty_line()
            if line1 is None:
                break
            line2 = self._read_non_empty_line()
            if line2 is None:
                break
            imagined_nums = list(map(int, line1.strip().split()))
            guessed_nums = list(map(int, line2.strip().split()))
            datasets.append((imagined_nums, guessed_nums))
        return datasets

    def _read_non_empty_line(self):
        for line in self.stream:
            if line.strip():
                return line
        return None


def main():
    input_reader = InputReader(sys.stdin)
    datasets = input_reader.read_datasets()
    processor = HitBlowGameProcessor()
    for imagined, guessed in datasets:
        processor.add_dataset(imagined, guessed)
    results = processor.process()
    for hit, blow in results:
        print(hit, blow)

if __name__ == "__main__":
    main()