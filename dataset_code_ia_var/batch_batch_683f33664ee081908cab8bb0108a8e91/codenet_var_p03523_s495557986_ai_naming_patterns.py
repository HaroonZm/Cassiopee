import sys

def read_input_line():
    return sys.stdin.readline().rstrip()

def get_valid_patterns():
    return [
        "AKIHABARA",
        "KIHABARA",
        "AKIHBARA",
        "AKIHABRA",
        "AKIHABAR",
        "KIHBARA",
        "KIHABRA",
        "KIHABAR",
        "AKIHBRA",
        "AKIHBAR",
        "AKIHABR",
        "KIHBRA",
        "KIHBAR",
        "KIHABR",
        "AKIHBR",
        "KIHBR",
    ]

def is_pattern_valid(candidate_pattern, valid_pattern_list):
    for valid_pattern in valid_pattern_list:
        if candidate_pattern == valid_pattern:
            return True
    return False

def display_result(is_valid):
    if is_valid:
        print("YES")
    else:
        print("NO")

def process_main():
    input_pattern = read_input_line()
    pattern_list = get_valid_patterns()
    validity = is_pattern_valid(input_pattern, pattern_list)
    display_result(validity)

if __name__ == "__main__":
    process_main()