import os
import sys

if os.getenv("LOCAL"):
    sys.stdin = open("_in.txt", "r")

sys.setrecursionlimit(10 ** 9)
CONST_FLOAT_INF = float("inf")
CONST_INT_INF = 10 ** 18
CONST_MOD = 10 ** 9 + 7
# CONST_MOD = 998244353

class DisjointSetUnion:
    def __init__(self, dsu_size=None, dsu_nodes=None):
        assert dsu_size is not None or dsu_nodes is not None
        if dsu_size is not None:
            self.parent_arr = [i for i in range(dsu_size)]
            self.rank_arr = [0 for _ in range(dsu_size)]
            self.size_arr = [1 for _ in range(dsu_size)]
        else:
            self.parent_dict = {k: k for k in dsu_nodes}
            self.rank_dict = {k: 0 for k in dsu_nodes}
            self.size_dict = {k: 1 for k in dsu_nodes}

    def find(self, id_x):
        if hasattr(self, "parent_arr"):
            if self.parent_arr[id_x] == id_x:
                return id_x
            self.parent_arr[id_x] = self.find(self.parent_arr[id_x])
            return self.parent_arr[id_x]
        else:
            if self.parent_dict[id_x] == id_x:
                return id_x
            self.parent_dict[id_x] = self.find(self.parent_dict[id_x])
            return self.parent_dict[id_x]

    def unite(self, id_x, id_y):
        x_root = self.find(id_x)
        y_root = self.find(id_y)
        if x_root == y_root:
            return
        if hasattr(self, "parent_arr"):
            if self.rank_arr[x_root] > self.rank_arr[y_root]:
                self.parent_arr[y_root] = x_root
                self.size_arr[x_root] += self.size_arr[y_root]
            else:
                self.parent_arr[x_root] = y_root
                self.size_arr[y_root] += self.size_arr[x_root]
                if self.rank_arr[x_root] == self.rank_arr[y_root]:
                    self.rank_arr[y_root] += 1
        else:
            if self.rank_dict[x_root] > self.rank_dict[y_root]:
                self.parent_dict[y_root] = x_root
                self.size_dict[x_root] += self.size_dict[y_root]
            else:
                self.parent_dict[x_root] = y_root
                self.size_dict[y_root] += self.size_dict[x_root]
                if self.rank_dict[x_root] == self.rank_dict[y_root]:
                    self.rank_dict[y_root] += 1

    def component_size(self, id_x):
        if hasattr(self, "size_arr"):
            return self.size_arr[self.find(id_x)]
        else:
            return self.size_dict[self.find(id_x)]

def get_argsort(seq, key_func=None, is_reverse=False):
    return [
        i for _, i in sorted(
            ((a, i) for i, a in enumerate(seq)),
            key=(lambda t: key_func(t[0])) if key_func else None,
            reverse=is_reverse
        )
    ]

vertex_count, edge_count = list(map(int, sys.stdin.buffer.readline().split()))
columns_a, columns_b = list(zip(*[map(int, sys.stdin.buffer.readline().split()) for _ in range(vertex_count)]))
edge_list = [list(map(int, sys.stdin.buffer.readline().split())) for _ in range(edge_count)]

adjacency_list = [[] for _ in range(vertex_count)]
for node_u, node_v in edge_list:
    node_u -= 1
    node_v -= 1
    adjacency_list[node_u].append(node_v)
    adjacency_list[node_v].append(node_u)

requirement_arr = [max(a, b) for a, b in zip(columns_a, columns_b)]
used_arr = list(columns_b)

sort_indices = get_argsort([a - b for a, b in zip(columns_a, columns_b)])
dsu = DisjointSetUnion(dsu_size=vertex_count)
visited_arr = [False] * vertex_count
answer_arr = [CONST_FLOAT_INF] * vertex_count
for idx_v in sort_indices:
    visited_arr[idx_v] = True
    root_set = set()
    for adj_node in adjacency_list[idx_v]:
        if not visited_arr[adj_node]:
            continue
        root_set.add(dsu.find(adj_node))
    used_total = used_arr[idx_v]
    for component_root in root_set:
        used_total += used_arr[component_root]

    requirement_v = requirement_arr[idx_v] + used_total - used_arr[idx_v]
    for component_root in root_set:
        requirement_v = min(
            requirement_v,
            max(requirement_arr[component_root], requirement_arr[idx_v] - used_arr[idx_v]) + used_total - used_arr[component_root]
        )

    for component_root in root_set:
        dsu.unite(idx_v, component_root)
    parent_root = dsu.find(idx_v)
    requirement_arr[parent_root] = requirement_v
    used_arr[parent_root] = used_total
final_answer = requirement_arr[dsu.find(0)]
print(final_answer)