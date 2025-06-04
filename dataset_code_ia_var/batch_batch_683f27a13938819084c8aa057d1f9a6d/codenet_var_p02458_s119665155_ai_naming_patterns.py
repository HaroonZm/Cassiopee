from bisect import bisect_left as _bs_left, bisect_right as _bs_right, insort_left as _ins_left

multiset_counter = {}
multiset_sorted_keys = []
multiset_total_count = 0
query_count = int(input())
for query_index in range(query_count):
    query_parts = input().split()
    operation_type = query_parts[0]
    key_value = int(query_parts[1])
    if operation_type == '0':
        if key_value not in multiset_counter:
            multiset_counter[key_value] = 1
            _ins_left(multiset_sorted_keys, key_value)
        else:
            multiset_counter[key_value] += 1
        multiset_total_count += 1
        print(multiset_total_count)
    elif operation_type == '1':
        print(multiset_counter[key_value] if key_value in multiset_counter else 0)
    elif operation_type == '2':
        if key_value in multiset_counter:
            multiset_total_count -= multiset_counter[key_value]
            multiset_counter[key_value] = 0
    else:
        lower_bound = _bs_left(multiset_sorted_keys, int(query_parts[1]))
        upper_bound = _bs_right(multiset_sorted_keys, int(query_parts[2]), lower_bound)
        for index in range(lower_bound, upper_bound):
            current_key = multiset_sorted_keys[index]
            for _ in range(multiset_counter[current_key]):
                print(current_key)