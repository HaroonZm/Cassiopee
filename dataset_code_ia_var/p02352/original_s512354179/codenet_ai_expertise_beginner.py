from array import array

class SegmentTree:
    def __init__(self, n):
        size = 1
        while size < n:
            size *= 2
        self.n = n
        self.size = 2 * size - 1
        self.data = array('i', [0] * self.size)
        self.lazy = array('i', [0] * self.size)
        self.max_value = 1000 * 10**5 + 1

    def add(self, l, r, val):
        def update(node, node_l, node_r):
            if self.lazy[node]:
                self.data[node] += self.lazy[node]
                if node_l != node_r:
                    left = node * 2 + 1
                    right = node * 2 + 2
                    self.lazy[left] += self.lazy[node]
                    self.lazy[right] += self.lazy[node]
                self.lazy[node] = 0

            # out of range
            if node_r < l or r < node_l:
                return

            # complete overlap
            if l <= node_l and node_r <= r:
                self.data[node] += val
                if node_l != node_r:
                    left = node * 2 + 1
                    right = node * 2 + 2
                    self.lazy[left] += val
                    self.lazy[right] += val
                return

            # partial overlap
            mid = (node_l + node_r) // 2
            left = node * 2 + 1
            right = node * 2 + 2
            update(left, node_l, mid)
            update(right, mid + 1, node_r)
            self.data[node] = min(self.data[left], self.data[right])

        update(0, 0, self.size // 2)

    def min(self, l, r):
        def query(node, node_l, node_r):
            if self.lazy[node]:
                self.data[node] += self.lazy[node]
                if node_l != node_r:
                    left = node * 2 + 1
                    right = node * 2 + 2
                    self.lazy[left] += self.lazy[node]
                    self.lazy[right] += self.lazy[node]
                self.lazy[node] = 0

            # out of range
            if node_r < l or r < node_l:
                return self.max_value

            # complete overlap
            if l <= node_l and node_r <= r:
                return self.data[node]

            # partial overlap
            mid = (node_l + node_r) // 2
            left = node * 2 + 1
            right = node * 2 + 2
            left_min = query(left, node_l, mid)
            right_min = query(right, mid + 1, node_r)
            return min(left_min, right_min)

        return query(0, 0, self.size // 2)

if __name__ == "__main__":
    n, q = map(int, input().split())
    seg = SegmentTree(n)
    result = []
    for _ in range(q):
        cmd = list(map(int, input().split()))
        if cmd[0] == 0:
            seg.add(cmd[1], cmd[2], cmd[3])
        else:
            result.append(seg.min(cmd[1], cmd[2]))
    for res in result:
        print(res)