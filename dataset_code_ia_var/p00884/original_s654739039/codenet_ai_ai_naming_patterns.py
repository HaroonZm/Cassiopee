def depth_first_search(graph_map, node_names, member_lists, visited_flags, current_index):
    if visited_flags[current_index]:
        return graph_map[node_names[current_index]]
    visited_flags[current_index] = 1
    current_members = member_lists[current_index]
    for member_index in range(len(current_members)):
        member = current_members[member_index]
        if member in graph_map:
            result = depth_first_search(
                graph_map,
                node_names,
                member_lists,
                visited_flags,
                node_names.index(member)
            )
            for elem in result:
                if elem not in graph_map[node_names[current_index]]:
                    graph_map[node_names[current_index]].append(elem)
        else:
            if member not in graph_map[node_names[current_index]]:
                graph_map[node_names[current_index]].append(member)
    return graph_map[node_names[current_index]]

while True:
    nodes_count = input()
    if not nodes_count:
        break
    node_names_list = []
    member_lists_all = []
    graph_representation = {}
    for node_idx in range(nodes_count):
        group_input, members_input = raw_input().split(":")
        node_names_list.append(group_input)
        member_lists_all.append(members_input[:-1].split(","))
        graph_representation[group_input] = []
    depth_first_search(
        graph_representation,
        node_names_list,
        member_lists_all,
        [0] * nodes_count,
        0
    )
    print len(graph_representation[node_names_list[0]])