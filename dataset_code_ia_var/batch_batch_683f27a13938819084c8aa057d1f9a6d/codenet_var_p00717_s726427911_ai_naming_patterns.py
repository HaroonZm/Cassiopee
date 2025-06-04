def input_read_as_int():
    return int(raw_input())

def input_read_as_int_list():
    return [int(x) for x in raw_input().split()]

def path_read():
    point_count = input_read_as_int()
    return [complex(*input_read_as_int_list()) for _ in xrange(point_count)]

def path_are_congruent(path_a, path_b):
    segment_count = len(path_a)
    if segment_count != len(path_b):
        return False
    base_ratio = (path_a[1] - path_a[0]) / (path_b[1] - path_b[0])
    if base_ratio not in (1, 1j, -1, -1j):
        return False
    for seg_idx in xrange(1, segment_count - 1):
        segment_ratio = (path_a[seg_idx + 1] - path_a[seg_idx]) / (path_b[seg_idx + 1] - path_b[seg_idx])
        if segment_ratio != base_ratio:
            return False
    return True

while True:
    test_case_count = input_read_as_int()
    if test_case_count == 0:
        break
    ref_path = path_read()
    ref_path_rev = list(reversed(ref_path))
    for candidate_idx in xrange(1, test_case_count + 1):
        candidate_path = path_read()
        if path_are_congruent(ref_path, candidate_path) or path_are_congruent(ref_path_rev, candidate_path):
            print candidate_idx
    print "+++++"