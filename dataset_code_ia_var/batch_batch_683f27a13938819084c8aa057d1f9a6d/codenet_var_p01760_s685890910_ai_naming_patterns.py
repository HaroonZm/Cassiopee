input_target, input_distance = map(int, input().split())
temp_a, temp_b = map(int, input().split())
dist_a, dist_b = map(int, input().split())

min_diff_result = 10000000007

for count_a in range(input_distance // dist_a + 1):
    for count_b in range(input_distance // dist_b + 1):
        total_distance = count_a * dist_a + count_b * dist_b
        if 1 <= total_distance <= input_distance:
            combined_temp = (temp_a * count_a * dist_a + temp_b * count_b * dist_b) / total_distance
            current_diff = abs(input_target - combined_temp)
            min_diff_result = min(min_diff_result, current_diff)

print(min_diff_result)