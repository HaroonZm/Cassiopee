import sys
import heapq as hp

class Edge:
    def __init__(self, end, cost):
        self.to = end
        self.cost = cost

def create_empty_graph(V):
    return [[] for _ in range(V)]

def create_distance_list(V, inf):
    return [inf for _ in range(V)]

def init_infinity():
    return sys.maxsize

def push_to_queue(que, item):
    hp.heappush(que, item)

def pop_from_queue(que):
    return hp.heappop(que)

def should_continue(dist, cur_vertex, cur_cost):
    return dist[cur_vertex] < cur_cost

def update_distance_and_push(que, dist, e, cur_cost):
    dist[e.to] = cur_cost + e.cost
    push_to_queue(que, (dist[e.to], e.to))

def process_neighbors(graph, dist, cur_vertex, cur_cost, que):
    for e in graph[cur_vertex]:
        if cur_cost + e.cost < dist[e.to]:
            update_distance_and_push(que, dist, e, cur_cost)

def dijkstra_solve(graph, dist, s):
    que = []
    dist[s] = 0
    push_to_queue(que, (0, s))
    while que:
        cur_cost, cur_vertex = pop_from_queue(que)
        if should_continue(dist, cur_vertex, cur_cost):
            continue
        process_neighbors(graph, dist, cur_vertex, cur_cost, que)

def add_edge(graph, st, ed, cost):
    graph[st].append(Edge(ed, cost))

def read_initial_input():
    return map(int, input().split())

def read_edge_input():
    return map(int, input().split())

def output_result(dist, inf):
    for value in dist:
        if value == inf:
            print("INF")
        else:
            print(value)

def main():
    V, E, r = read_initial_input()
    inf = init_infinity()
    graph = create_empty_graph(V)
    dist = create_distance_list(V, inf)
    for _ in range(E):
        s, t, d = read_edge_input()
        add_edge(graph, s, t, d)
    dijkstra_solve(graph, dist, r)
    output_result(dist, inf)

if __name__ == '__main__':
    main()