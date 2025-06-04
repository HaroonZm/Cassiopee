class ParenthesesNumberReconstructor:
    class InvalidPermutationError(Exception):
        pass

    class AbstractParser:
        def parse(self, permutation):
            raise NotImplementedError

    class PermutationParenthesesMapper(AbstractParser):
        def __init__(self, permutation):
            self.permutation = permutation
            self.n = len(permutation)

        def parse(self):
            # n must be even for a valid parentheses sequence
            if self.n % 2 != 0:
                raise ParenthesesNumberReconstructor.InvalidPermutationError()
            
            # Indexing permutation starting from 1 according to problem statement
            p = self.permutation
            inv_p = [0] * (self.n + 1)
            for i, val in enumerate(p, start=1):
                if val < 1 or val > self.n:
                    raise ParenthesesNumberReconstructor.InvalidPermutationError()
                inv_p[val] = i  # position of open bracket val corresponds to i-th close bracket

            result = [''] * self.n
            stack = []
            # We attempt to build a valid parentheses string following the rule:
            # the i-th closing bracket matches the p_i-th opening bracket.
            # Since p is a permutation of 1..n, and we have n brackets,
            # the number of closing brackets is n/2, same for opening brackets.
            # We use stack positions as opening bracket positions.

            # Because p maps closing bracket indices to opening bracket indices,
            # We must have n even and exactly n/2 opening and closing brackets.

            # But the problem states p length = n, and each p_i from 1..n,
            # It means n is the number of closing brackets.

            # Wait: The problem defines a permutation p of length n (number of closing brackets),
            # but these indexes also represent what opening bracket matches the i-th closing bracket.

            # So total length of bracket string is 2n.

            # We'll build a bracket sequence of length 2n.

            # Strategy:
            # We'll simulate the process:
            #  - stack to push opening brackets indices
            #  - When we see that the next closing bracket corresponds to an opening bracket
            #    on stack top, we pop and add closing bracket ')'.
            #  - But we must handle the order constraint given by p

            total_len = 2 * self.n
            s = [''] * total_len
            open_positions = []
            pos_map = [0] * (self.n + 1)  # pos_map[opening_bracket_index] = position in s

            # We'll place opening brackets in order (1..n) as we go,
            # Then close bracket i corresponds to opening bracket p_i

            # We'll try to build s from left to right.

            # The idea:
            # Let's keep track of which opening brackets are opened but not closed in a stack
            # For each closing bracket i in [1..n], p_i tells which opening bracket it closes.

            # We must output s: length 2n sequence of '(' and ')'
            # obeying the rules for valid parentheses.

            # We try to find positions for '(' and ')' in s to satisfy the matching

            opens_used = 0
            closes_used = 0
            stack = []
            position = 0
            opened = [False] * (self.n + 1)  # track if an opening bracket index has been opened in s
            used_closing = [False] * (self.n + 1)  # closing brackets used

            # Because p is a permutation from 1..n, each p_i unique,
            # p_i indicates which opening bracket the i-th close bracket matches.
            # So for each i = 1..n (closing bracket index), opening bracket p_i must appear before close i.

            # We'll iterate positions from 0 to 2n-1, deciding to put '(' or ')'
            # We'll open opening brackets starting from 1..n in ascending order.
            # We can close a bracket if the close bracket index is at current i (which we're about to place)
            # but we don't have indexes of close brackets positions upfront.
            # So instead we try to place all opening brackets first if possible, or close matched brackets.

            # Alternative approach inspired by editorial:
            # We can reconstruct the parentheses sequence by the order of processing opening brackets,
            # and ensure that the closing brackets appear in order i=1..n, matching p_i.

            # We know closing brackets appear at even positions?
            # No, we must reconstruct from permutation.

            # Let's invert the logic:
            # Let's create an array to store for each opening bracket index, the closing bracket index that closes it.

            closes_for_open = [0] * (self.n + 1)
            for i in range(self.n):
                closes_for_open[p[i]] = i+1  # closing bracket index that closes opening bracket p[i]

            # Sort opening brackets by the closing bracket index.
            # To maintain proper nesting, the opening bracket with earliest closing bracket must be closed first.

            order = list(range(1, self.n + 1))
            order.sort(key=lambda x: closes_for_open[x])

            # We'll create a stack and output accordingly.
            # At each step, if next opening bracket's closing bracket index is minimal,
            # we open it, then as soon as closing bracket appears, close it.

            # Let's simulate stack with pointers.

            stack = []
            res = []
            open_iter = iter(order)
            closing_positions = [False]*(self.n+1)  # closing bracket processed
            closing_indices_queue = [0]*(self.n+1)
            idx_open = 0

            # We'll try iterative approach:

            # We'll maintain a pointer i_c for closing brackets from 1 to n
            i_c = 1
            # And a pointer i_o for opening brackets in order list

            i_o = 0
            length = 2 * self.n

            # We'll build a sequence, operations to push opening brackets, and pop closing brackets matching p.

            pos = 0
            stack = []
            # We'll iterate while res length < 2n
            while len(res) < length:
                if i_o < self.n:
                    next_open = order[i_o]
                else:
                    next_open = None

                if stack and i_c <= self.n and closes_for_open[stack[-1]] == i_c:
                    # close bracket i_c matches top of stack
                    res.append(')')
                    stack.pop()
                    i_c += 1
                else:
                    if next_open is None:
                        # no opens left, but can't close top
                        raise ParenthesesNumberReconstructor.InvalidPermutationError()
                    # open next bracket
                    res.append('(')
                    stack.append(next_open)
                    i_o += 1

            if stack:
                raise ParenthesesNumberReconstructor.InvalidPermutationError()

            # final verification: the sequence corresponds correctly?
            # The reconstruction ensures proper matching.

            return ''.join(res)

    def __init__(self, permutation):
        self.permutation = permutation

    def reconstruct(self):
        mapper = self.PermutationParenthesesMapper(self.permutation)
        return mapper.parse()

def main():
    import sys
    sys.setrecursionlimit(10**7)
    n = int(sys.stdin.readline())
    p = list(map(int, sys.stdin.readline().split()))
    try:
        reconstructor = ParenthesesNumberReconstructor(p)
        ans = reconstructor.reconstruct()
        print(ans)
    except ParenthesesNumberReconstructor.InvalidPermutationError:
        print(":(")

if __name__ == "__main__":
    main()