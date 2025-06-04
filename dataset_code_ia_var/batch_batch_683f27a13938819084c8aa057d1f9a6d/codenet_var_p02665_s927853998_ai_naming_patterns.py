node_depth_count = int(input())
leaf_required_count_list = list(map(int, input().split()))

max_nodes_per_depth_list = [1]
for depth_index in range(1, node_depth_count + 1):
    if depth_index == node_depth_count:
        max_nodes_per_depth_list.append(leaf_required_count_list[depth_index])
    else:
        possible_nodes = (max_nodes_per_depth_list[-1] - leaf_required_count_list[depth_index - 1]) * 2
        max_nodes_per_depth_list.append(possible_nodes)
        if max_nodes_per_depth_list[-1] < 0:
            print(-1)
            exit()

if node_depth_count == 0:
    if leaf_required_count_list[0] != 1:
        print(-1)
        exit()

nodes_at_depth_list = [leaf_required_count_list[-1]]
current_leaf_count = leaf_required_count_list[-1]
for depth_index in range(node_depth_count - 1, -1, -1):
    allowed_nodes = min(current_leaf_count + leaf_required_count_list[depth_index], max_nodes_per_depth_list[depth_index])
    nodes_at_depth_list.append(allowed_nodes)
    current_leaf_count = nodes_at_depth_list[-1]

for depth_index in range(node_depth_count):
    ancestor_depth = node_depth_count - depth_index
    if (nodes_at_depth_list[ancestor_depth] - leaf_required_count_list[depth_index]) * 2 < leaf_required_count_list[depth_index + 1]:
        print(-1)
        exit()
print(sum(nodes_at_depth_list))