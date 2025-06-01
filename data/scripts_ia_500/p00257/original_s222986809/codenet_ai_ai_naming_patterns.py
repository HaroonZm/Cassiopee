import queue

while True:
    max_jump = int(input())
    if max_jump == 0:
        break
    num_positions = int(input())
    delta_displacement = [0] * (num_positions + 2)
    for pos_idx in range(1, num_positions + 1):
        delta_displacement[pos_idx] = int(input())
    is_visited = [False] * (num_positions + 2)
    is_visited[0] = True
    is_reachable_back = [False] * (num_positions + 2)
    is_reachable_back[num_positions + 1] = True
    reverse_graph = [[] for _ in range(num_positions + 2)]

    stack = queue.LifoQueue()
    stack.put(0)
    while not stack.empty():
        current_pos = stack.get()
        for jump_distance in range(1, max_jump + 1):
            next_pos = current_pos + jump_distance
            if next_pos > num_positions + 1:
                break
            adjusted_pos = min(max(next_pos + delta_displacement[next_pos], 0), num_positions + 1)
            reverse_graph[adjusted_pos].append(current_pos)
            if not is_visited[adjusted_pos]:
                stack.put(adjusted_pos)
                is_visited[adjusted_pos] = True

    stack.put(num_positions + 1)
    while not stack.empty():
        current_pos = stack.get()
        for prev_pos in reverse_graph[current_pos]:
            if not is_reachable_back[prev_pos]:
                is_reachable_back[prev_pos] = True
                stack.put(prev_pos)

    answer_status = 'OK'
    if not is_visited[num_positions + 1]:
        answer_status = 'NG'
    for pos in range(num_positions + 1):
        if is_visited[pos] and not is_reachable_back[pos]:
            answer_status = 'NG'
    print(answer_status)