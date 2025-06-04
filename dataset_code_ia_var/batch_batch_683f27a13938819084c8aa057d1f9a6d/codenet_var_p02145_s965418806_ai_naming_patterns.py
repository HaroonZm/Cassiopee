import sys
import re
from collections import deque, defaultdict, Counter
from math import ceil, sqrt, hypot, factorial, pi, sin, cos, radians
from itertools import accumulate, permutations, combinations, product, groupby, combinations_with_replacement
from operator import itemgetter, mul
from copy import deepcopy
from string import ascii_lowercase as CHR_LOWER_ALPHA, ascii_uppercase as CHR_UPPER_ALPHA, digits as CHR_DIGIT
from bisect import bisect as bin_search_right, bisect_left as bin_search_left
from fractions import gcd as frac_gcd
from heapq import heappush as heap_push, heappop as heap_pop
from functools import reduce as func_reduce

def get_input_line(): return sys.stdin.readline().strip()
def parse_int(): return int(get_input_line())
def parse_ints(): return map(int, get_input_line().split())
def parse_int_list(): return list(map(int, get_input_line().split()))
def zip_input(n): return zip(*(parse_ints() for _ in range(n)))

sys.setrecursionlimit(10 ** 9)
CONST_INF = 10**10
CONST_MOD = 10 ** 9 + 7

class DinicFlow:
    def __init__(self, num_vertex, inf_capacity=CONST_INF):
        self.num_vertex = num_vertex
        self.inf_capacity = inf_capacity
        self.graph_adj = [[] for _ in range(num_vertex)]
        self.depth_level = [-1]*num_vertex
        self.cur_edge_idx = [0]*num_vertex

    def add_edge(self, vertex_from, vertex_to, capacity):
        self.graph_adj[vertex_from].append([vertex_to, capacity, len(self.graph_adj[vertex_to])])
        self.graph_adj[vertex_to].append([vertex_from, 0, len(self.graph_adj[vertex_from])-1])

    def build_level_bfs(self, source):
        self.depth_level = [-1]*self.num_vertex
        self.depth_level[source] = 0
        queue = deque()
        queue.append(source)
        while queue:
            present_vertex = queue.popleft()
            for edge_idx in range(len(self.graph_adj[present_vertex])):
                v_to, cap, reverse_idx = self.graph_adj[present_vertex][edge_idx]
                if cap > 0 and self.depth_level[v_to] < 0:
                    self.depth_level[v_to] = self.depth_level[present_vertex] + 1
                    queue.append(v_to)

    def find_augmenting_dfs(self, vertex, sink, flow):
        if vertex == sink:
            return flow
        for edge_idx in range(self.cur_edge_idx[vertex], len(self.graph_adj[vertex])):
            self.cur_edge_idx[vertex] = edge_idx
            v_to, cap, reverse_idx = self.graph_adj[vertex][edge_idx]
            if cap > 0 and self.depth_level[vertex] < self.depth_level[v_to]:
                pushed_flow = self.find_augmenting_dfs(v_to, sink, min(flow, cap))
                if pushed_flow > 0:
                    self.graph_adj[vertex][edge_idx][1] -= pushed_flow
                    self.graph_adj[v_to][reverse_idx][1] += pushed_flow
                    return pushed_flow
        return 0

    def calc_max_flow(self, source, sink):
        total_flow = 0
        while True:
            self.build_level_bfs(source)
            if self.depth_level[sink] < 0:
                return total_flow
            self.cur_edge_idx = [0]*self.num_vertex
            augment_flow = self.find_augmenting_dfs(source, sink, self.inf_capacity)
            while augment_flow > 0:
                total_flow += augment_flow
                augment_flow = self.find_augmenting_dfs(source, sink, self.inf_capacity)

def char_to_index(c):
    return ord(c) - ord('a')

word_count = parse_int()
word_list = [get_input_line() for _ in range(word_count)]

result_letters = []
for idx_letter in range(len(CHR_LOWER_ALPHA)):
    node_count = len(CHR_LOWER_ALPHA) + 2
    dinic_solver = DinicFlow(node_count)
    src_node = 26
    sink_node = src_node + 1

    deg_in_cnt = 0
    deg_out_cnt = 0

    for word in word_list:
        first_idx = char_to_index(word[0])
        last_idx = char_to_index(word[-1])
        u_idx = first_idx
        v_idx = last_idx
        if first_idx == idx_letter:
            u_idx = src_node
            deg_out_cnt += 1
        if last_idx == idx_letter:
            v_idx = sink_node
            deg_in_cnt += 1

        dinic_solver.add_edge(u_idx, v_idx, 1)

    max_flow = dinic_solver.calc_max_flow(src_node, sink_node)
    if max_flow >= deg_out_cnt and deg_in_cnt > 0:
        result_letters.append(CHR_LOWER_ALPHA[idx_letter])

print(*result_letters, sep="\n")