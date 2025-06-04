import sys
sys.setrecursionlimit(10**7)
input = sys.stdin.readline

class SegmentTreeNode:
    __slots__ = ['l', 'r', 'left', 'right', 'hash_val', 'lazy', 'length']
    def __init__(self, l, r):
        self.l = l
        self.r = r
        self.left = None
        self.right = None
        self.hash_val = 0
        self.lazy = None
        self.length = r - l + 1

class SegmentTree:
    MOD1 = 10**9 + 7
    MOD2 = 10**9 + 9
    BASE = 131

    def __init__(self, s):
        self.n = len(s)
        self.s = s
        self.pow1 = [1]*(self.n+1)
        self.pow2 = [1]*(self.n+1)
        for i in range(self.n):
            self.pow1[i+1] = self.pow1[i]*self.BASE % self.MOD1
            self.pow2[i+1] = self.pow2[i]*self.BASE % self.MOD2
        self.root = self.build(0, self.n-1)

    def calc_hash(self, c, length):
        """hash of c repeated length times"""
        val1 = (ord(c) * (self.pow1[length] -1) * pow(self.BASE-1, -1, self.MOD1)) % self.MOD1
        val2 = (ord(c) * (self.pow2[length] -1) * pow(self.BASE-1, -1, self.MOD2)) % self.MOD2
        return (val1, val2)

    def build(self, l, r):
        node = SegmentTreeNode(l, r)
        if l == r:
            val = ord(self.s[l])
            node.hash_val = (val % self.MOD1, val % self.MOD2)
            return node
        m = (l+r)//2
        node.left = self.build(l, m)
        node.right = self.build(m+1, r)
        node.hash_val = self.merge(node.left.hash_val, node.right.hash_val, node.right.length)
        return node

    def merge(self, left_hash, right_hash, right_length):
        val1 = ( (left_hash[0]*self.pow1[right_length]) + right_hash[0]) % self.MOD1
        val2 = ( (left_hash[1]*self.pow2[right_length]) + right_hash[1]) % self.MOD2
        return (val1, val2)

    def pushdown(self, node):
        if node.lazy is not None and node.left:
            c = node.lazy
            node.left.lazy = c
            node.right.lazy = c
            node.left.hash_val = self.calc_hash(c, node.left.length)
            node.right.hash_val = self.calc_hash(c, node.right.length)
            node.lazy = None

    def update(self, node, l, r, c):
        if node.r < l or node.l > r:
            return
        if l <= node.l and node.r <= r:
            node.lazy = c
            node.hash_val = self.calc_hash(c, node.length)
            return
        self.pushdown(node)
        self.update(node.left, l, r, c)
        self.update(node.right, l, r, c)
        node.hash_val = self.merge(node.left.hash_val, node.right.hash_val, node.right.length)

    def query(self, node, l, r):
        if node.r < l or node.l > r:
            return (0,0,0)  # hash 0, length 0
        if l <= node.l and node.r <= r:
            return (node.hash_val[0], node.hash_val[1], node.length)
        self.pushdown(node)
        left_hash = self.query(node.left, l, r)
        right_hash = self.query(node.right, l, r)
        if left_hash[2] == 0:
            return right_hash
        if right_hash[2] == 0:
            return left_hash
        merged = (
            (left_hash[0]*self.pow1[right_hash[2]] + right_hash[0]) % self.MOD1,
            (left_hash[1]*self.pow2[right_hash[2]] + right_hash[1]) % self.MOD2,
            left_hash[2] + right_hash[2]
        )
        return merged


def main():
    N = int(input())
    U = input().rstrip('\n')
    Q = int(input())
    st = SegmentTree(U)

    # binary search for first diff char between s1[a:b] and s2[c:d]
    def first_diff(a, b, c, d):
        length = min(b - a +1, d - c +1)
        low = 0
        high = length
        while low < high:
            mid = (low + high) // 2
            h1 = st.query(st.root, a, a+mid)
            h2 = st.query(st.root, c, c+mid)
            if h1[0] == h2[0] and h1[1] == h2[1]:
                low = mid + 1
            else:
                high = mid
        return low

    for _ in range(Q):
        line = input().split()
        if line[0] == 'set':
            x, y, z = int(line[1])-1, int(line[2])-1, line[3]
            st.update(st.root, x, y, z)
        else:
            a, b, c, d = int(line[1])-1, int(line[2])-1, int(line[3])-1, int(line[4])-1
            diff = first_diff(a, b, c, d)
            len1 = b - a + 1
            len2 = d - c + 1
            if diff == min(len1, len2):
                if len1 == len2:
                    print('e')
                elif len1 < len2:
                    print('s')
                else:
                    print('t')
            else:
                ch1 = st.query(st.root, a+diff, a+diff)
                ch2 = st.query(st.root, c+diff, c+diff)
                if ch1[0] < ch2[0]:
                    print('s')
                else:
                    print('t')

if __name__ == "__main__":
    main()