import heapq

class MinCostFlowGraph:
    def __init__(self, vertex_count=0):
        self.vertex_count = vertex_count
        self.adjacency_list = [[] for _ in range(vertex_count)]
        self.edge_list = []

    def add_edge(self, from_vertex, to_vertex, capacity, cost):
        edge_id = len(self.edge_list)
        forward_edge = self._InternalEdge(to_vertex, capacity, cost)
        backward_edge = self._InternalEdge(from_vertex, 0, -cost)
        forward_edge.reverse = backward_edge
        backward_edge.reverse = forward_edge
        self.edge_list.append(forward_edge)
        self.adjacency_list[from_vertex].append(forward_edge)
        self.adjacency_list[to_vertex].append(backward_edge)
        return edge_id

    class EdgeData:
        def __init__(self, start_vertex, end_vertex, total_capacity, current_flow, edge_cost):
            self.start_vertex = start_vertex
            self.end_vertex = end_vertex
            self.total_capacity = total_capacity
            self.current_flow = current_flow
            self.edge_cost = edge_cost

        def __iter__(self):
            yield self.start_vertex
            yield self.end_vertex
            yield self.total_capacity
            yield self.current_flow
            yield self.edge_cost

    def get_edge(self, edge_index):
        edge = self.edge_list[edge_index]
        reverse_edge = edge.reverse
        from_vertex = reverse_edge.to_vertex
        to_vertex = edge.to_vertex
        total_capacity = edge.capacity + reverse_edge.capacity
        current_flow = reverse_edge.capacity
        edge_cost = edge.cost
        return self.EdgeData(from_vertex, to_vertex, total_capacity, current_flow, edge_cost)

    def get_all_edges(self):
        return [self.get_edge(idx) for idx in range(len(self.edge_list))]

    def max_flow(self, source_vertex, sink_vertex, flow_upper_bound=float('inf')):
        return self.flow_slope(source_vertex, sink_vertex, flow_upper_bound)[-1]

    def flow_slope(self, source_vertex, sink_vertex, flow_upper_bound=float('inf')):
        heappop = heapq.heappop
        heappush = heapq.heappush
        n = self.vertex_count
        adj = self.adjacency_list
        dual_potential = [0] * n
        distance = [0] * n
        previous_vertex = [0] * n
        previous_edge = [None] * n
        visited = [False] * n
        INF = float('inf')
        total_flow = 0
        total_cost = 0
        last_added_cost = -1
        flow_cost_trace = [(total_flow, total_cost)]
        while total_flow < flow_upper_bound:
            for v_idx in range(n):
                distance[v_idx] = INF
                visited[v_idx] = False
            distance[source_vertex] = 0
            heap = [(0, source_vertex)]
            while heap:
                _, vert = heappop(heap)
                if visited[vert]:
                    continue
                visited[vert] = True
                if vert == sink_vertex:
                    break
                for edge in adj[vert]:
                    next_v = edge.to_vertex
                    if visited[next_v] or not edge.capacity:
                        continue
                    new_distance = distance[vert] + edge.cost - dual_potential[next_v] + dual_potential[vert]
                    if new_distance < distance[next_v]:
                        distance[next_v] = new_distance
                        previous_vertex[next_v] = vert
                        previous_edge[next_v] = edge
                        heappush(heap, (distance[next_v], next_v))
            else:
                break
            for v_idx in range(n):
                if visited[v_idx]:
                    dual_potential[v_idx] -= distance[sink_vertex] - distance[v_idx]
            delta = flow_upper_bound - total_flow
            v = sink_vertex
            while v != source_vertex:
                delta = min(delta, previous_edge[v].capacity)
                v = previous_vertex[v]
            v = sink_vertex
            while v != source_vertex:
                edge = previous_edge[v]
                edge.capacity -= delta
                edge.reverse.capacity += delta
                v = previous_vertex[v]
            minimum_cost = -dual_potential[source_vertex]
            total_flow += delta
            total_cost += delta * minimum_cost
            if last_added_cost == total_cost:
                flow_cost_trace[-1] = (total_flow, total_cost)
            else:
                flow_cost_trace.append((total_flow, total_cost))
            last_added_cost = total_cost
        return flow_cost_trace

    class _InternalEdge:
        def __init__(self, to_vertex, capacity, cost):
            self.to_vertex = to_vertex
            self.capacity = capacity
            self.cost = cost

n, k = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(n)]
max_value = max(cell for row in matrix for cell in row)
source = n * n
sink = source + 1
row_start = sink + 1
col_start = row_start + n
vertex_total = col_start + n
graph = MinCostFlowGraph(vertex_total)
for row_idx in range(n):
    graph.add_edge(source, row_start + row_idx, k, 0)
for row_idx in range(n):
    for col_idx in range(n):
        graph.add_edge(row_start + row_idx, row_idx * n + col_idx, 1, max_value - matrix[row_idx][col_idx])
for row_idx in range(n):
    for col_idx in range(n):
        graph.add_edge(row_idx * n + col_idx, col_start + col_idx, 1, 0)
for col_idx in range(n):
    graph.add_edge(col_start + col_idx, sink, k, 0)
graph.add_edge(source, sink, n * n, max_value)
_, min_cost_result = graph.max_flow(source, sink, n * n)
print(n * n * max_value - min_cost_result)
answer_grid = [['.'] * n for _ in range(n)]
for from_v, to_v, capacity, flow, cost in graph.get_all_edges():
    if from_v < n * n and flow:
        i, j = divmod(from_v, n)
        answer_grid[i][j] = 'X'
for row in answer_grid:
    print(''.join(row))