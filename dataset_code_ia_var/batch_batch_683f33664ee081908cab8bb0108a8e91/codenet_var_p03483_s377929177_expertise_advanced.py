from collections import Counter, defaultdict

def palindrome_min_swaps(s: str) -> int:
    n = len(s)
    counter = Counter(s)
    odd_chars = [c for c, v in counter.items() if v % 2]
    if len(odd_chars) > 1:
        return -1
    # Assign target palindrome indices
    char_indices = defaultdict(list)
    for i, c in enumerate(s):
        char_indices[c].append(i)
    memo = [None] * n
    used = defaultdict(int)
    front, back = 0, n - 1
    for c in sorted(counter, key=lambda x: (ord(x))):
        total = counter[c]
        indices = char_indices[c]
        half = total // 2
        for i in range(half):
            memo[indices[i]] = front
            memo[indices[-(i+1)]] = back
            front += 1
            back -= 1
    if odd_chars:
        odd_char = odd_chars[0]
        center = char_indices[odd_char][counter[odd_char]//2]
        memo[center] = n//2
    # BIT/Fenwick tree
    class BIT:
        __slots__ = ['size','tree']
        def __init__(self, n):
            self.size = n+2
            self.tree = [0] * self.size
        def add(self, i, x):
            i += 1
            while i < self.size:
                self.tree[i] += x
                i += i & -i
        def sum(self, i):
            i += 1
            res = 0
            while i > 0:
                res += self.tree[i]
                i -= i & -i
            return res
    ans = 0
    bit = BIT(n)
    for idx in memo:
        bit.add(idx, 1)
        ans += bit.sum(n-1) - bit.sum(idx)
    return ans

if __name__ == "__main__":
    import sys
    s = sys.stdin.readline().rstrip()
    print(palindrome_min_swaps(s))