class TreeEdge:
    __slots__ = ('node_u', 'node_v')

    def __init__(self, node_u, node_v):
        self.node_u = node_u
        self.node_v = node_v

    def get_first(self):
        return self.node_u

    def get_other(self, ref_node):
        if ref_node == self.node_u:
            return self.node_v
        else:
            return self.node_u

class TreeGraph:
    def __init__(self, num_nodes):
        self.num_nodes = num_nodes
        self.adjacency = [[] for _ in range(num_nodes)]

    def add_edge(self, edge):
        self.adjacency[edge.node_u].append(edge)
        self.adjacency[edge.node_v].append(edge)

    def get_adjacent(self, node):
        return self.adjacency[node]

    def all_edges(self):
        for neighbor_list in self.adjacency:
            for edge in neighbor_list:
                yield edge

class SegmentRangeAddQuery:
    def __init__(self, size, fill_value=0):
        internal_size = 1
        while internal_size < size:
            internal_size <<= 1
        self.size_internal = 2 * internal_size - 1
        self.data_tree = [fill_value] * self.size_internal

    def add_range(self, left, right, increment):
        def _add(current, low, high):
            if high < left or low > right:
                return
            if left <= low and high <= right:
                self.data_tree[current] += increment
            else:
                mid = low + (high - low) // 2
                _add(current * 2 + 1, low, mid)
                _add(current * 2 + 2, mid + 1, high)
        return _add(0, 0, self.size_internal // 2)

    def get_point(self, index):
        def _query(current, low, high, acc):
            acc += self.data_tree[current]
            if low == high:
                return acc
            mid = low + (high - low) // 2
            if index <= mid:
                return _query(current * 2 + 1, low, mid, acc)
            else:
                return _query(current * 2 + 2, mid + 1, high, acc)
        return _query(0, 0, self.size_internal // 2, 0)

class SubtreeRangeSum:
    def __init__(self, input_graph, root_node):
        self.segment_raq = SegmentRangeAddQuery(input_graph.num_nodes)
        self.entry_time = [0] * input_graph.num_nodes
        self.exit_time = [0] * input_graph.num_nodes
        self._prepare_eulertour(input_graph, root_node)

    def _prepare_eulertour(self, graph, root):
        visited_nodes = [False] * graph.num_nodes
        process_stack = [root]
        order_counter = 0
        while process_stack:
            current = process_stack.pop()
            if not visited_nodes[current]:
                visited_nodes[current] = True
                self.entry_time[current] = order_counter
                order_counter += 1
                process_stack.append(current)
                for edge in graph.get_adjacent(current):
                    adj_node = edge.get_other(current)
                    if not visited_nodes[adj_node]:
                        process_stack.append(adj_node)
            else:
                self.exit_time[current] = order_counter - 1

    def add_to_subtree(self, node_id, increment):
        begin = self.entry_time[node_id]
        end = self.exit_time[node_id]
        self.segment_raq.add_range(begin, end, increment)

    def get_node_sum(self, node_id):
        return self.segment_raq.get_point(self.entry_time[node_id])

def main_execution():
    total_nodes = int(input())
    graph_instance = TreeGraph(total_nodes)
    for node_idx in range(total_nodes):
        input_parts = [int(x) for x in input().split()]
        child_count = input_parts[0]
        if child_count > 0:
            for child_node in input_parts[1:]:
                graph_instance.add_edge(TreeEdge(node_idx, child_node))
    path_sum_euler = SubtreeRangeSum(graph_instance, 0)
    query_count = int(input())
    for _ in range(query_count):
        query = [int(x) for x in input().split()]
        op_type = query[0]
        op_args = query[1:]
        if op_type == 0:
            target_node, value = op_args
            path_sum_euler.add_to_subtree(target_node, value)
        elif op_type == 1:
            (target_node,) = op_args
            print(path_sum_euler.get_node_sum(target_node))
        else:
            raise ValueError("unknown operation type")

if __name__ == "__main__":
    main_execution()