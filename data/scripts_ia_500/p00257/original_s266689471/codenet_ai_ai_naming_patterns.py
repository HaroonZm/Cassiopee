from collections import deque

while True:
    max_jump = int(input())
    if max_jump == 0:
        break
    num_positions = int(input())
    position_offsets = [0] + [int(input()) for _ in range(num_positions)] + [0]
    graph_predecessors = [[] for _ in range(num_positions + 2)]

    visited_forward = [0] * (num_positions + 2)
    queue_forward = deque([0])
    visited_forward[0] = 1

    while queue_forward:
        current_pos = queue_forward.popleft()
        for step in range(1, max_jump + 1):
            if position_offsets[min(current_pos + step, num_positions + 1)] != 0:
                next_pos = max(min(current_pos + step + position_offsets[current_pos + step], num_positions + 1), 0)
            else:
                next_pos = min(current_pos + step, num_positions + 1)
            if not visited_forward[next_pos]:
                queue_forward.append(next_pos)
                visited_forward[next_pos] = 1
            graph_predecessors[next_pos].append(current_pos)

    visited_backward = [0] * (num_positions + 2)
    queue_backward = deque([num_positions + 1])
    visited_backward[num_positions + 1] = 1

    while queue_backward:
        current_pos = queue_backward.popleft()
        for prev_pos in graph_predecessors[current_pos]:
            if visited_backward[prev_pos]:
                continue
            visited_backward[prev_pos] = 1
            queue_backward.append(prev_pos)

    print("OK" if visited_forward == visited_backward else "NG")