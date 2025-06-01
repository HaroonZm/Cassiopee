import sys
from collections import defaultdict
from itertools import combinations
from typing import List, Tuple, Dict, Set


class PurchaseInfo:
    def __init__(self, items: List[str]):
        self.items = items

    @staticmethod
    def from_input_line(line: str) -> 'PurchaseInfo':
        parts = line.strip().split()
        m = int(parts[0])
        items = parts[1:1 + m]
        return PurchaseInfo(items)


class CoPurchaseCounter:
    def __init__(self):
        # key: (item1, item2), value: count of co-purchase
        self.co_purchase_counts: Dict[Tuple[str, str], int] = defaultdict(int)

    def add_purchase_info(self, purchase_info: PurchaseInfo):
        # Consider all pairs of items bought together without duplicates or order issues
        # Sort items lex so that pair tuples always have consistent order
        for item1, item2 in combinations(sorted(purchase_info.items), 2):
            key = (item1, item2)
            self.co_purchase_counts[key] += 1

    def filter_pairs_by_threshold(self, threshold: int) -> List[Tuple[str, str]]:
        return [pair for pair, count in self.co_purchase_counts.items() if count >= threshold]


class OutputFormatter:
    @staticmethod
    def format_output(pairs: List[Tuple[str, str]]) -> str:
        # sort pairs first by first item, then second (both lex)
        pairs_sorted = sorted(pairs, key=lambda x: (x[0], x[1]))
        lines = [str(len(pairs_sorted))]
        for item1, item2 in pairs_sorted:
            lines.append(f"{item1} {item2}")
        return "\n".join(lines)


class RelatedProductsAnalyzer:
    def __init__(self, threshold: int):
        self.threshold = threshold
        self.counter = CoPurchaseCounter()

    def process_purchase_infos(self, purchase_infos: List[PurchaseInfo]):
        for info in purchase_infos:
            self.counter.add_purchase_info(info)

    def analyze(self) -> List[Tuple[str, str]]:
        return self.counter.filter_pairs_by_threshold(self.threshold)


class InputReader:
    @staticmethod
    def read_input() -> Tuple[int, int, List[PurchaseInfo]]:
        input_lines = sys.stdin.read().strip().split("\n")
        n, f = map(int, input_lines[0].split())
        purchase_infos = []
        for i in range(1, n + 1):
            purchase_infos.append(PurchaseInfo.from_input_line(input_lines[i]))
        return n, f, purchase_infos


def main():
    n, f, purchase_infos = InputReader.read_input()
    analyzer = RelatedProductsAnalyzer(f)
    analyzer.process_purchase_infos(purchase_infos)
    pairs = analyzer.analyze()
    output = OutputFormatter.format_output(pairs)
    print(output)


if __name__ == "__main__":
    main()