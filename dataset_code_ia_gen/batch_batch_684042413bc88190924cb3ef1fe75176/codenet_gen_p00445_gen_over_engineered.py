from abc import ABC, abstractmethod
from typing import List, Tuple, Iterator

class StringSource(ABC):
    @abstractmethod
    def __iter__(self) -> Iterator[str]:
        pass

class StdInStringSource(StringSource):
    def __iter__(self) -> Iterator[str]:
        import sys
        for line in sys.stdin:
            line = line.strip()
            if line:
                yield line

class PatternMatcher(ABC):
    @abstractmethod
    def count_patterns(self, s: str) -> Tuple[int, int]:
        pass

class JOIIOIPatternMatcher(PatternMatcher):
    def __init__(self, patterns: List[str] = ["JOI", "IOI"]):
        self.patterns = patterns

    def count_patterns(self, s: str) -> Tuple[int, int]:
        counts = {pattern: 0 for pattern in self.patterns}
        length = len(s)
        for i in range(length - 2):
            substring = s[i:i+3]
            if substring in counts:
                counts[substring] += 1
        return counts["JOI"], counts["IOI"]

class Processor:
    def __init__(self, source: StringSource, matcher: PatternMatcher):
        self.source = source
        self.matcher = matcher

    def process(self) -> List[Tuple[int, int]]:
        results = []
        for line in self._limited_datasets(self.source, limit=5):
            joi_count, ioi_count = self.matcher.count_patterns(line)
            results.append((joi_count, ioi_count))
        return results

    @staticmethod
    def _limited_datasets(source: StringSource, limit: int) -> Iterator[str]:
        count = 0
        for line in source:
            if count >= limit:
                break
            yield line
            count += 1

class OutputRenderer:
    def __init__(self, results: List[Tuple[int, int]]):
        self.results = results

    def render(self):
        for joi_count, ioi_count in self.results:
            print(joi_count)
            print(ioi_count)

def main():
    source = StdInStringSource()
    matcher = JOIIOIPatternMatcher()
    processor = Processor(source, matcher)
    results = processor.process()
    renderer = OutputRenderer(results)
    renderer.render()

if __name__ == "__main__":
    main()