class Word:
    def __init__(self, text: str):
        self.text = text

    def is_prefix_of(self, other: 'Word') -> bool:
        return other.text.startswith(self.text)

    def __lt__(self, other: 'Word') -> bool:
        # If self is prefix of other, then self < other
        if self.is_prefix_of(other):
            return True
        # If other is prefix of self, then self is not less than other
        if other.is_prefix_of(self):
            return False
        # Otherwise lexicographical comparison
        return self.text < other.text

    def __eq__(self, other: 'Word') -> bool:
        return self.text == other.text


class Dataset:
    def __init__(self, words: list):
        # Store list of Word objects
        self.words = [Word(w) for w in words]

    def check_lex_order(self) -> bool:
        # Check that words[i] < words[i+1] or words[i] == words[i+1]
        # according to lexicographical order with prefix rule
        n = len(self.words)
        for i in range(n - 1):
            w1 = self.words[i]
            w2 = self.words[i + 1]
            if not (w1 < w2 or w1 == w2):
                return False
        return True


class InputParser:
    def __init__(self):
        self.datasets = []

    def parse(self):
        while True:
            try:
                n = input().strip()
                if n == '0':
                    break
                n = int(n)
                words = [input().strip() for _ in range(n)]
                self.datasets.append(Dataset(words))
            except EOFError:
                break


class OutputWriter:
    @staticmethod
    def write_results(results: list):
        for res in results:
            print("yes" if res else "no")


class LexOrderJudge:
    def __init__(self, datasets: list):
        self.datasets = datasets

    def process(self):
        results = []
        for dataset in self.datasets:
            results.append(dataset.check_lex_order())
        return results


def main():
    parser = InputParser()
    parser.parse()
    judge = LexOrderJudge(parser.datasets)
    results = judge.process()
    OutputWriter.write_results(results)


if __name__ == "__main__":
    main()