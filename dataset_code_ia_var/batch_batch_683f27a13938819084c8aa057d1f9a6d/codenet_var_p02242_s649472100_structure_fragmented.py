import heapq
from collections import deque
from enum import Enum
import sys
import math
from _heapq import heappush, heappop

#------------------------------------------#

BIG_NUM = 2000000000
HUGE_NUM = 9999999999999999
MOD = 1000000007
EPS = 0.000000001

#------------------------------------------#

class Edge:
    def __init__(self,arg_to,arg_cost):
        self.to = arg_to
        self.cost = arg_cost

class Info:
    def __init__(self,arg_node_id,arg_sum_cost):
        self.node_id = arg_node_id
        self.sum_cost = arg_sum_cost

    def __lt__(self,arg):
        return self.sum_cost < arg.sum_cost

def read_single_int_from_input():
    return int(input())

def create_min_dist_array(V):
    return [BIG_NUM]*V

def create_graph(V):
    return [[] for _ in range(V)]

def read_line_of_ints():
    return list(map(int, input().split()))

def add_edge_to_graph(graph, node_id, table):
    for i in range(0, len(table), 2):
        append_edge(graph, node_id, table, i)

def append_edge(graph, node_id, table, i):
    edge = Edge(table[i], table[i+1])
    graph[node_id].append(edge)

def fill_graph_from_input(V, G):
    for _ in range(V):
        populate_graph_from_single_input(G)

def populate_graph_from_single_input(G):
    items = read_line_of_ints()
    node_id = items[0]
    tmp_num = items[1]
    table = items[2:]
    add_edge_to_graph(G, node_id, table)

def set_start_node_distance_to_zero(min_dist):
    min_dist[0] = 0

def create_priority_queue():
    return []

def push_initial_info(Q):
    heappush(Q, Info(0,0))

def is_empty(Q):
    return len(Q) == 0

def dijkstra(V, G, min_dist):
    Q = create_priority_queue()
    set_start_node_distance_to_zero(min_dist)
    push_initial_info(Q)
    while not is_empty(Q):
        process_queue(Q, G, min_dist)

def process_queue(Q, G, min_dist):
    info = heappop(Q)
    if should_continue(info, min_dist):
        return
    process_edges(G, info, min_dist, Q)

def should_continue(info, min_dist):
    return info.sum_cost > min_dist[info.node_id]

def process_edges(G, info, min_dist, Q):
    for edge in get_edges(G, info):
        process_single_edge(edge, info, min_dist, Q)

def get_edges(G, info):
    return G[info.node_id]

def process_single_edge(edge, info, min_dist, Q):
    if should_update_min_dist(edge, info, min_dist):
        update_min_dist(edge, info, min_dist)
        push_new_info(Q, edge, min_dist)

def should_update_min_dist(edge, info, min_dist):
    return min_dist[edge.to] > info.sum_cost + edge.cost

def update_min_dist(edge, info, min_dist):
    min_dist[edge.to] = info.sum_cost + edge.cost

def push_new_info(Q, edge, min_dist):
    heappush(Q, Info(edge.to, min_dist[edge.to]))

def print_all_distances(V, min_dist):
    for i in range(V):
        print_distance(i, min_dist)

def print_distance(i, min_dist):
    print("%d %d" % (i, min_dist[i]))

def main():
    V = read_single_int_from_input()
    min_dist = create_min_dist_array(V)
    G = create_graph(V)
    fill_graph_from_input(V, G)
    dijkstra(V, G, min_dist)
    print_all_distances(V, min_dist)

main()