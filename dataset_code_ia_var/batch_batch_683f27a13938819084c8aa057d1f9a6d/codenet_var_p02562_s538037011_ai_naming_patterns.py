n_rows, n_assign = map(int, input().split())
cost_matrix = [list(map(int, input().split())) for row_idx in range(n_rows)]
node_count = 2 * n_rows + 2
max_cost = 10 ** 14
graph = [[] for node_idx in range(node_count)]
distances = [max_cost] * node_count
prev_vertex = [0] * node_count
prev_edge = [0] * node_count

def add_edge(from_node, to_node, capacity, cost):
    global graph
    graph[from_node].append([to_node, capacity, cost, len(graph[to_node]), 0])
    graph[to_node].append([from_node, 0, -cost, len(graph[from_node]) - 1, 0])

def min_cost_flow(source, sink, flow_amount):
    global graph, node_count, max_cost, distances, prev_vertex, prev_edge
    for node_idx in range(node_count):
        for edge_idx in range(len(graph[node_idx])):
            graph[node_idx][edge_idx][4] = 0
    total_cost = 0
    remaining_flow = flow_amount
    while remaining_flow > 0:
        distances = [max_cost] * node_count
        distances[source] = 0
        updated = True
        while updated:
            updated = False
            for node_idx in range(node_count):
                if distances[node_idx] == max_cost:
                    continue
                for edge_idx in range(len(graph[node_idx])):
                    to_node, capacity, edge_cost, rev_idx, flow_pushed = graph[node_idx][edge_idx]
                    if capacity > 0 and distances[to_node] > distances[node_idx] + edge_cost:
                        distances[to_node] = distances[node_idx] + edge_cost
                        prev_vertex[to_node] = node_idx
                        prev_edge[to_node] = edge_idx
                        updated = True
        if distances[sink] == max_cost:
            return -max_cost
        path_flow = remaining_flow
        node = sink
        while node != source:
            path_flow = min(path_flow, graph[prev_vertex[node]][prev_edge[node]][1])
            node = prev_vertex[node]
        remaining_flow -= path_flow
        total_cost += path_flow * distances[sink]
        node = sink
        while node != source:
            graph[prev_vertex[node]][prev_edge[node]][1] -= path_flow
            graph[prev_vertex[node]][prev_edge[node]][4] += path_flow
            rev = graph[prev_vertex[node]][prev_edge[node]][3]
            graph[node][rev][1] += path_flow
            graph[node][rev][4] -= path_flow
            node = prev_vertex[node]
    return total_cost

source_node = n_rows * 2
sink_node = source_node + 1
for row_idx in range(n_rows):
    add_edge(source_node, row_idx, n_assign, 0)
    add_edge(n_rows + row_idx, sink_node, n_assign, 0)
    for col_idx in range(n_rows):
        add_edge(row_idx, n_rows + col_idx, 1, 10 ** 10 - cost_matrix[row_idx][col_idx])
add_edge(source_node, sink_node, n_rows * n_assign, 10 ** 10)
print(n_rows * n_assign * 10 ** 10 - min_cost_flow(source_node, sink_node, n_rows * n_assign))
assignment_matrix = [['.'] * n_rows for i in range(n_rows)]
for row_idx in range(n_rows):
    for edge in graph[row_idx]:
        if edge[4] > 0:
            assignment_matrix[row_idx][edge[0] - n_rows] = 'X'
    print(''.join(assignment_matrix[row_idx]))