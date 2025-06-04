import sys
sys.setrecursionlimit(1000000)

def tsp_dp_state(state_a_idx, state_b_idx, current_idx):
    distance_row = all_distances[current_idx]
    if current_idx == num_points - 1:
        return distance_row[state_a_idx] + distance_row[state_b_idx]
    if dp_visited[state_a_idx][state_b_idx]:
        return dp_cache[state_a_idx][state_b_idx]
    option_1 = distance_row[state_a_idx] + tsp_dp_state(state_b_idx, current_idx, current_idx + 1)
    option_2 = distance_row[state_b_idx] + tsp_dp_state(state_a_idx, current_idx, current_idx + 1)
    dp_cache[state_a_idx][state_b_idx] = min(option_1, option_2)
    dp_visited[state_a_idx][state_b_idx] = True
    return dp_cache[state_a_idx][state_b_idx]

num_points = int(input())
point_list = [complex(*map(int, input().split())) for _ in range(num_points)]
all_distances = [[abs(point_a - point_b) for point_b in point_list] for point_a in point_list]
dp_visited = [[False] * num_points for _ in range(num_points)]
dp_cache = [[0] * num_points for _ in range(num_points)]

print(tsp_dp_state(0, 0, 0))