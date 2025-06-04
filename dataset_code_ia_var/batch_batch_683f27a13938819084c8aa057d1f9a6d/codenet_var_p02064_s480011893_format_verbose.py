def main():

    total_nodes, start_node, target_node = map(int, input().split())

    if total_nodes <= 2:
        print("! " + str(start_node) + " " + str(target_node))
        return

    print("? " + str(start_node) + " " + str(target_node))
    shortest_distance_between_start_and_target = int(input())

    distance_from_start_to_each_node = [(0, 0) for _ in range(total_nodes)]

    for node_index in range(total_nodes):
        print("? " + str(start_node) + " " + str(node_index + 1), flush=True)
        distance = int(input())
        distance_from_start_to_each_node[node_index] = (distance, node_index + 1)

    distance_from_start_to_each_node.sort()

    distance_from_target_to_each_node = [0] * (total_nodes + 1)

    for node_label in range(1, total_nodes + 1):
        print("? " + str(target_node) + " " + str(node_label), flush=True)
        distance = int(input())
        distance_from_target_to_each_node[node_label] = distance

    answer_path = [start_node]
    last_used_distance = 0

    for ordered_index in range(1, total_nodes):
        current_distance, current_node_label = distance_from_start_to_each_node[ordered_index]
        
        if current_distance == shortest_distance_between_start_and_target:
            answer_path.append(target_node)
            break
        
        if last_used_distance == current_distance:
            continue
        
        if current_distance + distance_from_target_to_each_node[current_node_label] == shortest_distance_between_start_and_target:
            answer_path.append(current_node_label)
            last_used_distance = current_distance

    print("! " + " ".join(map(str, answer_path)))

if __name__ == '__main__':
    main()