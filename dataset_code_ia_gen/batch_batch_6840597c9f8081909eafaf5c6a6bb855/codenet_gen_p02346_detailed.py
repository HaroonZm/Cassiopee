import sys
input = sys.stdin.readline

class FenwickTree:
    """
    Fenwick Tree (Binary Indexed Tree) implementation for efficient prefix sums and updates.
    Supports:
      - add(idx, val): add val to element at idx
      - prefix_sum(idx): compute sum of elements from 1 to idx
    """
    def __init__(self, size):
        self.size = size
        self.tree = [0] * (size + 1)  # 1-based indexing
    
    def add(self, idx, val):
        """
        Add val to element at index idx.
        Updates all relevant nodes in Fenwick tree.
        """
        while idx <= self.size:
            self.tree[idx] += val
            idx += idx & (-idx)
    
    def prefix_sum(self, idx):
        """
        Compute sum of elements from 1 to idx.
        """
        result = 0
        while idx > 0:
            result += self.tree[idx]
            idx -= idx & (-idx)
        return result
    
    def range_sum(self, left, right):
        """
        Compute sum of elements from left to right (inclusive).
        """
        return self.prefix_sum(right) - self.prefix_sum(left - 1)

def main():
    # Read number of elements n and number of queries q
    n, q = map(int, input().split())
    
    fenw = FenwickTree(n)
    
    for _ in range(q):
        com, x, y = map(int, input().split())
        
        if com == 0:
            # add(x, y)
            fenw.add(x, y)
        else:
            # com == 1, getSum(x, y)
            # Note: x and y can be in any order, but problem constraints do not clarify
            # We assume x <= y, otherwise swap to handle range query properly
            if x > y:
                x, y = y, x
            print(fenw.range_sum(x, y))

if __name__ == "__main__":
    main()