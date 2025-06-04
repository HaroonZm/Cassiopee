class Polyline:
    def __init__(self, is_flag_active=False):
        self.num_points = int(raw_input())
        self.point_list_original = [map(int, raw_input().split(" ")) for _ in range(self.num_points)]
        self.point_list_reversed = self.point_list_original[::-1]
        self.point_list_normal = self._normalize_points(self.point_list_original)
        if is_flag_active:
            self.point_list_reversed_normal = self._normalize_points(self.point_list_reversed)
        else:
            self.point_list_reversed_normal = self.point_list_reversed

    def is_equivalent(self, other_polyline):
        return (self.num_points == other_polyline.num_points and
                (self._compare_point_lists(self.point_list_normal, other_polyline.point_list_normal) or
                 self._compare_point_lists(self.point_list_reversed_normal, other_polyline.point_list_normal)))

    def _normalize_points(self, points):
        delta_to_origin = (0 - points[0][0], 0 - points[0][1])
        second_point_translated = (points[1][0] + delta_to_origin[0], points[1][1] + delta_to_origin[1])
        if second_point_translated[0] == 0:
            orientation_sign = -1 if second_point_translated[1] < 0 else 1
            normalized_points = [[orientation_sign * (x + delta_to_origin[0]), orientation_sign * (y + delta_to_origin[1])] for x, y in points]
        else:
            orientation_sign = -1 if second_point_translated[0] < 0 else 1
            normalized_points = [[-orientation_sign * (y + delta_to_origin[1]), orientation_sign * (x + delta_to_origin[0])] for x, y in points]
        return normalized_points

    def _compare_point_lists(self, list_a, list_b):
        for idx in range(self.num_points):
            if list_a[idx] != list_b[idx]:
                return False
        return True

while True:
    num_polylines = int(raw_input())
    if num_polylines == 0:
        break
    matching_indices = []
    reference_polyline = Polyline(True)
    for idx in range(1, num_polylines + 1):
        current_polyline = Polyline()
        if reference_polyline.is_equivalent(current_polyline):
            matching_indices.append(idx)
    matching_indices.sort()
    for match_idx in matching_indices:
        print match_idx
    print "+++++"