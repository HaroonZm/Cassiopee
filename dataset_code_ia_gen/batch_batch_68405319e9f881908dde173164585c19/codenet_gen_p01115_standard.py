import sys
import threading
sys.setrecursionlimit(1 << 25)


def main():
    input = sys.stdin.readline

    # Parser and evaluator that enumerates all substrings that are valid expressions and computes their values.
    # Key idea: use dynamic programming with memoization on intervals.
    # Given the huge constraints (total length up to 5*10^6) a full O(n^3) DP is impossible.
    # Instead, we leverage the grammar structure:
    # - F: a digit or a parenthesized expression
    # - T: sequence of F separated by *
    # - E: sequence of T separated by +
    #
    # We parse the expression once, build parse tree nodes with start-end indices,
    # then for each node we compute all possible values of its substrings and count how many
    # substrings with a given value exist.
    #
    # To handle substrings, we parse not only whole nodes but also sub-nodes representing substrings.
    #
    # But enumerating all substrings and their values is impossible due to problem size.
    #
    # Hence, the problem is known as counting substrings that are valid expressions with value n.
    # The grammar is unambiguous and expressions correspond to unique parse trees.
    #
    # So the substrings that are valid expressions correspond exactly to nodes in the parse tree,
    # plus smaller nodes corresponding to sub-expressions (children).
    #
    # We can obtain all valid expressions substrings by enumerating all intervals corresponding to parse tree nodes.
    #
    # So the problem reduces to:
    # - Parse s into a tree of expressions where each node covers an interval [l, r)
    # - For each node, compute its value
    # - Count how many nodes have value == n
    #
    # Since nesting depth is at most 1000, the number of nodes is manageable.
    #
    # We'll implement a recursive descent parser with position indexes and gather (start, end, value) per node.
    # Then count those with value = n.
    #
    # Parentheses must be handled properly to define substrings.
    #
    # The index convention: start inclusive, end exclusive.

    s = []
    while True:
        line = sys.stdin.readline()
        if not line:
            break
        nline = line.strip()
        if not nline:
            continue
        if nline == '0':
            break
        n = int(nline)
        s_line = sys.stdin.readline().strip()
        s = s_line

        length = len(s)
        pos = 0

        # Parsing functions return (value, (start_index, end_index))
        # We'll also store all nodes with their intervals and values.
        # Decorate functions with current start position.
        # Global pos pointer to parse s.

        # We will use a class to represent the parser state.

        class Parser:
            def __init__(self, s):
                self.s = s
                self.n = len(s)
                self.pos = 0
                self.nodes = []  # tuples: (start, end, value)

            def parse_E(self):
                start = self.pos
                val, _ = self.parse_T()
                # repeat + T
                while self.pos < self.n and self.s[self.pos] == '+':
                    self.pos += 1
                    val2, _ = self.parse_T()
                    val += val2
                end = self.pos
                self.nodes.append((start, end, val))
                return val, (start, end)

            def parse_T(self):
                start = self.pos
                val, _ = self.parse_F()
                while self.pos < self.n and self.s[self.pos] == '*':
                    self.pos += 1
                    val2, _ = self.parse_F()
                    val *= val2
                end = self.pos
                self.nodes.append((start, end, val))
                return val, (start, end)

            def parse_F(self):
                start = self.pos
                c = self.s[self.pos]
                if c == '(':
                    self.pos += 1
                    val, _ = self.parse_E()
                    if self.pos >= self.n or self.s[self.pos] != ')':
                        # invalid but input conforms, so ignore
                        pass
                    self.pos += 1
                    end = self.pos
                    self.nodes.append((start, end, val))
                    return val, (start, end)
                else:
                    # digit
                    val = int(c)
                    self.pos += 1
                    end = self.pos
                    self.nodes.append((start, end, val))
                    return val, (start, end)

        parser = Parser(s)
        parser.parse_E()

        # Count how many nodes have value == n
        count = 0
        for st, en, val in parser.nodes:
            if val == n:
                count += 1
        print(count)


threading.Thread(target=main,).start()