import sys

def fast_input_line():
    return sys.stdin.readline().strip()

def create_2d_list(num_rows, num_columns, fill_value):
    return [[fill_value] * num_columns for row_index in range(num_rows)]

def create_3d_list(dim1, dim2, dim3, fill_value):
    return [[[fill_value] * dim3 for col_index in range(dim2)] for row_index in range(dim1)]

def create_4d_list(dim1, dim2, dim3, dim4, fill_value):
    return [[[[fill_value] * dim4 for d3 in range(dim3)] for d2 in range(dim2)] for d1 in range(dim1)]

def integer_ceil(numerator, denominator=1):
    return int(-(-numerator // denominator))

def read_integer():
    return int(fast_input_line())

def read_ints():
    return map(int, fast_input_line().split())

def read_integer_list(num_elements=None):
    if num_elements is None:
        return list(read_ints())
    else:
        return [read_integer() for _ in range(num_elements)]

def print_yes_lowercase():
    print('Yes')

def print_no_lowercase():
    print('No')

def print_yes_uppercase():
    print('YES')

def print_no_uppercase():
    print('NO')

sys.setrecursionlimit(10 ** 9)

INFINITY = 10 ** 18
MODULO = 10 ** 9 + 7

class MinimumCostFlowDijkstra:
    """ Minimum Cost Flow (Dijkstra type): O(F * E * logV) """

    INFINITY = 10 ** 18

    def __init__(self, num_vertices):
        self.number_of_vertices = num_vertices
        self.graph = [[] for _ in range(num_vertices)]

    def add_edge(self, from_vertex, to_vertex, capacity, cost):
        graph = self.graph
        graph[from_vertex].append([to_vertex, capacity, cost, len(graph[to_vertex])])
        # Reverse edge for residual network
        graph[to_vertex].append([from_vertex, 0, -cost, len(graph[from_vertex]) - 1])

    def minimum_cost_flow(self, source, sink, amount_flow):
        from heapq import heappush, heappop

        num_vertices = self.number_of_vertices
        graph = self.graph
        INFINITY = MinimumCostFlowDijkstra.INFINITY

        total_cost = 0
        # Potential for each vertex for reduced cost computation
        potential = [0] * num_vertices
        previous_vertex = [0] * num_vertices
        previous_edge = [0] * num_vertices

        while amount_flow:
            minimum_distances = [INFINITY] * num_vertices
            minimum_distances[source] = 0
            priority_queue = [(0, source)]

            while priority_queue:
                cost_so_far, current_vertex = heappop(priority_queue)
                if minimum_distances[current_vertex] < cost_so_far:
                    continue
                for edge_index, (next_vertex, capacity, edge_cost, _) in enumerate(graph[current_vertex]):
                    if capacity > 0 and minimum_distances[next_vertex] > minimum_distances[current_vertex] + edge_cost + potential[current_vertex] - potential[next_vertex]:
                        updated_cost = minimum_distances[current_vertex] + edge_cost + potential[current_vertex] - potential[next_vertex]
                        minimum_distances[next_vertex] = updated_cost
                        previous_vertex[next_vertex] = current_vertex
                        previous_edge[next_vertex] = edge_index
                        heappush(priority_queue, (updated_cost, next_vertex))
            if minimum_distances[sink] == INFINITY:
                return INFINITY

            for vertex_index in range(num_vertices):
                potential[vertex_index] += minimum_distances[vertex_index]

            # Find minimum residual capacity along the path from sink to source
            current_flow = amount_flow
            vertex = sink
            while vertex != source:
                prev_vertex = previous_vertex[vertex]
                prev_edge_index = previous_edge[vertex]
                current_flow = min(current_flow, graph[prev_vertex][prev_edge_index][1])
                vertex = prev_vertex

            amount_flow -= current_flow
            total_cost += current_flow * potential[sink]

            # Update the residual network
            vertex = sink
            while vertex != source:
                prev_vertex = previous_vertex[vertex]
                prev_edge_index = previous_edge[vertex]
                forward_edge = graph[prev_vertex][prev_edge_index]
                forward_edge[1] -= current_flow
                reverse_edge_index = forward_edge[3]
                graph[vertex][reverse_edge_index][1] += current_flow
                vertex = prev_vertex

        return total_cost

number_of_elements = read_integer()
permutation_elements = read_integer_list()

total_vertices = number_of_elements * 2 + 2
minimum_cost_flow_solver = MinimumCostFlowDijkstra(total_vertices)
source_vertex = number_of_elements * 2
sink_vertex = number_of_elements * 2 + 1

for original_index, element_value in enumerate(permutation_elements):
    minimum_cost_flow_solver.add_edge(source_vertex, original_index, 1, 0)
    minimum_cost_flow_solver.add_edge(number_of_elements + original_index, sink_vertex, 1, 0)
    for target_index in range(number_of_elements):
        # For derangements (no fixed points): Do not connect if position matches value
        if element_value == target_index + 1:
            continue
        assignment_cost = element_value * abs(original_index - target_index)
        minimum_cost_flow_solver.add_edge(original_index, number_of_elements + target_index, 1, assignment_cost)

minimum_cost = minimum_cost_flow_solver.minimum_cost_flow(source_vertex, sink_vertex, number_of_elements)
print(minimum_cost)