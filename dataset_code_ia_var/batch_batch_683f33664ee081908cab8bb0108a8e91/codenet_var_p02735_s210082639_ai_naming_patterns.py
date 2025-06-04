def compute_min_transitions():
    row_count, col_count = map(int, input().split())
    grid_matrix = [list(input()) for grid_row_idx in range(row_count)]

    transition_dp = [[0 for col_idx in range(col_count)] for row_idx in range(row_count)]

    for row_idx in range(1, row_count):
        if grid_matrix[row_idx - 1][0] == '.' and grid_matrix[row_idx][0] == '#':
            transition_dp[row_idx][0] = transition_dp[row_idx - 1][0] + 1
        else:
            transition_dp[row_idx][0] = transition_dp[row_idx - 1][0]

    for col_idx in range(1, col_count):
        if grid_matrix[0][col_idx - 1] == '.' and grid_matrix[0][col_idx] == '#':
            transition_dp[0][col_idx] = transition_dp[0][col_idx - 1] + 1
        else:
            transition_dp[0][col_idx] = transition_dp[0][col_idx - 1]

    for row_idx in range(1, row_count):
        for col_idx in range(1, col_count):
            upward_transition = transition_dp[row_idx - 1][col_idx]
            if grid_matrix[row_idx - 1][col_idx] == '.' and grid_matrix[row_idx][col_idx] == '#':
                upward_transition += 1

            leftward_transition = transition_dp[row_idx][col_idx - 1]
            if grid_matrix[row_idx][col_idx - 1] == '.' and grid_matrix[row_idx][col_idx] == '#':
                leftward_transition += 1

            transition_dp[row_idx][col_idx] = min(upward_transition, leftward_transition)

    total_transitions = transition_dp[row_count - 1][col_count - 1]
    if grid_matrix[0][0] == '#':
        total_transitions += 1

    print(total_transitions)

if __name__ == '__main__':
    compute_min_transitions()