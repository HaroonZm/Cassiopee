import math
from collections import deque

class SegmentTreeCoherent:
    __slots__ = [
        "depth_level",
        "leaf_count",
        "node_count",
        "segment_tree",
        "pending_update",
        "identity_element"
    ]

    def __init__(self, input_array: list, identity_value: int):
        self.identity_element = identity_value
        input_length = len(input_array)
        self.depth_level = math.ceil(math.log2(input_length))
        self.leaf_count = 1 << self.depth_level
        self.node_count = 2 * self.leaf_count
        self.segment_tree = (
            [identity_value] * self.leaf_count +
            input_array +
            [identity_value] * (self.leaf_count - input_length)
        )
        self.pending_update = [None] * self.node_count
        self._initialize_segment_tree()

    def _initialize_segment_tree(self):
        st = self.segment_tree
        for idx in range(self.leaf_count - 1, 0, -1):
            left_child, right_child = st[idx << 1], st[(idx << 1) + 1]
            st[idx] = left_child if left_child < right_child else right_child

    def _propagate(self, range_left: int, range_right: int, update_value: int = None):
        st, pu, leaf_cnt, d_lvl = (
            self.segment_tree,
            self.pending_update,
            self.leaf_count,
            self.depth_level - 1
        )
        range_l = range_left + leaf_cnt
        range_r = range_right + leaf_cnt
        affected_nodes = deque()
        left_path, right_path = 0, 0
        left_depth, right_depth = 0, 0
        queue_append = affected_nodes.append

        curr_depth = d_lvl

        l, r = range_l, range_r
        while l < r:
            if l & 1:
                queue_append(l)
                left_path = left_path or l >> 1
                left_depth = left_depth or curr_depth
                l += 1
            if r & 1:
                r -= 1
                queue_append(r)
                right_path = right_path or r >> 1
                right_depth = right_depth or curr_depth
            l >>= 1
            r >>= 1
            curr_depth -= 1

        deepest_paths = (left_path, right_path)

        traversal_paths = [
            [left_path >> k for k in range(left_depth - 1, -1, -1)],
            [right_path >> k for k in range(right_depth - 1, -1, -1)]
        ]

        for path in traversal_paths:
            for node in path:
                if pu[node] is None:
                    continue
                st[node] = pu[node]
                if node < leaf_cnt:
                    pu[node << 1] = pu[node]
                    pu[(node << 1) + 1] = pu[node]
                pu[node] = None

        min_result = self.identity_element
        if update_value is None:
            for node in affected_nodes:
                if pu[node] is not None:
                    st[node] = pu[node]
                    if node < leaf_cnt:
                        pu[node << 1] = pu[node]
                        pu[(node << 1) + 1] = pu[node]
                    pu[node] = None
                if min_result > st[node]:
                    min_result = st[node]
        else:
            for node in affected_nodes:
                if node < leaf_cnt:
                    pu[node << 1] = update_value
                    pu[(node << 1) + 1] = update_value
                st[node] = update_value
                pu[node] = None

        self._refresh_internal_nodes(deepest_paths)
        return min_result if update_value is None else None

    def update_range(self, update_left, update_right, value):
        self._propagate(update_left, update_right, value)

    def query_range(self, query_left: int, query_right: int):
        st = self.segment_tree
        min_query = self._propagate(query_left, query_right)
        return min_query

    def _refresh_internal_nodes(self, affected_indices: tuple):
        st, pu = self.segment_tree, self.pending_update
        for node_idx in affected_indices:
            while node_idx > 0:
                left_idx, right_idx = node_idx << 1, (node_idx << 1) + 1
                left_val = st[left_idx] if pu[left_idx] is None else pu[left_idx]
                right_val = st[right_idx] if pu[right_idx] is None else pu[right_idx]
                st[node_idx] = left_val if left_val < right_val else right_val
                node_idx >>= 1

num_elements, num_operations = map(int, input().split())
segment_tree = SegmentTreeCoherent([2**31 - 1] * num_elements, 2**31 - 1)
output_results = []
output_append = output_results.append

for _ in range(num_operations):
    command_list = list(map(int, input().split()))
    if command_list[0] == 0:
        segment_tree.update_range(command_list[1], command_list[2] + 1, command_list[3])
    else:
        result = segment_tree.query_range(command_list[1], command_list[2] + 1)
        output_append(result)

print("\n".join(str(x) for x in output_results))