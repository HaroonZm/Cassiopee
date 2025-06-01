NULL = 10000
TOWN_COUNT = 10
while True:
    input_count = int(input())
    if input_count == 0:
        break
    adjacency_matrix = []
    for _ in range(TOWN_COUNT):
        row = []
        for __ in range(TOWN_COUNT):
            row.append(NULL)
        adjacency_matrix.append(row)
    for i in range(TOWN_COUNT):
        adjacency_matrix[i][i] = 0
    need_range = 0
    for _ in range(input_count):
        line = input()
        parts = line.split(" ")
        start = int(parts[0])
        end = int(parts[1])
        time = int(parts[2])
        adjacency_matrix[start][end] = time
        adjacency_matrix[end][start] = time
        if start > need_range:
            need_range = start
        if end > need_range:
            need_range = end
    for a in range(need_range + 1):
        for b in range(need_range + 1):
            for c in range(need_range + 1):
                val = adjacency_matrix[b][a] + adjacency_matrix[a][c]
                if val < adjacency_matrix[b][c]:
                    adjacency_matrix[b][c] = val
    min_time = NULL
    min_index = -1
    for index in range(len(adjacency_matrix)):
        item = adjacency_matrix[index]
        need_element = []
        for item2 in item:
            if item2 > 0 and item2 < NULL:
                need_element.append(item2)
        if len(need_element) > 0:
            time = 0
            for t in need_element:
                time += t
            if time < min_time:
                min_time = time
                min_index = index
    print(min_index, min_time)