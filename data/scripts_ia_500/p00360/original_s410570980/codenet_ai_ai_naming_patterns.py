import sys

def main():
    read_integer = lambda: int(sys.stdin.readline())
    read_string = lambda: sys.stdin.readline().rstrip()

    input_string = read_string()
    string_length = len(input_string)
    max_removals = read_integer()

    def char_to_index(char):
        return ord(char) - ord('a')

    fenwick_tree = [0] * (string_length + 1)

    def fenwick_add(index):
        while index <= string_length:
            fenwick_tree[index] += 1
            index += index & (-index)

    def fenwick_sum(index):
        total = 0
        while index > 0:
            total += fenwick_tree[index]
            index -= index & (-index)
        return total

    removed_flags = [0] * string_length
    top_positions = [-1] * 26
    next_positions = [-1] * string_length
    last_positions = [-1] * 26

    for position in range(string_length):
        char_index = char_to_index(input_string[position])
        if last_positions[char_index] >= 0:
            next_positions[last_positions[char_index]] = position
        last_positions[char_index] = position
        if top_positions[char_index] < 0:
            top_positions[char_index] = position

    result_chars = []
    remaining_removals = max_removals

    while remaining_removals > 0:
        for char_code in range(26):
            if top_positions[char_code] < 0:
                continue
            pos = top_positions[char_code]
            cost = pos - fenwick_sum(pos + 1)
            if cost <= remaining_removals:
                result_chars.append(chr(ord('a') + char_code))
                removed_flags[pos] = 1
                remaining_removals -= cost
                top_positions[char_code] = next_positions[pos]
                fenwick_add(pos + 1)
                break
        else:
            break

    for position in range(string_length):
        if removed_flags[position] == 0:
            result_chars.append(input_string[position])

    print(''.join(result_chars))

if __name__ == '__main__':
    main()