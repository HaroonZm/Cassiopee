from typing import List, Tuple, Dict
from collections import defaultdict
import sys

class PurchaseRecord:
    def __init__(self, items: List[str]):
        self.items = items

    @classmethod
    def from_input_line(cls, line: str) -> 'PurchaseRecord':
        parts = line.strip().split()
        m = int(parts[0])
        items = parts[1:]
        if len(items) != m:
            raise ValueError("Mismatch between declared count and items count")
        return cls(items)

class PairFrequencyCounter:
    def __init__(self):
        self.frequency_map: Dict[Tuple[str, str], int] = defaultdict(int)

    def add_purchase_record(self, record: PurchaseRecord):
        sorted_items = sorted(record.items)
        n = len(sorted_items)
        for i in range(n):
            for j in range(i+1, n):
                pair = (sorted_items[i], sorted_items[j])
                self.frequency_map[pair] += 1

    def get_frequent_pairs(self, threshold: int) -> List[Tuple[str,str]]:
        result = [pair for pair, count in self.frequency_map.items() if count >= threshold]
        # sort primarily by first item, secondarily by second item lexicographically
        result.sort()
        return result

class RelatedProductsAnalyzer:
    def __init__(self, threshold: int):
        self.threshold = threshold
        self.counter = PairFrequencyCounter()

    def analyze(self, purchase_records: List[PurchaseRecord]) -> List[Tuple[str,str]]:
        for record in purchase_records:
            self.counter.add_purchase_record(record)
        return self.counter.get_frequent_pairs(self.threshold)

class InputOutputHandler:
    def __init__(self):
        self.purchase_records: List[PurchaseRecord] = []
        self.threshold = 0

    def read_input(self):
        first_line = sys.stdin.readline()
        if not first_line:
            raise EOFError("No input provided")
        parts = first_line.strip().split()
        if len(parts) != 2:
            raise ValueError("First line must contain two integers")
        N, F = map(int, parts)
        self.threshold = F
        for _ in range(N):
            line = sys.stdin.readline()
            if not line:
                raise EOFError("Not enough purchase records")
            record = PurchaseRecord.from_input_line(line)
            self.purchase_records.append(record)

    def output_results(self, pairs: List[Tuple[str,str]]):
        print(len(pairs))
        for a, b in pairs:
            print(a, b)

def main():
    ioh = InputOutputHandler()
    ioh.read_input()
    analyzer = RelatedProductsAnalyzer(ioh.threshold)
    result = analyzer.analyze(ioh.purchase_records)
    ioh.output_results(result)

if __name__ == '__main__':
    main()