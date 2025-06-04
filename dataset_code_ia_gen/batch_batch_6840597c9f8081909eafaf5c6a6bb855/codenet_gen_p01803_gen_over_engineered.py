from typing import List, Optional, Dict, Set, Tuple

class AirportCodeStrategy:
    VOWELS = {'a', 'i', 'u', 'e', 'o'}

    @staticmethod
    def extract_signature(name: str) -> str:
        # Extract airport signature: first letter + letters after vowels
        result = [name[0]]
        for i in range(len(name) - 1):
            if name[i] in AirportCodeStrategy.VOWELS:
                result.append(name[i + 1])
        return ''.join(result)

class CodeAssigner:
    def __init__(self, names: List[str]):
        self.names = names
        self.signatures = [AirportCodeStrategy.extract_signature(name) for name in names]

    def can_assign_unique_codes(self, k: int) -> bool:
        codes = set()
        for s in self.signatures:
            code = s[:k] if len(s) >= k else s
            if code in codes:
                return False
            codes.add(code)
        return True

    def min_code_length(self) -> int:
        max_signature_length = max(len(s) for s in self.signatures)
        for k in range(1, max_signature_length + 1):
            if self.can_assign_unique_codes(k):
                return k
        return -1

class DatasetProcessor:
    def __init__(self, datasets: List[List[str]]):
        self.datasets = datasets

    def process_all(self) -> List[int]:
        results = []
        for names in self.datasets:
            assigner = CodeAssigner(names)
            results.append(assigner.min_code_length())
        return results

class InputParser:
    def __init__(self, raw_input: str):
        self.raw_input = raw_input.strip().splitlines()

    def parse(self) -> List[List[str]]:
        datasets = []
        idx = 0
        while idx < len(self.raw_input):
            n = int(self.raw_input[idx])
            idx += 1
            if n == 0:
                break
            names = self.raw_input[idx: idx + n]
            idx += n
            datasets.append(names)
        return datasets

class AirportCodeSolver:
    def __init__(self, raw_input: str):
        self.raw_input = raw_input

    def solve(self) -> List[int]:
        parser = InputParser(self.raw_input)
        datasets = parser.parse()
        processor = DatasetProcessor(datasets)
        return processor.process_all()

def main():
    import sys
    raw_input = sys.stdin.read()
    solver = AirportCodeSolver(raw_input)
    results = solver.solve()
    for r in results:
        print(r)

if __name__ == "__main__":
    main()