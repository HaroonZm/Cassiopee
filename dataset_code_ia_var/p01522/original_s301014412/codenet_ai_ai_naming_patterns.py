total_items, num_groups = map(int, raw_input().split())
group_assignments = [0] * 51
is_flagged_bad = [False] * 51
for group_index in xrange(num_groups):
    input_numbers = map(int, raw_input().split())[1:]
    for item in input_numbers:
        group_assignments[item] = group_index
for query_index in xrange(input()):
    item_a, item_b = map(int, raw_input().split())
    if group_assignments[item_a] == group_assignments[item_b]:
        is_flagged_bad[item_a] = True
        is_flagged_bad[item_b] = True
print is_flagged_bad.count(True)