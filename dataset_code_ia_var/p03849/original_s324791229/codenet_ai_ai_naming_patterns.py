MODULO = 10**9 + 7
binary_string = bin(int(input()))[2:]
memo_table = [[[0, 0], [0, 0]] for _ in range(len(binary_string))]

def dp_recursive(position_index, last_bit, is_limited):
    if position_index == len(binary_string):
        return int(last_bit == 0)
    if memo_table[position_index][last_bit][is_limited]:
        return memo_table[position_index][last_bit][is_limited]
    total_count = 0
    max_bit = int(binary_string[position_index]) if is_limited else 1
    for current_bit in range(max_bit + 1):
        total_count += dp_recursive(position_index + 1, last_bit, is_limited and (current_bit == max_bit))
        if last_bit != current_bit:
            total_count += dp_recursive(position_index + 1, int(not last_bit), is_limited and (current_bit == max_bit))
    total_count %= MODULO
    memo_table[position_index][last_bit][is_limited] = total_count
    return total_count

print(dp_recursive(0, 0, 1))