input_n = int(input())
input_line = input().split()
input_k = int(input_line[0])
input_indices = [int(s) for s in input_line[1:]]

total_subsets = 2 ** input_n
for subset_index in range(total_subsets):
    subset_bits = [0 for _ in range(input_n)]
    temp_index = subset_index
    bit_pos = 0
    while temp_index > 0:
        if temp_index % 2 == 1:
            subset_bits[bit_pos] = 1
        temp_index //= 2
        bit_pos += 1
    all_selected = True
    for required_idx in input_indices:
        if subset_bits[required_idx] == 0:
            all_selected = False
    if all_selected:
        selected_indices = []
        for idx in range(input_n):
            if subset_bits[idx] == 1:
                selected_indices.append(idx)
        print(subset_index, end="")
        if subset_index != 0:
            print(":", end=" ")
            print(*selected_indices)
        else:
            print(":")