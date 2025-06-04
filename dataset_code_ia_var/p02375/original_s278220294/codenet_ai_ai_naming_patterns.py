class ConsistentEdge:
    __slots__ = ('endpoint1', 'endpoint2')

    def __init__(self, endpoint1, endpoint2):
        self.endpoint1 = endpoint1
        self.endpoint2 = endpoint2

    def get_first_endpoint(self):
        return self.endpoint1

    def get_other_endpoint(self, current):
        return self.endpoint2 if current == self.endpoint1 else self.endpoint1

class ConsistentGraph:
    def __init__(self, num_vertices):
        self.vertex_count = num_vertices
        self.adjacency_lists = [[] for _ in range(num_vertices)]

    def add_edge(self, edge):
        self.adjacency_lists[edge.endpoint1].append(edge)
        self.adjacency_lists[edge.endpoint2].append(edge)

    def adjacent_edges(self, vertex):
        return self.adjacency_lists[vertex]

    def all_edges(self):
        for edge_list in self.adjacency_lists:
            for edge in edge_list:
                yield edge

class ConsistentHeavyLightDecomposition:
    class ConsistentPath:
        __slots__ = ('vertex_sequence', 'vertex_to_index')

        def __init__(self):
            self.vertex_sequence = []
            self.vertex_to_index = None

        @property
        def path_head(self):
            return self.vertex_sequence[0]

        @property
        def path_size(self):
            return len(self.vertex_sequence)

        def append_vertex(self, vertex):
            self.vertex_sequence.append(vertex)

        def get_index(self, vertex):
            if self.vertex_to_index is None:
                self.vertex_to_index = {v: i for i, v in enumerate(self.vertex_sequence)}
            return self.vertex_to_index[vertex]

        def get_next_vertex(self, vertex):
            return self.vertex_sequence[self.get_index(vertex) + 1]

    def __init__(self, graph_instance, root_vertex):
        self.vertex_to_path = {}
        self.parent_list = [root_vertex] * graph_instance.vertex_count
        self.vertex_head = [-1] * graph_instance.vertex_count
        self._decompose_paths(graph_instance, root_vertex)

    def _decompose_paths(self, graph_instance, root_vertex):
        def construct_path(vertex):
            current_path = self.ConsistentPath()
            traversal_pointer = vertex
            while traversal_pointer != -1:
                current_path.append_vertex(traversal_pointer)
                self.vertex_head[traversal_pointer] = vertex
                traversal_pointer = heavy_child[traversal_pointer]
            return current_path

        subtree_size = [1] * graph_instance.vertex_count
        max_subtree_size = [0] * graph_instance.vertex_count
        heavy_child = [-1] * graph_instance.vertex_count
        visit_status = [False] * graph_instance.vertex_count

        traversal_stack = [root_vertex]
        while traversal_stack:
            current_vertex = traversal_stack.pop()
            if not visit_status[current_vertex]:
                visit_status[current_vertex] = True
                traversal_stack.append(current_vertex)
                for edge in graph_instance.adjacent_edges(current_vertex):
                    neighbor = edge.get_other_endpoint(current_vertex)
                    if not visit_status[neighbor]:
                        self.parent_list[neighbor] = current_vertex
                        traversal_stack.append(neighbor)
            else:
                if current_vertex != root_vertex:
                    parent_vertex = self.parent_list[current_vertex]
                    if subtree_size[current_vertex] > max_subtree_size[parent_vertex]:
                        max_subtree_size[parent_vertex] = subtree_size[current_vertex]
                        heavy_child[parent_vertex] = current_vertex
                    subtree_size[parent_vertex] += subtree_size[current_vertex]
                for edge in graph_instance.adjacent_edges(current_vertex):
                    neighbor = edge.get_other_endpoint(current_vertex)
                    if neighbor != self.parent_list[current_vertex] and neighbor != heavy_child[current_vertex]:
                        self.vertex_to_path[neighbor] = construct_path(neighbor)
        self.vertex_to_path[root_vertex] = construct_path(root_vertex)

    def get_parent(self, vertex):
        return self.parent_list[vertex]

    def all_paths(self):
        return self.vertex_to_path.values()

    def find_path(self, vertex):
        return self.vertex_to_path[self.vertex_head[vertex]]

class ConsistentRangePathSum:
    def __init__(self, graph_instance, root_vertex):
        self.root_vertex = root_vertex
        self.hld_instance = ConsistentHeavyLightDecomposition(graph_instance, root_vertex)
        self.path_range_queries = {p.path_head: ConsistentRangeQuery(p.path_size) for p in self.hld_instance.all_paths()}

    def update_add(self, target_vertex, add_value):
        current_vertex = target_vertex
        while current_vertex != self.root_vertex:
            path_inst = self.hld_instance.find_path(current_vertex)
            head_vertex = path_inst.path_head
            if head_vertex != self.root_vertex:
                left_index = path_inst.get_index(head_vertex)
            else:
                left_index = path_inst.get_index(path_inst.get_next_vertex(head_vertex))
            right_index = path_inst.get_index(current_vertex)
            self.path_range_queries[head_vertex].range_add(left_index + 1, right_index + 1, add_value)
            current_vertex = self.hld_instance.get_parent(head_vertex)

    def range_sum(self, target_vertex):
        total_sum = 0
        current_vertex = target_vertex
        while current_vertex != self.root_vertex:
            path_inst = self.hld_instance.find_path(current_vertex)
            head_vertex = path_inst.path_head
            left_index = path_inst.get_index(head_vertex)
            right_index = path_inst.get_index(current_vertex)
            total_sum += self.path_range_queries[head_vertex].range_sum(left_index + 1, right_index + 1)
            current_vertex = self.hld_instance.get_parent(head_vertex)
        return total_sum

class ConsistentBinaryIndexedTree:
    def __init__(self, capacity):
        self.bit_capacity = capacity
        self.tree_vals = [0] * (self.bit_capacity + 1)

    def point_add(self, index, value):
        while index <= self.bit_capacity:
            self.tree_vals[index] += value
            index += (index & -index)

    def query_prefix(self, index):
        prefix_sum = 0
        while index > 0:
            prefix_sum += self.tree_vals[index]
            index -= (index & -index)
        return prefix_sum

class ConsistentRangeQuery:
    def __init__(self, length):
        self.range_length = length
        self.primary_bit = ConsistentBinaryIndexedTree(length + 1)
        self.secondary_bit = ConsistentBinaryIndexedTree(length + 1)

    def range_add(self, left, right, value):
        self.primary_bit.point_add(left, value * -left)
        self.primary_bit.point_add(right + 1, value * (right + 1))
        self.secondary_bit.point_add(left, value)
        self.secondary_bit.point_add(right + 1, -value)

    def range_sum(self, left, right):
        segment_sum = self.primary_bit.query_prefix(right + 1) + (right + 1) * self.secondary_bit.query_prefix(right + 1)
        segment_sum -= self.primary_bit.query_prefix(left) + left * self.secondary_bit.query_prefix(left)
        return segment_sum

def main_consistent_run():
    node_count = int(input())
    main_graph = ConsistentGraph(node_count)

    for node_index in range(node_count):
        values = [int(x) for x in input().split()]
        child_count, *children = values
        if child_count > 0:
            for child in children:
                main_graph.add_edge(ConsistentEdge(node_index, child))

    range_path_sum_solver = ConsistentRangePathSum(main_graph, 0)
    query_count = int(input())
    for _ in range(query_count):
        args = [int(x) for x in input().split()]
        command_id = args[0]
        if command_id == 0:
            target_node, addition_value = args[1], args[2]
            range_path_sum_solver.update_add(target_node, addition_value)
        elif command_id == 1:
            query_node = args[1]
            print(range_path_sum_solver.range_sum(query_node))
        else:
            raise ValueError("invalid command")

if __name__ == '__main__':
    main_consistent_run()