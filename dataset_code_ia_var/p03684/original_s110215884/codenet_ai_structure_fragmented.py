import array
import sys

sys.setrecursionlimit(10 ** 7)
INF = 10 ** 20
MOD = 10 ** 9 + 7

def II():
    return int(input())

def ILI():
    return list(map(int, input().split()))

def IAI(LINE):
    return [ILI() for __ in range(LINE)]

def IDI():
    return {key: value for key, value in ILI()}

def read_N():
    return II()

def read_one_point(i):
    _x, _y = ILI()
    return (i, _x), (i, _y)

def read_points(N):
    x, y = [], []
    for i in range(N):
        px, py = read_one_point(i)
        x.append(px)
        y.append(py)
    return x, y

def read():
    N = read_N()
    x, y = read_points(N)
    return N, x, y

def create_sequence(n):
    return range(n)

def array_from_range(n):
    return array.array("L", create_sequence(n))

def array_of_zeros(n):
    return array.array("L", (0 for _ in create_sequence(n)))

def get_node_indexes(number_of_nodes):
    return create_sequence(number_of_nodes)

def initialize_parents(number_of_nodes):
    return array_from_range(number_of_nodes)

def initialize_ranks(number_of_nodes):
    return array_of_zeros(number_of_nodes)

class UnionFind(object):
    def __init__(self, number_of_nodes):
        self.par = initialize_parents(number_of_nodes)
        self.rank = initialize_ranks(number_of_nodes)

    def root(self, node):
        if self.par[node] == node:
            return node
        r = self._find_root_and_compress(node)
        self.par[node] = r
        return r

    def _find_root_and_compress(self, node):
        return self.root(self.par[node])

    def in_the_same_set(self, node1, node2):
        return self.root(node1) == self.root(node2)

    def _get_roots(self, node1, node2):
        return self.root(node1), self.root(node2)

    def _update_ranks_after_union(self, x, y):
        if self.rank[x] == self.rank[y]:
            self.rank[x] += 1

    def unite(self, node1, node2):
        x, y = self._get_roots(node1, node2)
        if x == y:
            return
        elif self.rank[x] < self.rank[y]:
            self.par[x] = y
        else:
            self.par[y] = x
            self._update_ranks_after_union(x, y)

def sort_points(points):
    return sorted(points, key=lambda t: t[1])

def sort_points_in_place(points):
    points.sort(key=lambda t: t[1])

def edge_from_x_pair(x1, x2):
    return (x1[0], x2[0], x2[1] - x1[1])

def edge_from_y_pair(y1, y2):
    return (y1[0], y2[0], y2[1] - y1[1])

def add_edge(edges, e):
    edges.append(e)

def make_x_edges(edges, x, i):
    e = edge_from_x_pair(x[i], x[i+1])
    add_edge(edges, e)

def make_y_edges(edges, y, i):
    e = edge_from_y_pair(y[i], y[i+1])
    add_edge(edges, e)

def make_edges(N, x, y):
    edges = []
    sort_points_in_place(x)
    sort_points_in_place(y)
    for i in range(N-1):
        make_x_edges(edges, x, i)
        make_y_edges(edges, y, i)
    return edges

def sort_edges(edges):
    edges.sort(key=lambda e: e[2])

def build_uf(N):
    return UnionFind(N)

def should_connect(u, v, uf):
    return not uf.in_the_same_set(u, v)

def connect(u, v, uf):
    uf.unite(u, v)

def add_cost(ans, cost):
    return ans + cost

def kruskal(edges, N):
    sort_edges(edges)
    uf = build_uf(N)
    ans = 0
    for edge in edges:
        u, v, cost = edge
        if should_connect(u, v, uf):
            connect(u, v, uf)
            ans = add_cost(ans, cost)
    return ans

def solve(N, x, y):
    edges = make_edges(N, x, y)
    return kruskal(edges, N)

def print_answer(ans):
    print(ans)

def get_params():
    return read()

def execute():
    params = get_params()
    answer = solve(*params)
    print_answer(answer)

def main():
    execute()

if __name__ == "__main__":
    main()