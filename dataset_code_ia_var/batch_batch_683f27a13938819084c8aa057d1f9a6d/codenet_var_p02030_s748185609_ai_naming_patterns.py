input_n, input_m = raw_input().split()
set_a = set(map(int, raw_input().split()))
set_b = set(map(int, raw_input().split()))
set_intersection_sorted = sorted(set_a & set_b)
set_union_sorted = sorted(set_a | set_b)
count_intersection = len(set_intersection_sorted)
count_union = len(set_union_sorted)
print count_intersection, count_union
for value_intersection in set_intersection_sorted:
    print value_intersection
for value_union in set_union_sorted:
    print value_union