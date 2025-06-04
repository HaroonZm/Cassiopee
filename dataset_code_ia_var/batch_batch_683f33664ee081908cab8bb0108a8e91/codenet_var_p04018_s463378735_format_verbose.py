import sys

standard_input_binary = sys.stdin.buffer.read
input_line_binary = sys.stdin.buffer.readline
input_lines_binary = sys.stdin.buffer.readlines

word_bytes = standard_input_binary().rstrip()

length_of_word = len(word_bytes)

def compute_Z_array(string_bytes):
    length_of_string = len(string_bytes)
    z_array = [0] * length_of_string
    z_array[0] = length_of_string
    match_length = 0
    i = 1
    while i < length_of_string:
        while i + match_length < length_of_string and string_bytes[match_length] == string_bytes[i + match_length]:
            match_length += 1
        z_array[i] = match_length
        if match_length == 0:
            i += 1
            continue
        k = 1
        while i + k < length_of_string and k + z_array[k] < match_length:
            z_array[i + k] = z_array[k]
            k += 1
        i += k
        match_length -= k
    return z_array

def compute_left_periodicity_flags(sequence_bytes):
    z_values = compute_Z_array(sequence_bytes)
    periodicity_flags = [False] * length_of_word
    for period in range(1, length_of_word // 2 + 10):
        for start_index in range(period, length_of_word, period):
            if z_values[start_index] >= period:
                periodicity_flags[period + start_index - 1] = True
            else:
                break
    return periodicity_flags

left_periodic_flags = compute_left_periodicity_flags(word_bytes)
right_periodic_flags = compute_left_periodicity_flags(word_bytes[::-1])[::-1]

if not left_periodic_flags[-1]:
    output_tuple = (1, 1)
elif len(set(word_bytes)) == 1:
    output_tuple = (length_of_word, 1)
else:
    non_periodic_count = sum(
        not (left_flag or right_flag_next)
        for left_flag, right_flag_next in zip(left_periodic_flags, right_periodic_flags[1:])
    )
    output_tuple = (2, non_periodic_count)

print('\n'.join(map(str, output_tuple)))