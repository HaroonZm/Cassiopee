import sys
sys.setrecursionlimit(10**7)
input = sys.stdin.readline

class SegmentTree:
    def __init__(self, data):
        n = len(data)
        self.n = 1
        while self.n < n:
            self.n <<= 1
        # Initialize tree with infinities
        self.data = [float('inf')] * (2 * self.n)
        # Build the tree
        for i in range(n):
            self.data[self.n + i] = data[i]
        for i in range(self.n - 1, 0, -1):
            self.data[i] = min(self.data[2*i], self.data[2*i+1])
    
    def update(self, idx, val):
        # Update value at position idx
        idx += self.n
        self.data[idx] = val
        idx >>= 1
        while idx > 0:
            self.data[idx] = min(self.data[2*idx], self.data[2*idx+1])
            idx >>= 1
    
    def query(self, l, r):
        # Query min value in [l, r]
        l += self.n
        r += self.n
        res = float('inf')
        while l <= r:
            if (l & 1) == 1:
                res = min(res, self.data[l])
                l += 1
            if (r & 1) == 0:
                res = min(res, self.data[r])
                r -= 1
            l >>= 1
            r >>= 1
        return res

def main():
    n, q = map(int, input().split())
    a = [int(input()) for _ in range(n)]
    seg = SegmentTree(a)
    a_list = a  # We'll keep array for shifting and updating
    
    for _ in range(q):
        x, y, z = map(int, input().split())
        if x == 0:
            # Circular shift from l=y to r=z
            l, r = y, z
            # Save last element in range
            last_val = a_list[r]
            # Shift elements to the right by one
            for i in range(r, l, -1):
                a_list[i] = a_list[i-1]
                seg.update(i, a_list[i])
            a_list[l] = last_val
            seg.update(l, last_val)
        elif x == 1:
            # Query min in [l=y, r=z]
            l, r = y, z
            res = seg.query(l, r)
            print(res)
        else:
            # Update pos=y with val=z
            pos, val = y, z
            a_list[pos] = val
            seg.update(pos, val)

if __name__ == "__main__":
    main()