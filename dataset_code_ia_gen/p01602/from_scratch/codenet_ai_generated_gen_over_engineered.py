class BalanceString:
    class Node:
        def __init__(self, char: str, count: int):
            if char not in ('(', ')'):
                raise ValueError("Node char must be '(' or ')'")
            if count < 0:
                raise ValueError("Count must be non-negative")
            self.char = char
            self.count = count

        def __str__(self):
            return f"{self.char * self.count}"

    class AbstractSequence:
        def length(self) -> int:
            raise NotImplementedError()

        def is_balanced(self) -> bool:
            raise NotImplementedError()

        def net_balance(self) -> int:
            raise NotImplementedError()

        def min_partial_balance(self) -> int:
            raise NotImplementedError()

    class FlatSequence(AbstractSequence):
        def __init__(self, node: 'BalanceString.Node'):
            self.node = node

        def length(self) -> int:
            return self.node.count

        # net_balance: +count if '(' else -count
        def net_balance(self) -> int:
            return self.node.count if self.node.char == '(' else -self.node.count

        # minimal partial balance when traversing this sequence
        def min_partial_balance(self) -> int:
            step = 1 if self.node.char == '(' else -1
            # For a sequence of identical chars, partial sums go:
            # partial balances = [step * i for i in 1..count]
            # minimal partial balance is min among these values
            if step == 1:
                # always ≥ 1, minimal partial balance is 1
                return step
            else:
                # step = -1, partial balance goes -1, -2, ..., -count
                # minimal is -count
                return step * self.node.count

        def is_balanced(self) -> bool:
            # A sequence of only '(' or only ')' can only be balanced if count == 0 (empty)
            # since empty string is balanced, else no
            # but count>0 here always => False
            # But we never rely on is_balanced for a single node except empty, so just:
            return self.node.count == 0

        def __str__(self):
            return str(self.node)

    class CompositeSequence(AbstractSequence):
        def __init__(self, left: 'BalanceString.AbstractSequence', right: 'BalanceString.AbstractSequence'):
            self.left = left
            self.right = right

        def length(self) -> int:
            return self.left.length() + self.right.length()

        def net_balance(self) -> int:
            return self.left.net_balance() + self.right.net_balance()

        def min_partial_balance(self) -> int:
            # minimal prefix sum when concatenating left and right sequences
            # minimal of left.min_partial_balance
            # and left.net_balance + right.min_partial_balance
            left_min = self.left.min_partial_balance()
            right_min = self.right.min_partial_balance()
            combined_min = min(left_min, self.left.net_balance() + right_min)
            return combined_min

        def is_balanced(self) -> bool:
            # balanced if total net balance == 0 and minimal partial sum >= 0
            return self.net_balance() == 0 and self.min_partial_balance() >= 0

        def __str__(self):
            return str(self.left) + str(self.right)

    def __init__(self):
        self.sequence: BalanceString.AbstractSequence = self.FlatSequence(self.Node('(', 0))

    def append(self, char: str, count: int):
        if count == 0:
            return
        new_node = self.Node(char, count)
        new_seq = self.FlatSequence(new_node)
        self.sequence = self.CompositeSequence(self.sequence, new_seq)

    def is_balanced(self) -> bool:
        return self.sequence.is_balanced()

def main():
    import sys
    sys.setrecursionlimit(10**7)

    n = int(sys.stdin.readline())
    BStr = BalanceString()
    for _ in range(n):
        line = ''
        while line.strip() == '':
            line = sys.stdin.readline()
        p_i, x_i = line.strip().split()
        x_i = int(x_i)
        BStr.append(p_i, x_i)

    print("YES" if BStr.is_balanced() else "NO")

if __name__ == "__main__":
    main()