def compute_dimensions():
    DIRECTION_DELTAS = [(-1, 0), (0, -1), (1, 0), (0, 1)]
    while True:
        node_count = int(input())
        if node_count == 0:
            exit()
        x_positions = [0]
        y_positions = [0]
        for node_index in range(node_count - 1):
            parent_node, direction_index = map(int, input().split())
            x_positions.append(x_positions[parent_node] + DIRECTION_DELTAS[direction_index][0])
            y_positions.append(y_positions[parent_node] + DIRECTION_DELTAS[direction_index][1])
        width = max(x_positions) - min(x_positions) + 1
        height = max(y_positions) - min(y_positions) + 1
        print(width, height)

if __name__ == '__main__':
    compute_dimensions()