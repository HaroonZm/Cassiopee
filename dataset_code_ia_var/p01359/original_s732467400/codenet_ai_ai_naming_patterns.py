#!/usr/bin/python

def binary_search_bounds(data_list, query_value, left_idx, right_idx):
    if left_idx == right_idx:
        if query_value <= data_list[left_idx][2]:
            return int(left_idx)
        else:
            return left_idx + 1
    mid_idx = left_idx + (right_idx - left_idx) // 2
    if query_value <= data_list[mid_idx][2]:
        return binary_search_bounds(data_list, query_value, left_idx, mid_idx)
    elif data_list[mid_idx][2] < query_value:
        return binary_search_bounds(data_list, query_value, mid_idx + 1, right_idx)

while True:
    num_entries_query = raw_input().split()
    num_entries, num_queries = map(int, num_entries_query)
    if num_entries == 0:
        break

    entry_list = []
    for entry_idx in range(num_entries):
        entry_data = raw_input().split()
        entry_list.append(entry_data)
    for entry_idx in range(num_entries):
        entry_list[entry_idx][1] = int(entry_list[entry_idx][1])
        entry_list[entry_idx][2] = int(entry_list[entry_idx][2])
    entry_list.sort(key=lambda item: item[2])

    for query_idx in range(num_queries):
        current_query = int(raw_input())
        position_idx = binary_search_bounds(entry_list, current_query, 0, num_entries - 1)
        if position_idx < num_entries and entry_list[position_idx][1] > entry_list[position_idx][2] - current_query:
            print entry_list[position_idx][0], entry_list[position_idx][1] - (entry_list[position_idx][2] - current_query)
        else:
            print "Unknown"