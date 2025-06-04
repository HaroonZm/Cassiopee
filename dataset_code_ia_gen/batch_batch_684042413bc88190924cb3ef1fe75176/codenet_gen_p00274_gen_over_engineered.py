class PrizesCollection:
    def __init__(self, prize_counts):
        self.prize_counts = prize_counts
        self.total_types = len(prize_counts)

    def is_possible(self):
        return any(count >= 2 for count in self.prize_counts)

    def minimal_attempts(self):
        if not self.is_possible():
            return None
        max_count = max(self.prize_counts)
        sum_counts = sum(self.prize_counts)

        # If there's at least one prize with count >= 2, minimal attempts calculation:
        # The worst case is to get all other prizes plus one of the duplicated prize, so minimal attempts = sum of all + 1 - max duplicated count
        # Or simply minimal attempts = total number of prizes - max count + 2, reasoning from sample outputs and problem statement.
        # But sample shows minimal attempts is sum - max_count + 2
        return sum_counts - max_count + 2

class InputParser:
    def __init__(self):
        self.datasets = []

    def parse(self, lines):
        index = 0
        while index < len(lines):
            n = int(lines[index])
            index += 1
            if n == 0:
                break
            counts = list(map(int, lines[index].split()))
            index += 1
            self.datasets.append(PrizesCollection(counts))

class OutputFormatter:
    def __init__(self):
        pass

    def format_result(self, result):
        if result is None:
            return "NA"
        else:
            return str(result)

class GachaponSolver:
    def __init__(self, data_collections):
        self.data_collections = data_collections
        self.formatter = OutputFormatter()

    def solve(self):
        results = []
        for collection in self.data_collections:
            minimal = collection.minimal_attempts()
            results.append(self.formatter.format_result(minimal))
        return results

def main():
    import sys
    lines = [line.strip() for line in sys.stdin if line.strip() != '']
    parser = InputParser()
    parser.parse(lines)
    solver = GachaponSolver(parser.datasets)
    results = solver.solve()
    for res in results:
        print(res)

if __name__ == "__main__":
    main()