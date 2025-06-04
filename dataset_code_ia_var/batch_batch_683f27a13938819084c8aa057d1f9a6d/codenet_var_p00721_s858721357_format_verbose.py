from heapq import heappush, heappop

INFINITY_DISTANCE = 10 ** 10

DIRECTIONS = ((0, -1), (0, 1), (-1, 0), (1, 0))  # left, right, up, down


def get_shortest_distance_between_points(start_point, end_point, room_map):
    """
    Utilise Dijkstra pour trouver la plus courte distance entre deux points
    sur la carte (room_map), en évitant les obstacles marqués par 'x'.
    """
    prioritized_queue = []
    heappush(prioritized_queue, (0, start_point))

    map_height = len(room_map)
    map_width = len(room_map[0])
    is_visited = [[False] * map_width for _ in range(map_height)]
    is_visited[start_point[1]][start_point[0]] = True

    while prioritized_queue:
        accumulated_distance, current_position = heappop(prioritized_queue)
        current_x, current_y = current_position
        for x_offset, y_offset in DIRECTIONS:
            next_x, next_y = current_x + x_offset, current_y + y_offset
            if (next_x, next_y) == end_point:
                return accumulated_distance + 1
            if (
                not is_visited[next_y][next_x]
                and room_map[next_y][next_x] != "x"
            ):
                is_visited[next_y][next_x] = True
                heappush(prioritized_queue, (accumulated_distance + 1, (next_x, next_y)))
    return -1  # No route found


def encode_remaining_targets(remaining_indices):
    """
    Encode l'ensemble des indices restants par une somme de puissances de 10 pour hashing rapide.
    """
    return sum([10 ** index for index in remaining_indices])


def compute_min_path_through_targets(current_index, remaining_indices, distance_graph, memoization_table):
    """
    Retourne la longueur minimum du chemin pour nettoyer toutes les taches restantes
    en partant du point d'indice current_index.
    """
    if not remaining_indices:
        return 0

    encoded_remaining = encode_remaining_targets(remaining_indices)
    if encoded_remaining in memoization_table[current_index]:
        return memoization_table[current_index][encoded_remaining]

    shortest_total_path = INFINITY_DISTANCE

    for distance, next_index in distance_graph[current_index]:
        if next_index in remaining_indices:
            candidate_path_length = distance + compute_min_path_through_targets(
                next_index,
                remaining_indices - {next_index},
                distance_graph,
                memoization_table
            )
            if candidate_path_length < shortest_total_path:
                shortest_total_path = candidate_path_length

    memoization_table[current_index][encoded_remaining] = shortest_total_path
    return shortest_total_path


def main():
    while True:
        room_width, room_height = map(int, input().split())
        if room_width == 0:
            break

        # Construction de la carte avec une bordure d'obstacles 'x'
        room_map = ["x" + input() + "x" for _ in range(room_height)]
        room_map.insert(0, "x" * (room_width + 2))
        room_map.append("x" * (room_width + 2))

        stain_positions = []
        starting_position_index = None

        for y in range(1, room_height + 1):
            for x in range(1, room_width + 1):
                if room_map[y][x] == "*":
                    stain_positions.append((x, y))
                elif room_map[y][x] == "o":
                    starting_position_index = len(stain_positions)
                    stain_positions.append((x, y))

        number_of_targets = len(stain_positions)
        distance_graph = [[] for _ in range(number_of_targets)]
        unreachable_flag = False

        # Calcul des distances entre chaque paire de taches ou de la position de départ
        for first_index in range(number_of_targets):
            for second_index in range(first_index + 1, number_of_targets):
                point_a = stain_positions[first_index]
                point_b = stain_positions[second_index]
                path_distance = get_shortest_distance_between_points(point_a, point_b, room_map)
                if path_distance == -1:
                    unreachable_flag = True
                distance_graph[first_index].append((path_distance, second_index))
                distance_graph[second_index].append((path_distance, first_index))

        if unreachable_flag:
            print(-1)
            continue

        memoization_table = [{} for _ in range(number_of_targets)]
        indices_to_clean = {index for index in range(number_of_targets) if index != starting_position_index}
        min_steps = compute_min_path_through_targets(
            starting_position_index,
            indices_to_clean,
            distance_graph,
            memoization_table
        )
        print(min_steps)

main()