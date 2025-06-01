import sys

def get_min_value_in_row(data):
    if len(data) < 1:
        return 0
    minimum_index = 0
    for idx, val in enumerate(data):
        if val < data[minimum_index]:
            minimum_index = idx
    return minimum_index

def is_max(Min, index, data):
    max_val = data[index][Min]
    i = index
    while i >= 0:
        if data[i][Min] > max_val:
            max_val = data[i][Min]
        i -= 1
    i = index
    while i < len(data):
        if data[i][Min] > max_val:
            max_val = data[i][Min]
        i += 1
    return max_val == data[index][Min]

def print_both(data):
    idx = 0
    while idx < len(data):
        min_pos = get_min_value_in_row(data[idx])
        if is_max(min_pos, idx, data):
            print(data[idx][min_pos])
            return
        idx += 1
    print(0)

lines = sys.stdin.readlines()

i = 0
while i < len(lines):
    stripped = lines[i].strip()
    if len(stripped) == 2 and stripped.isdigit():
        count = int(stripped)
        Matrix = []
        for j in range(i+1, i+1+count):
            nums = list(map(int, lines[j].split()))
            Matrix.append(nums)
        i += count + 1
        print_both(Matrix)
    else:
        i += 1