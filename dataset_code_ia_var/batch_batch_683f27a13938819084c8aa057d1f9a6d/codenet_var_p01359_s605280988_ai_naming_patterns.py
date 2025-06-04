num_input, num_output = (int(val) for val in input().split())
while True:
    range_dict = {}
    for idx_input in range(num_input):
        entry = input().split()
        key = entry[0]
        range_start = int(entry[1])
        range_end = int(entry[2])
        range_first = range_end - range_start + 1
        range_dict[key] = [range_first, range_end]
    for idx_output in range(num_output):
        query_val = int(input())
        found = False
        for label, (range_first, range_end) in range_dict.items():
            if range_first <= query_val <= range_end:
                print(f"{label} {query_val - range_first + 1}")
                found = True
                break
        if not found:
            print("Unknown")
    num_input, num_output = (int(val) for val in input().split())
    if num_input == 0 and num_output == 0:
        break