import sys

class BinaryIndexedTree(object):
    def __init__(self, n):
        self.size = n + 1
        self.tree = [0 for _ in range(self.size)]

    def update(self, idx, val):
        while idx < self.size:
            self.tree[idx] = self.tree[idx] + val
            idx = idx + (idx & -idx)

    def prefix_sum(self, idx):
        s = 0
        while idx > 0:
            s += self.tree[idx]
            idx -= idx & -idx
        return s

def handle_queries(bt, number_of_queries):
    counter = 0
    while counter < number_of_queries:
        inputs = sys.stdin.readline().split()
        x = int(inputs[0])
        if x == 0:
            y, z = int(inputs[1]), int(inputs[2])
            bt.update(y, z)
        else:
            left, right = int(inputs[1]), int(inputs[2])
            res = bt.prefix_sum(right) - bt.prefix_sum(left - 1)
            sys.stdout.write(str(res) + '\n')
        counter += 1

def main():
    n, q = map(int, sys.stdin.readline().split())
    bit = BinaryIndexedTree(n)
    handle_queries(bit, q)

main()