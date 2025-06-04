import sys

def main():
    data = _read_input()
    processed = _process_data(data)
    _output_processed(processed)
    return 0

def _read_input():
    raw_lines = _read_stdin_lines()
    stripped_lines = _strip_lines(raw_lines)
    return stripped_lines

def _read_stdin_lines():
    return sys.stdin.readlines()

def _strip_lines(lines):
    return [_strip_line(line) for line in lines]

def _strip_line(line):
    return line.strip()

def _process_data(data):
    return _apply_proc(data)

def _apply_proc(data):
    return [_process_single_entry(passwd) for passwd in data if _is_hitofude(passwd)]

def _process_single_entry(passwd):
    return passwd

def _output_processed(processed):
    for entry in processed:
        _print_output(entry)

def _print_output(entry):
    print(entry)

def _is_hitofude(text):
    for first, second in _get_pair(text):
        if _is_second_empty(second):
            break
        if not _can_slide(first, second):
            return False
    return True

def _is_second_empty(second):
    return second == ''

def _get_pair(text):
    return _pair_generator(text)

def _pair_generator(text):
    pair_list = _reverse_list(list(text))
    while True:
        pair_length = len(pair_list)
        if _has_at_least_two_elements(pair_length):
            yield (_pop_last(pair_list), _get_last(pair_list))
        elif _has_exactly_one_element(pair_length):
            yield (_pop_last(pair_list), '')
        else:
            break

def _reverse_list(lst):
    lst.reverse()
    return lst

def _has_at_least_two_elements(n):
    return n >= 2

def _has_exactly_one_element(n):
    return n == 1

def _pop_last(lst):
    return lst.pop()

def _get_last(lst):
    return lst[-1]

def _can_slide(first, second):
    return _pair_in_allowed_pairs(first, second)

def _pair_in_allowed_pairs(first, second):
    return (first, second) in _get_allowed_pairs()

def _get_allowed_pairs():
    return _precomputed_pair()

def _precomputed_pair():
    if not hasattr(_precomputed_pair, 'cache'):
        _precomputed_pair.cache = _compute_matrix_pairs()
    return _precomputed_pair.cache

def _compute_matrix_pairs():
    matrix = _get_matrix()
    pairs = []
    for y, row in enumerate(matrix):
        for x, base in enumerate(row):
            pairs.extend(_get_neighbor_pairs(matrix, y, x, base))
    return pairs

def _get_matrix():
    return ["ABC", "DEF", "GHI"]

def _get_neighbor_pairs(matrix, y, x, base):
    pairs = []
    row = matrix[y]
    if _x_plus_one_in_range(x, row):
        pairs.append((base, row[x+1]))
    if _x_minus_one_in_range(x):
        pairs.append((base, row[x-1]))
    if _y_plus_one_in_range(y, matrix):
        pairs.append((base, matrix[y+1][x]))
    if _y_minus_one_in_range(y):
        pairs.append((base, matrix[y-1][x]))
    return pairs

def _x_plus_one_in_range(x, row):
    return x + 1 < len(row)

def _x_minus_one_in_range(x):
    return x - 1 >= 0

def _y_plus_one_in_range(y, matrix):
    return y + 1 < len(matrix)

def _y_minus_one_in_range(y):
    return y - 1 >= 0

if __name__ == '__main__':
    main()