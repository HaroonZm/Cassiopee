import sys
sys.setrecursionlimit(10000000)

MOD_CONST = 1001
INF_CONST = 10 ** 15

class DisjointSetUnion:
    def __init__(self, num_elements):
        self.num_elements = num_elements
        self.parent_arr = [-1] * num_elements

    def find_root(self, node_idx):
        if self.parent_arr[node_idx] < 0:
            return node_idx
        else:
            self.parent_arr[node_idx] = self.find_root(self.parent_arr[node_idx])
            return self.parent_arr[node_idx]

    def unite_sets(self, node_idx1, node_idx2):
        root1 = self.find_root(node_idx1)
        root2 = self.find_root(node_idx2)
        if root1 == root2:
            return
        if self.parent_arr[root1] > self.parent_arr[root2]:
            root1, root2 = root2, root1
        self.parent_arr[root1] += self.parent_arr[root2]
        self.parent_arr[root2] = root1

    def is_same_set(self, node_idx1, node_idx2):
        return self.find_root(node_idx1) == self.find_root(node_idx2)

    def get_group_members(self, node_idx):
        root = self.find_root(node_idx)
        return [i for i in range(self.num_elements) if self.find_root(i) == root]

    def get_group_size(self, node_idx):
        return -self.parent_arr[self.find_root(node_idx)]

    def get_all_roots(self):
        return [i for i, val in enumerate(self.parent_arr) if val < 0]

    def get_group_count(self):
        return len(self.get_all_roots())

def process_groups(vertex_count, diff_threshold, fib_sequence):
    dsu_instance = DisjointSetUnion(vertex_count)
    for idx_i in range(vertex_count):
        for idx_j in range(idx_i + 1, vertex_count):
            if abs(fib_sequence[idx_i] - fib_sequence[idx_j]) < diff_threshold:
                dsu_instance.unite_sets(idx_i, idx_j)
    group_count_result = dsu_instance.get_group_count()
    print(group_count_result)

def main_entrypoint():
    fib_sequence = [0] * 1005
    fib_sequence[0] = 2
    fib_sequence[1] = 3
    for idx in range(2, 1005):
        fib_sequence[idx] = fib_sequence[idx - 1] + fib_sequence[idx - 2]
        fib_sequence[idx] %= MOD_CONST

    while True:
        try:
            vertex_count, diff_threshold = map(int, input().split())
            process_groups(vertex_count, diff_threshold, fib_sequence)
        except:
            return

if __name__ == '__main__':
    main_entrypoint()