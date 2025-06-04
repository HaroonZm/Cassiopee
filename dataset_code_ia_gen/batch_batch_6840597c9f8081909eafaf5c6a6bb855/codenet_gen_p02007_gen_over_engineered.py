from typing import List, Dict, Tuple, Optional
import sys
sys.setrecursionlimit(10**7)

class TrieNode:
    def __init__(self):
        # Map char to child TrieNode
        self.children: Dict[str, 'TrieNode'] = dict()
        # Sorted list of word ids passing through this node
        self.word_ids: List[int] = []

    def insert(self, word: str, word_id: int):
        node = self
        for ch in word:
            if ch not in node.children:
                node.children[ch] = TrieNode()
            node = node.children[ch]
            # Append id in a way that keeps list sorted (appending sequentially guarantees sorted)
            node.word_ids.append(word_id)

    def find_prefix_node(self, prefix: str) -> Optional['TrieNode']:
        node = self
        for ch in prefix:
            if ch not in node.children:
                return None
            node = node.children[ch]
        return node

class AbstractWordIndex:
    def __init__(self, words: List[str]):
        self.words = words
        self.n = len(words)
        self.prefix_trie = TrieNode()
        self.suffix_trie = TrieNode()
        self._build()

    def _build(self):
        raise NotImplementedError()

    def query(self, prefix: str, suffix: str) -> int:
        """
        Query the number of words with given prefix and suffix.
        """
        prefix_node = self.prefix_trie.find_prefix_node(prefix)
        if prefix_node is None:
            return 0
        suffix_node = self.suffix_trie.find_prefix_node(suffix[::-1])
        if suffix_node is None:
            return 0

        prefix_ids = prefix_node.word_ids
        suffix_ids = suffix_node.word_ids
        # intersection count using efficient two pointer
        return self._count_intersection(prefix_ids, suffix_ids)

    @staticmethod
    def _count_intersection(sorted_a: List[int], sorted_b: List[int]) -> int:
        count = 0
        i, j = 0, 0
        while i < len(sorted_a) and j < len(sorted_b):
            if sorted_a[i] == sorted_b[j]:
                count += 1
                i += 1
                j += 1
            elif sorted_a[i] < sorted_b[j]:
                i += 1
            else:
                j += 1
        return count


class PrefixSuffixSearcher(AbstractWordIndex):
    """
    Concrete implementation that builds prefix and suffix tries
    keeping track of word IDs to efficiently answer queries.
    Currently does not build additional indexes, but is ready
    for future extensions like weighted counts, fuzzy prefix/suffix etc.
    """
    def _build(self):
        for word_id, word in enumerate(self.words):
            self.prefix_trie.insert(word, word_id)
            self.suffix_trie.insert(word[::-1], word_id)


class InputParser:
    """
    Encapsulates input parsing and data preparation logic.
    Helps future extension e.g. to support multiple test cases.
    """
    def __init__(self, input_stream):
        self.input = input_stream

    def parse(self) -> Tuple[List[str], List[Tuple[str, str]]]:
        first_line = ''
        while first_line.strip() == '':
            first_line = self.input.readline()
        n, q = map(int, first_line.strip().split())
        words = []
        while len(words) < n:
            line = self.input.readline()
            if line.strip():
                words.append(line.strip())
        queries = []
        while len(queries) < q:
            line = self.input.readline()
            if line.strip():
                p, s = line.strip().split()
                queries.append((p, s))
        return words, queries


class OutputHandler:
    """
    Abstract output handler. Could be extended to support buffered output,
    output to files, or custom formatting.
    """
    def __init__(self, output_stream):
        self.output = output_stream

    def writeline(self, line: str):
        self.output.write(line + '\n')

    def writelines(self, lines: List[str]):
        for line in lines:
            self.writeline(line)


def main():
    parser = InputParser(sys.stdin)
    words, queries = parser.parse()
    searcher = PrefixSuffixSearcher(words)
    output = OutputHandler(sys.stdout)
    results = []
    for prefix, suffix in queries:
        results.append(str(searcher.query(prefix, suffix)))
    output.writelines(results)


if __name__ == "__main__":
    main()