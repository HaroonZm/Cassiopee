number_of_bits = int(input())

for current_number in range(1 << number_of_bits):

    subset_indices = []
    temp_number = current_number
    bit_position = 0
    bitmask = current_number

    while bitmask:
        if bitmask & 1:
            subset_indices.append(bit_position)
        bit_position += 1
        bitmask = bitmask >> 1

    print(f'{temp_number}:', end = '')

    if temp_number == 0:
        print()
    else:
        print('', *subset_indices)