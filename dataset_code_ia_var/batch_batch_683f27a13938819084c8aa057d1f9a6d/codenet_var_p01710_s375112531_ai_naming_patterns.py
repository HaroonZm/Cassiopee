import sys
from collections import deque

input_reader = sys.stdin.readline
output_writer = sys.stdout.write

def strongly_connected_components(node_count, adj_list, rev_adj_list):
    node_order = []
    visited_nodes = [0] * node_count
    component_group = [None] * node_count

    def forward_dfs(node_index):
        visited_nodes[node_index] = 1
        for neighbor_index in adj_list[node_index]:
            if not visited_nodes[neighbor_index]:
                forward_dfs(neighbor_index)
        node_order.append(node_index)

    def reverse_dfs(node_index, component_id):
        component_group[node_index] = component_id
        visited_nodes[node_index] = 1
        for neighbor_index in rev_adj_list[node_index]:
            if not visited_nodes[neighbor_index]:
                reverse_dfs(neighbor_index, component_id)

    for idx in range(node_count):
        if not visited_nodes[idx]:
            forward_dfs(idx)

    visited_nodes = [0] * node_count
    current_label = 0
    for node_index in reversed(node_order):
        if not visited_nodes[node_index]:
            reverse_dfs(node_index, current_label)
            current_label += 1

    return current_label, component_group

def component_graph_construction(node_count, adj_list, label_count, component_group):
    comp_adj_list = [set() for _ in range(label_count)]
    comp_rev_adj_list = [set() for _ in range(label_count)]
    comp_node_members = [[] for _ in range(label_count)]

    for node_index in range(node_count):
        source_label = component_group[node_index]
        for dest_index in adj_list[node_index]:
            target_label = component_group[dest_index]
            if source_label == target_label:
                continue
            comp_adj_list[source_label].add(target_label)
            comp_rev_adj_list[target_label].add(source_label)
        comp_node_members[source_label].append(node_index)

    return comp_adj_list, comp_rev_adj_list, comp_node_members

def main_solver():
    node_count, edge_count, knapsack_capacity = map(int, input_reader().split())
    if node_count == edge_count == knapsack_capacity == 0:
        return False

    item_value = [0] * node_count
    item_weight = [0] * node_count
    item_count = [0] * node_count
    for idx in range(node_count):
        item_value[idx], item_weight[idx], item_count[idx] = map(int, input_reader().split())

    base_adj_list = [[] for _ in range(node_count)]
    base_rev_adj_list = [[] for _ in range(node_count)]
    self_loop_flags = [0] * node_count

    for _ in range(edge_count):
        from_node, to_node = map(int, input_reader().split())
        if from_node == to_node:
            self_loop_flags[from_node - 1] = 1
        else:
            base_adj_list[from_node - 1].append(to_node - 1)
            base_rev_adj_list[to_node - 1].append(from_node - 1)

    component_label_count, component_group = strongly_connected_components(
        node_count, base_adj_list, base_rev_adj_list
    )
    comp_adj_list, comp_rev_adj_list, comp_node_members = component_graph_construction(
        node_count, base_adj_list, component_label_count, component_group
    )

    max_inf = 10 ** 18
    dp_table = [None] * component_label_count
    base_dp_state = [0] + [-max_inf] * knapsack_capacity

    bfs_queue = deque()
    incoming_degree = [0] * component_label_count

    for idx in range(component_label_count):
        if not len(comp_rev_adj_list[idx]):
            bfs_queue.append(idx)
            dp_table[idx] = base_dp_state[:]
        incoming_degree[idx] = len(comp_rev_adj_list[idx])

    max_result = 0
    combined_dp = [0] * (knapsack_capacity + 1)

    while bfs_queue:
        current_comp = bfs_queue.popleft()
        current_dp = dp_table[current_comp]
        member_nodes = comp_node_members[current_comp]

        if len(member_nodes) == 1 and not self_loop_flags[member_nodes[0]]:
            node = member_nodes[0]
            node_value, node_weight_val = item_value[node], item_weight[node]
            for cap in range(knapsack_capacity, node_weight_val - 1, -1):
                current_dp[cap] = max(current_dp[cap], current_dp[cap - node_weight_val] + node_value)
        else:
            temp_deque = deque()
            for node in member_nodes:
                node_val = item_value[node]
                node_wei = item_weight[node]
                node_cnt = item_count[node]
                if knapsack_capacity < node_wei:
                    continue
                if node_cnt == 1:
                    for cap in range(knapsack_capacity, node_wei - 1, -1):
                        current_dp[cap] = max(current_dp[cap], current_dp[cap - node_wei] + node_val)
                elif knapsack_capacity <= node_wei * node_cnt:
                    for cap in range(node_wei, knapsack_capacity + 1):
                        current_dp[cap] = max(current_dp[cap], current_dp[cap - node_wei] + node_val)
                else:
                    for mod_val in range(node_wei):
                        temp_deque.clear()
                        for multiple in range((knapsack_capacity - mod_val) // node_wei + 1):
                            index = mod_val + multiple * node_wei
                            prev_val = current_dp[index] - multiple * node_val
                            while temp_deque and temp_deque[-1][1] <= prev_val:
                                temp_deque.pop()
                            temp_deque.append((multiple, prev_val))
                            current_dp[index] = temp_deque[0][1] + multiple * node_val
                            if temp_deque[0][0] == multiple - node_cnt:
                                temp_deque.popleft()
        max_result = max(max_result, max(current_dp))

        for neighbor_comp in comp_adj_list[current_comp]:
            incoming_degree[neighbor_comp] -= 1
            if incoming_degree[neighbor_comp] == 0:
                bfs_queue.append(neighbor_comp)
            if dp_table[neighbor_comp] is None:
                dp_table[neighbor_comp] = current_dp[:]
            else:
                dp_table[neighbor_comp][:] = (max(a, b) for a, b in zip(dp_table[neighbor_comp], current_dp))

    output_writer(f"{max_result}\n")
    return True

while main_solver():
    pass