class LanguageNode:
    def __init__(self, length=0, open_count=0, close_count=0):
        self.length = length
        self.open_count = open_count
        self.close_count = close_count

    @staticmethod
    def from_char(c, count):
        if c == '(':
            # '(' contributes open count
            return LanguageNode(length=count, open_count=count, close_count=0)
        else:
            # ')' contributes close count
            return LanguageNode(length=count, open_count=0, close_count=count)

    @staticmethod
    def merge(left, right):
        # The merge logic simulates the CFG rules:
        # sum the lengths
        # match as many open from left.open_count with right.close_count
        matched = min(left.open_count, right.close_count)
        open_count = left.open_count + right.open_count - matched
        close_count = left.close_count + right.close_count - matched
        length = left.length + right.length
        return LanguageNode(length, open_count, close_count)

    def is_balanced(self):
        # The string is in the language if no unmatched opens or closes remain
        return self.open_count == 0 and self.close_count == 0


class RopeNode:
    # Abstract rope node class to allow extensions
    def length(self):
        raise NotImplementedError

    def get_language_node(self):
        raise NotImplementedError


class RopeLeaf(RopeNode):
    def __init__(self, char, count):
        self.char = char
        self.count = count
        self.lang_node = LanguageNode.from_char(char, count)

    def length(self):
        return self.count

    def get_language_node(self):
        return self.lang_node

    def split(self, pos):
        # pos < self.count
        left_count = pos
        right_count = self.count - pos
        left_leaf = RopeLeaf(self.char, left_count) if left_count > 0 else None
        right_leaf = RopeLeaf(self.char, right_count) if right_count > 0 else None
        return left_leaf, right_leaf


class RopeInternal(RopeNode):
    def __init__(self, left, right):
        self.left = left
        self.right = right
        self._length = left.length() + right.length()
        self.lang_node = LanguageNode.merge(left.get_language_node(), right.get_language_node())

    def length(self):
        return self._length

    def get_language_node(self):
        return self.lang_node


class Rope:
    def __init__(self):
        self.root = None

    def length(self):
        return self.root.length() if self.root else 0

    def concat(self, left, right):
        if left is None:
            return right
        if right is None:
            return left
        return RopeInternal(left, right)

    def split_node(self, node, pos):
        # Splits node at position pos, returns (left, right)
        # node is a RopeNode, pos is 0 <= pos <= node.length()
        if pos == 0:
            return None, node
        if pos == node.length():
            return node, None
        if isinstance(node, RopeLeaf):
            return node.split(pos)
        # node is RopeInternal
        left_len = node.left.length()
        if pos < left_len:
            left_split, left_remain = self.split_node(node.left, pos)
            right = self.concat(left_remain, node.right)
            return left_split, right
        else:
            right_split, right_remain = self.split_node(node.right, pos - left_len)
            left = self.concat(node.left, right_split)
            return left, right_remain

    def insert(self, pos, char, count):
        left, right = self.split_node(self.root, pos) if self.root else (None, None)
        middle = RopeLeaf(char, count)
        merged_left = self.concat(left, middle)
        self.root = self.concat(merged_left, right)

    def is_balanced(self):
        if self.root is None:
            return True
        return self.root.get_language_node().is_balanced()


class QueryProcessor:
    def __init__(self):
        self.rope = Rope()

    def process_query(self, p, c, n):
        self.rope.insert(p, c, n)
        return "Yes" if self.rope.is_balanced() else "No"


def main():
    import sys
    input = sys.stdin.readline
    q = int(input())
    processor = QueryProcessor()
    for _ in range(q):
        p, c, n = input().split()
        p = int(p)
        n = int(n)
        ans = processor.process_query(p, c, n)
        print(ans)


if __name__ == "__main__":
    main()