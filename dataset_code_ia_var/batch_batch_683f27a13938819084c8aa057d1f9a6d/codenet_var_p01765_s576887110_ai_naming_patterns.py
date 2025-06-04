def compute_point_segment_distance(pt, seg_start, seg_end):
    relative_pt = pt - seg_start
    seg_vector = seg_end - seg_start
    projected = (relative_pt / seg_vector) * abs(seg_vector)
    seg_length = abs(seg_vector)
    if 0 <= projected.real <= seg_length:
        return abs(projected.imag)
    return min(abs(relative_pt), abs(relative_pt - seg_vector))

num_points_a = int(input())
points_a = [0]
for _ in range(num_points_a):
    coord_x, coord_y = map(int, input().split())
    points_a.append(complex(coord_x, coord_y))
points_a.append(1000)

num_points_b = int(input())
points_b = [1000j]
for _ in range(num_points_b):
    coord_x, coord_y = map(int, input().split())
    points_b.append(complex(coord_x, coord_y))
points_b.append(1000 + 1000j)

minimum_distance = 10 ** 30
for idx_a in range(num_points_a + 2):
    for idx_b in range(num_points_b + 1):
        current_distance = compute_point_segment_distance(points_a[idx_a], points_b[idx_b], points_b[idx_b + 1])
        minimum_distance = min(minimum_distance, current_distance)
for idx_b in range(num_points_b + 2):
    for idx_a in range(num_points_a + 1):
        current_distance = compute_point_segment_distance(points_b[idx_b], points_a[idx_a], points_a[idx_a + 1])
        minimum_distance = min(minimum_distance, current_distance)
print(minimum_distance)