class SubstringQuerySolver:
    class TrieNode:
        def __init__(self):
            self.children = {}
            self.positions = []

    class Trie:
        def __init__(self):
            self.root = SubstringQuerySolver.TrieNode()

        def insert(self, s, pos):
            node = self.root
            for char in s:
                if char not in node.children:
                    node.children[char] = SubstringQuerySolver.TrieNode()
                node = node.children[char]
                node.positions.append(pos)

        def find_positions(self, s):
            node = self.root
            for char in s:
                if char not in node.children:
                    return []
                node = node.children[char]
            return node.positions

    def __init__(self, S):
        self.S = S
        self.length = len(S)
        self.prefix_trie = SubstringQuerySolver.Trie()
        self.suffix_trie = SubstringQuerySolver.Trie()
        # Build prefix trie with all suffixes of S for prefix queries
        for i in range(self.length):
            self.prefix_trie.insert(self.S[i:], i)
        # Build suffix trie with all reversed prefixes of S for suffix queries
        reversed_S = self.S[::-1]
        for i in range(self.length):
            self.suffix_trie.insert(reversed_S[i:], i)

    def longest_substring_length(self, x, y):
        prefix_positions = self.prefix_trie.find_positions(x)
        if not prefix_positions:
            return 0
        reversed_y = y[::-1]
        suffix_positions = self.suffix_trie.find_positions(reversed_y)
        if not suffix_positions:
            return 0

        # suffix_positions are positions in reversed string
        # convert them back to original positions where suffix starts
        suffix_start_positions = [self.length - pos - len(y) for pos in suffix_positions]
        suffix_start_positions = [pos for pos in suffix_start_positions if 0 <= pos <= self.length - len(y)]
        if not suffix_start_positions:
            return 0

        prefix_positions.sort()
        suffix_start_positions.sort()

        max_len = 0
        # Two pointers approach to find intervals [p, s+|y|-1]
        j = 0
        slen = len(y)
        plen = len(x)
        for p in prefix_positions:
            # Move j forward while suffix_start_positions[j] < p+plen-1 (prefix substring length minimum)
            while j < len(suffix_start_positions) and suffix_start_positions[j] + slen - 1 < p + plen - 1:
                j += 1
            k = j
            # Try to find the largest s >= p with s in suffix_start_positions
            # Since suffix_start_positions sorted ascending and >= p + plen -1, check all from k to len
            while k < len(suffix_start_positions):
                s = suffix_start_positions[k]
                if s < p:
                    k += 1
                    continue
                length = s + slen - p
                if length > max_len and length <= self.length - p:
                    # Check substring S[p:p+length] starts with x and ends with y by construction of tries; no extra check needed
                    max_len = length
                k += 1

        return max_len

class QueryProcessor:
    def __init__(self, S, queries):
        self.S = S
        self.queries = queries
        self.solver = SubstringQuerySolver(S)

    def process_queries(self):
        results = []
        for x, y in self.queries:
            res = self.solver.longest_substring_length(x, y)
            results.append(res)
        return results

class InputReader:
    def __init__(self):
        self.S = None
        self.m = None
        self.queries = []

    def read_input(self):
        import sys
        self.S = sys.stdin.readline().strip()
        self.m = int(sys.stdin.readline())
        for _ in range(self.m):
            line = sys.stdin.readline().strip()
            x, y = line.split()
            self.queries.append((x, y))

class OutputWriter:
    @staticmethod
    def write_output(results):
        print('\n'.join(map(str, results)))

class Application:
    def __init__(self):
        self.reader = InputReader()
        self.processor = None

    def run(self):
        self.reader.read_input()
        self.processor = QueryProcessor(self.reader.S, self.reader.queries)
        results = self.processor.process_queries()
        OutputWriter.write_output(results)

if __name__ == '__main__':
    Application().run()