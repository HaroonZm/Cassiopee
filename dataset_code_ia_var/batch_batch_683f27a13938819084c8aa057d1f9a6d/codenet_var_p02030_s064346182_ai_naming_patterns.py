num_set_a_size, num_set_b_size = map(int, input().split())
set_a_elements = set(map(int, input().split()))
set_b_elements = set(map(int, input().split()))
set_intersection_sorted = sorted(set_a_elements & set_b_elements)
set_union_sorted = sorted(set_a_elements | set_b_elements)
print(len(set_intersection_sorted), len(set_union_sorted))
for element in set_intersection_sorted:
    print(element)
for element in set_union_sorted:
    print(element)