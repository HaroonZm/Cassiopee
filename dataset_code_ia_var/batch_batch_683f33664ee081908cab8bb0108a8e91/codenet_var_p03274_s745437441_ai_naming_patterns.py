num_total, num_select = map(int, input().split())
coord_list = list(map(int, input().split()))

left_distances = []
right_distances = []

for coord in coord_list:
    if coord < 0:
        left_distances.append(-coord)
    else:
        right_distances.append(coord)

left_distances.reverse()
min_total_distance = float('inf')

for left_count in range(min(num_select + 1, len(left_distances) + 1)):
    right_count = num_select - left_count
    if left_count == 0:
        if len(right_distances) >= right_count:
            min_total_distance = min(min_total_distance, right_distances[num_select - 1])
    elif left_count == num_select:
        if len(left_distances) >= num_select:
            min_total_distance = min(min_total_distance, left_distances[num_select - 1])
    else:
        if len(right_distances) >= right_count and len(left_distances) >= left_count:
            right_furthest = right_distances[right_count - 1]
            left_furthest = left_distances[left_count - 1]
            if right_furthest < left_furthest:
                min_total_distance = min(min_total_distance, 2 * right_furthest + left_furthest)
            else:
                min_total_distance = min(min_total_distance, 2 * left_furthest + right_furthest)

print(min_total_distance)