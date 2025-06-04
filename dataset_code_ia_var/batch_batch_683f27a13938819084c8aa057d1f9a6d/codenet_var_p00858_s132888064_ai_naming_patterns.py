import sys
from heapq import heappush, heappop

io_in_read = sys.stdin.readline
io_out_write = sys.stdout.write

def geom_dot_ref_pt_vec(o_vec, a_vec, b_vec):
    ox, oy = o_vec
    ax, ay = a_vec
    bx, by = b_vec
    return (ax - ox) * (bx - ox) + (ay - oy) * (by - oy)

def geom_cross_ref_pt_vec(o_vec, a_vec, b_vec):
    ox, oy = o_vec
    ax, ay = a_vec
    bx, by = b_vec
    return (ax - ox) * (by - oy) - (bx - ox) * (ay - oy)

def geom_dist2_between_pts(pt_a, pt_b):
    ax, ay = pt_a
    bx, by = pt_b
    return (ax - bx) ** 2 + (ay - by) ** 2

def geom_segments_intersect(seg1_start, seg1_end, seg2_start, seg2_end):
    cross_a = geom_cross_ref_pt_vec(seg1_start, seg1_end, seg2_start)
    cross_b = geom_cross_ref_pt_vec(seg1_start, seg1_end, seg2_end)
    cross_c = geom_cross_ref_pt_vec(seg2_start, seg2_end, seg1_start)
    cross_d = geom_cross_ref_pt_vec(seg2_start, seg2_end, seg1_end)
    if cross_a == cross_b == 0:
        dot_e = geom_dot_ref_pt_vec(seg1_start, seg1_end, seg2_start)
        dot_f = geom_dot_ref_pt_vec(seg1_start, seg1_end, seg2_end)
        if not dot_e < dot_f:
            dot_e, dot_f = dot_f, dot_e
        return dot_e <= geom_dist2_between_pts(seg1_start, seg1_end) and 0 <= dot_f
    return cross_a * cross_b <= 0 and cross_c * cross_d <= 0

def problem_process_case():
    segment_cnt = int(io_in_read())
    if segment_cnt == 0:
        return False
    point_start_x, point_start_y = map(int, io_in_read().split())
    point_goal_x, point_goal_y = map(int, io_in_read().split())
    segment_list = []
    for seg_idx in range(segment_cnt):
        seg_x0, seg_y0, seg_x1, seg_y1 = map(int, io_in_read().split())
        seg_start = (seg_x0, seg_y0)
        seg_end = (seg_x1, seg_y1)
        segment_list.append((seg_start, seg_end))

    def segment_contains_point(seg_start, seg_end, pt_query):
        seg_x0, seg_y0 = seg_start
        seg_x1, seg_y1 = seg_end
        px, py = pt_query
        diff_x = seg_x1 - seg_x0
        diff_y = seg_y1 - seg_y0
        if (px - seg_x0) * diff_y != (py - seg_y0) * diff_x:
            return False
        if diff_x != 0:
            if diff_x < 0:
                return diff_x <= (px - seg_x0) <= 0
            return 0 <= (px - seg_x0) <= diff_x
        if diff_y < 0:
            return diff_y <= (py - seg_y0) <= 0
        return 0 <= (py - seg_y0) <= diff_y

    def segment_point_position_ratio(seg_start, seg_end, pt_query):
        seg_x0, seg_y0 = seg_start
        seg_x1, seg_y1 = seg_end
        px, py = pt_query
        diff_x = seg_x1 - seg_x0
        diff_y = seg_y1 - seg_y0
        if (px - seg_x0) * diff_y != (py - seg_y0) * diff_x:
            return None
        if diff_x != 0:
            if diff_x < 0:
                return -(px - seg_x0), -diff_x
            return (px - seg_x0), diff_x
        if diff_y < 0:
            return -(py - seg_y0), -diff_y
        return (py - seg_y0), diff_y

    key_point_set = set()
    segment_adj_list = [[] for _ in range(segment_cnt)]
    is_key_segment = [0] * segment_cnt

    for seg_idx_i in range(segment_cnt):
        seg_i_start, seg_i_end = segment_list[seg_idx_i]
        seg_i_touch_start, seg_i_touch_end = 0, 0
        for seg_idx_j in range(segment_cnt):
            if seg_idx_i == seg_idx_j:
                continue
            seg_j_start, seg_j_end = segment_list[seg_idx_j]
            if segment_contains_point(seg_j_start, seg_j_end, seg_i_start):
                seg_i_touch_start = 1
                segment_adj_list[seg_idx_i].append(seg_idx_j)
            elif segment_contains_point(seg_j_start, seg_j_end, seg_i_end):
                seg_i_touch_end = 1
                segment_adj_list[seg_idx_i].append(seg_idx_j)
        if seg_i_touch_start and seg_i_touch_end:
            is_key_segment[seg_idx_i] = 1
            key_point_set.add(seg_i_start)
            key_point_set.add(seg_i_end)

    key_point_sorted_list = sorted(key_point_set)
    key_point_index_map = {key_pt: idx for idx, key_pt in enumerate(key_point_sorted_list)}
    key_point_count = len(key_point_sorted_list)
    key_graph = [[] for _ in range(key_point_count)]

    for seg_idx in range(segment_cnt):
        seg_start, seg_end = segment_list[seg_idx]
        if not is_key_segment[seg_idx]:
            continue
        x0, y0 = seg_start
        x1, y1 = seg_end
        event_points = [(0, 0, seg_start), (1, 0, seg_end)]
        for adj_idx in range(segment_cnt):
            seg_cmp_start, seg_cmp_end = segment_list[adj_idx]
            pos_ratio = segment_point_position_ratio(seg_start, seg_end, seg_cmp_start)
            if pos_ratio is not None:
                s0, t0 = pos_ratio
                if 0 <= s0 <= t0:
                    if is_key_segment[adj_idx]:
                        event_points.append((s0 / t0, 0, seg_cmp_start))
                    else:
                        x2, y2 = seg_cmp_start
                        x3, y3 = seg_cmp_end
                        event_points.append(
                            (s0 / t0, 1, (x1 - x0)*(x3 - x2) + (y1 - y0)*(y3 - y2))
                        )
            else:
                pos_ratio = segment_point_position_ratio(seg_start, seg_end, seg_cmp_end)
                if pos_ratio is not None:
                    s0, t0 = pos_ratio
                    if 0 <= s0 <= t0:
                        if is_key_segment[adj_idx]:
                            event_points.append((s0 / t0, 0, seg_cmp_end))
                        else:
                            x2, y2 = seg_cmp_end
                            x3, y3 = seg_cmp_start
                            event_points.append(
                                (s0 / t0, 1, (x1 - x0)*(x3 - x2) + (y1 - y0)*(y3 - y2))
                            )
        event_points.sort()
        prev_point = None
        dir_a, dir_b = 1, 1
        for event_type, type_class, event_value in event_points:
            if type_class:
                if event_value < 0:
                    dir_b = 0
                elif event_value > 0:
                    dir_a = 0
                else:
                    dir_a = dir_b = 0
                continue
            if prev_point is not None and prev_point != event_value:
                dist_val = geom_dist2_between_pts(prev_point, event_value) ** 0.5
                idx_from = key_point_index_map[prev_point]
                idx_to = key_point_index_map[event_value]
                if dir_a:
                    key_graph[idx_from].append((idx_to, dist_val))
                if dir_b:
                    key_graph[idx_to].append((idx_from, dist_val))
                dir_a = dir_b = 1
            prev_point = event_value

    INF_LIB_VALUE = 10**18
    visited_prev = [-1] * key_point_count
    shortest_dist = [INF_LIB_VALUE] * key_point_count
    start_index = key_point_index_map[(point_start_x, point_start_y)]
    goal_index = key_point_index_map[(point_goal_x, point_goal_y)]
    shortest_dist[start_index] = 0
    dijkstra_queue = [(0, start_index)]
    while dijkstra_queue:
        current_cost, current_vertex = heappop(dijkstra_queue)
        if shortest_dist[current_vertex] < current_cost:
            continue
        for next_vertex, edge_cost in key_graph[current_vertex]:
            dist_candidate = current_cost + edge_cost
            if dist_candidate < shortest_dist[next_vertex]:
                shortest_dist[next_vertex] = dist_candidate
                visited_prev[next_vertex] = current_vertex
                heappush(dijkstra_queue, (dist_candidate, next_vertex))

    if shortest_dist[goal_index] == INF_LIB_VALUE:
        io_out_write("-1\n")
        return True

    restore_path_list = []
    current = goal_index
    while current != start_index:
        restore_path_list.append(key_point_sorted_list[current])
        current = visited_prev[current]
    restore_path_list.append(key_point_sorted_list[current])
    restore_path_list.reverse()
    for px, py in restore_path_list:
        io_out_write("%d %d\n" % (px, py))
    io_out_write("0\n")
    return True

while problem_process_case():
    pass