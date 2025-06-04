import sys
from collections import Counter

def read_input_line(): return sys.stdin.readline().strip()
def create_2d_list(rows, cols, default_value): return [[default_value] * cols for _ in range(rows)]
def create_3d_list(x, y, z, default_value): return [[[default_value] * z for _ in range(y)] for _ in range(x)]
def create_4d_list(a, b, c, d, default_value): return [[[[default_value] * d for _ in range(c)] for _ in range(b)] for _ in range(a)]
def ceil_division(x, y=1): return int(-(-x // y))
def read_int(): return int(read_input_line())
def read_ints(): return map(int, read_input_line().split())
def read_int_list(length=None): return list(read_ints()) if length is None else [read_int() for _ in range(length)]
def print_yes(): print('Yes')
def print_no(): print('No')
def print_yes_upper(): print('YES')
def print_no_upper(): print('NO')
sys.setrecursionlimit(10 ** 9)
CONST_INF = 10 ** 18
CONST_MOD = 10 ** 9 + 7

class MaxFlowDinic:
    """ Dinic Algorithm for Maximum Flow Problem """

    VALUE_INF = 10 ** 18

    def __init__(self, vertex_count):
        self.vertex_count = vertex_count
        self.adjacent_edges = [[] for _ in range(vertex_count)]
        self.level = None
        self.iter = None

    def add_edge(self, from_vertex, to_vertex, capacity):
        self.adjacent_edges[from_vertex].append([capacity, to_vertex, len(self.adjacent_edges[to_vertex])])
        self.adjacent_edges[to_vertex].append([0, from_vertex, len(self.adjacent_edges[from_vertex]) - 1])

    def build_level(self, source_vertex):
        from collections import deque
        self.level = [-1] * self.vertex_count
        self.level[source_vertex] = 0
        queue = deque([source_vertex])
        while queue:
            current_vertex = queue.popleft()
            for capacity, to_vertex, _ in self.adjacent_edges[current_vertex]:
                if capacity > 0 and self.level[to_vertex] < 0:
                    self.level[to_vertex] = self.level[current_vertex] + 1
                    queue.append(to_vertex)

    def flow_dfs(self, current_vertex, sink_vertex, flow_limit):
        if current_vertex == sink_vertex:
            return flow_limit
        edge_list = self.adjacent_edges[current_vertex]
        while self.iter[current_vertex] < len(edge_list):
            index = self.iter[current_vertex]
            self.iter[current_vertex] += 1
            capacity, to_vertex, rev_index = edge_list[index]
            if capacity == 0 or self.level[current_vertex] >= self.level[to_vertex]:
                continue
            pushed_flow = self.flow_dfs(to_vertex, sink_vertex, min(flow_limit, capacity))
            if pushed_flow == 0:
                continue
            edge_list[index][0] -= pushed_flow
            self.adjacent_edges[to_vertex][rev_index][0] += pushed_flow
            return pushed_flow
        return 0

    def compute_max_flow(self, source_vertex, sink_vertex):
        total_flow = 0
        INF = MaxFlowDinic.VALUE_INF
        while True:
            self.build_level(source_vertex)
            if self.level[sink_vertex] < 0:
                return total_flow
            self.iter = [0] * self.vertex_count
            pushed_flow = self.flow_dfs(source_vertex, sink_vertex, INF)
            while pushed_flow > 0:
                total_flow += pushed_flow
                pushed_flow = self.flow_dfs(source_vertex, sink_vertex, INF)

def char_to_index(ch):
    return ord(ch) - ord('a')

def index_to_char(idx):
    return chr(idx + ord('a'))

word_count = read_int()
word_list = [read_input_line() for _ in range(word_count)]
ALPHABET_SIZE = 26
edge_counter = Counter()
out_degree = [0] * ALPHABET_SIZE
in_degree = [0] * ALPHABET_SIZE

for word in word_list:
    start_index = char_to_index(word[0])
    end_index = char_to_index(word[-1])
    edge_counter[(start_index, end_index)] += 1
    out_degree[start_index] += 1
    in_degree[end_index] += 1

dinic_instance = MaxFlowDinic(ALPHABET_SIZE * 2)
for from_index in range(ALPHABET_SIZE):
    dinic_instance.add_edge(from_index, ALPHABET_SIZE + from_index, CONST_INF)
    for to_index in range(ALPHABET_SIZE):
        dinic_instance.add_edge(ALPHABET_SIZE + from_index, to_index, edge_counter[(from_index, to_index)])

result_chars = []
for char_index in range(ALPHABET_SIZE):
    max_flow_value = dinic_instance.compute_max_flow(ALPHABET_SIZE + char_index, char_index)
    if in_degree[char_index] >= 1 and max_flow_value >= out_degree[char_index]:
        result_chars.append(index_to_char(char_index))
for output_char in result_chars:
    print(output_char)