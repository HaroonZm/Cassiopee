import bisect

while True:
    entry_count, query_count = map(int, input().split())
    if entry_count == 0:
        break
    entry_list = []
    for entry_index in range(entry_count):
        entry_name, entry_length, entry_year = input().split()
        entry_tuple = (int(entry_year), int(entry_length), entry_name)
        entry_list.append(entry_tuple)
    entry_list.sort()
    for query_index in range(query_count):
        query_value = int(input())
        bisect_index = bisect.bisect(entry_list, (query_value, -1, -1))
        resolved = False
        if bisect_index < entry_count:
            candidate_year, candidate_length, candidate_name = entry_list[bisect_index]
            if candidate_year - candidate_length < query_value <= candidate_year:
                print(candidate_name + ' ' + str(query_value - candidate_year + candidate_length))
                resolved = True
        if not resolved and bisect_index + 1 < entry_count:
            candidate_year, candidate_length, candidate_name = entry_list[bisect_index + 1]
            if candidate_year - candidate_length < query_value <= candidate_year:
                print(candidate_name + ' ' + str(query_value - candidate_year + candidate_length))
                resolved = True
        if not resolved:
            print('Unknown')