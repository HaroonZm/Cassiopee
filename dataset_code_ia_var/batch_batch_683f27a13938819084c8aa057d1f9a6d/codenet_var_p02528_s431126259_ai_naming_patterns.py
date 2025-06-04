def get_pivot_index(lst, left_idx, right_idx):
    range_len = right_idx - left_idx + 1
    if range_len < 3:
        return left_idx
    else:
        left_val = lst[left_idx]
        mid_idx = (left_idx + right_idx) // 2
        mid_val = lst[mid_idx]
        right_val = lst[right_idx]
        trio = [(left_val, left_idx), (mid_val, mid_idx), (right_val, right_idx)]
        trio.sort()
        return trio[1][1]

def quick_sort(lst, start_idx, end_idx):
    if end_idx <= start_idx:
        return
    pivot_idx = get_pivot_index(lst, start_idx, end_idx)
    pivot_val = lst[pivot_idx]
    lst[pivot_idx], lst[end_idx] = lst[end_idx], lst[pivot_idx]
    store_idx = start_idx
    for curr_idx in range(start_idx, end_idx):
        if lst[curr_idx] <= pivot_val:
            lst[curr_idx], lst[store_idx] = lst[store_idx], lst[curr_idx]
            store_idx += 1
    lst[store_idx], lst[end_idx] = lst[end_idx], lst[store_idx]
    quick_sort(lst, start_idx, store_idx - 1)
    quick_sort(lst, store_idx + 1, end_idx)

input_size = int(raw_input())
input_list = map(int, raw_input().split())
quick_sort(input_list, 0, input_size - 1)
print " ".join(map(str, input_list))