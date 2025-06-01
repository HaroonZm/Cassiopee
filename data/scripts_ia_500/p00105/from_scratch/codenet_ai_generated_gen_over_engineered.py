from typing import List, Dict, Set, Tuple, Iterable
from collections import defaultdict

class PageNumber:
    def __init__(self, number: int) -> None:
        if not (0 < number <= 1000):
            raise ValueError("Page number must be between 1 and 1000")
        self.number = number

    def __lt__(self, other: 'PageNumber') -> bool:
        return self.number < other.number

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, PageNumber):
            return False
        return self.number == other.number

    def __hash__(self) -> int:
        return hash(self.number)

    def __str__(self) -> str:
        return str(self.number)

class Word:
    MAX_LENGTH = 30

    def __init__(self, text: str) -> None:
        if len(text) > self.MAX_LENGTH:
            raise ValueError(f"Word length must be at most {self.MAX_LENGTH}")
        self.text = text

    def __lt__(self, other: 'Word') -> bool:
        return self.text < other.text

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Word):
            return False
        return self.text == other.text

    def __hash__(self) -> int:
        return hash(self.text)

    def __str__(self) -> str:
        return self.text

class IndexEntry:
    def __init__(self, word: Word) -> None:
        self.word = word
        self.page_numbers: Set[PageNumber] = set()

    def add_page(self, page: PageNumber) -> None:
        self.page_numbers.add(page)

    def sorted_pages(self) -> List[PageNumber]:
        return sorted(self.page_numbers)

    def __str__(self) -> str:
        pages_str = ' '.join(str(p) for p in self.sorted_pages())
        return f"{self.word}\n{pages_str}"

class BookIndex:
    def __init__(self) -> None:
        self.entries: Dict[Word, IndexEntry] = {}

    def add_entry(self, word_str: str, page_num: int) -> None:
        word = Word(word_str)
        page = PageNumber(page_num)
        if word not in self.entries:
            self.entries[word] = IndexEntry(word)
        self.entries[word].add_page(page)

    def sorted_entries(self) -> List[IndexEntry]:
        return [self.entries[word] for word in sorted(self.entries.keys())]

    def __str__(self) -> str:
        return '\n'.join(str(entry) for entry in self.sorted_entries())

class BookIndexProcessor:
    def __init__(self, input_lines: Iterable[str]) -> None:
        self.input_lines = input_lines
        self.book_index = BookIndex()

    def process(self) -> None:
        for line in self.input_lines:
            stripped_line = line.strip()
            if not stripped_line:
                continue
            parts = stripped_line.split()
            if len(parts) != 2:
                # Ignore malformed lines
                continue
            word_str, page_str = parts
            try:
                page_num = int(page_str)
                self.book_index.add_entry(word_str, page_num)
            except ValueError:
                continue

    def output(self) -> None:
        print(self.book_index)

def main() -> None:
    import sys
    processor = BookIndexProcessor(sys.stdin)
    processor.process()
    processor.output()

if __name__ == "__main__":
    main()