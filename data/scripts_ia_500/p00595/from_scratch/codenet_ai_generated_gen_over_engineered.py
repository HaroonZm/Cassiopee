class InputParser:
    def __init__(self, source):
        self.source = source

    def parse(self):
        for line in self.source:
            line = line.strip()
            if not line:
                continue
            yield tuple(map(int, line.split()))

class EuclidAlgorithm:
    @staticmethod
    def gcd(a: int, b: int) -> int:
        while b:
            a, b = b, a % b
        return a

class GCDProcessor:
    def __init__(self, parser, algorithm):
        self.parser = parser
        self.algorithm = algorithm

    def process(self):
        results = []
        for a, b in self.parser.parse():
            gcd_result = self.algorithm.gcd(a, b)
            results.append(gcd_result)
        return results

class OutputHandler:
    def __init__(self, destination):
        self.destination = destination

    def write(self, results):
        for result in results:
            print(result, file=self.destination)

if __name__ == "__main__":
    import sys
    parser = InputParser(sys.stdin)
    algorithm = EuclidAlgorithm()
    processor = GCDProcessor(parser, algorithm)
    results = processor.process()
    output_handler = OutputHandler(sys.stdout)
    output_handler.write(results)