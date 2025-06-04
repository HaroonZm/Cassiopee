from collections import Counter

def is_valid_string():
    input_string = raw_input()
    char_counter = Counter(input_string)
    input_length = len(input_string)
    if input_length == 1:
        return True

    freq_items = sorted(char_counter.items(), key=lambda item: -item[1])

    freq_kind_count = len(freq_items)
    if freq_kind_count == 2:
        return input_length == 2

    if freq_kind_count == 1:
        return False

    highest_freq = freq_items[0][1]
    sum_other_freqs = sum(freq for char, freq in freq_items[1:])
    return sum_other_freqs >= (highest_freq - 1) * 2

print 'YES' if is_valid_string() else 'NO'