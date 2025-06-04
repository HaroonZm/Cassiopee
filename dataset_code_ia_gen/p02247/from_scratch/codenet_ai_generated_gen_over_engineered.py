class SearchStrategy:
    def find_occurrences(self, text: str, pattern: str) -> list[int]:
        raise NotImplementedError("Subclasses should implement this!")

class NaiveSearchStrategy(SearchStrategy):
    def find_occurrences(self, text: str, pattern: str) -> list[int]:
        indices = []
        n, m = len(text), len(pattern)
        for i in range(n - m + 1):
            if self._match_at(text, pattern, i):
                indices.append(i)
        return indices
    
    def _match_at(self, text: str, pattern: str, index: int) -> bool:
        for j in range(len(pattern)):
            if text[index + j] != pattern[j]:
                return False
        return True

class SearchContext:
    def __init__(self, strategy: SearchStrategy) -> None:
        self._strategy = strategy

    def set_strategy(self, strategy: SearchStrategy) -> None:
        self._strategy = strategy

    def search(self, text: str, pattern: str) -> list[int]:
        return self._strategy.find_occurrences(text, pattern)

class InputParser:
    def __init__(self) -> None:
        self._text = ""
        self._pattern = ""
    
    def parse(self) -> tuple[str, str]:
        self._text = input().rstrip('\n')
        self._pattern = input().rstrip('\n')
        return self._text, self._pattern

class ResultRenderer:
    def render(self, indices: list[int]) -> None:
        for idx in indices:
            print(idx)

class NaiveStringSearchApp:
    def __init__(self) -> None:
        self._input_parser = InputParser()
        self._search_context = SearchContext(NaiveSearchStrategy())
        self._result_renderer = ResultRenderer()
    
    def run(self) -> None:
        text, pattern = self._input_parser.parse()
        indices = self._search_context.search(text, pattern)
        self._result_renderer.render(indices)

if __name__ == "__main__":
    NaiveStringSearchApp().run()