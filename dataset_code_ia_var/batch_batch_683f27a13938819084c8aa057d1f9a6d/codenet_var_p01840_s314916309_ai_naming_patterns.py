num_items, margin, total_time = map(int, input().split())
time_points = [int(element) for element in input().split()]
initial_gap = time_points[0] - margin
final_gap = max(total_time - time_points[-1] - margin, 0)
middle_gaps = sum(max(0, time_points[index + 1] - time_points[index] - 2 * margin) for index in range(num_items - 1))
print(initial_gap + final_gap + middle_gaps)