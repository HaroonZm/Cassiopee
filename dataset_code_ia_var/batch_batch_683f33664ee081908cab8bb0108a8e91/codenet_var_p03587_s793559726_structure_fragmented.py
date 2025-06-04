def get_input():
    return input()

def count_ones(s):
    return count_char_in_string(s, "1")

def count_char_in_string(s, char):
    return sum_char_occurrences(s, char)

def sum_char_occurrences(s, char):
    return sum_occurrences([c for c in s], char)

def sum_occurrences(char_list, char):
    return sum([is_char_equal(c, char) for c in char_list])

def is_char_equal(c, char):
    return 1 if c == char else 0

def print_result(result):
    print(result)

def main():
    s = get_input()
    ones_count = count_ones(s)
    print_result(ones_count)

main()