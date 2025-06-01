while True:
    try:
        num_rows, num_cols = map(int, input().split())
    except:
        break

    relations = []
    while True:
        relation_line = input()
        if relation_line == "0 0 0":
            break
        start_idx, target_idx, multiplier = map(int, relation_line.split())
        relations.append((start_idx - 1, target_idx - 1, multiplier))

    num_vectors = int(input())
    vectors = [list(map(int, input().split())) for _ in range(num_vectors)]

    result_matrix = [[0] * num_rows for _ in range(num_vectors)]

    for start_idx, target_idx, multiplier in relations:
        for vector_idx in range(num_vectors):
            result_matrix[vector_idx][start_idx] += vectors[vector_idx][target_idx] * multiplier

    for vector_idx in range(num_vectors):
        print(" ".join(str(value) for value in result_matrix[vector_idx]))