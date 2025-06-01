import sys

def count_matching_signboards(target_string, total_signboards):
    match_count = 0
    for _ in range(total_signboards):
        current_signboard = input()
        found_match = False
        starting_indices = [index for index, char in enumerate(current_signboard) if char == target_string[0]]
        for start_index in starting_indices:
            if found_match:
                break
            gap_length = 1
            while True:
                extracted_substring = current_signboard[start_index::gap_length]
                if len(extracted_substring) < len(target_string):
                    break
                if extracted_substring.startswith(target_string):
                    found_match = True
                    break
                gap_length += 1
        match_count += found_match
    return match_count

def main(args):
    total_lines = int(input())
    search_string = input()
    result = count_matching_signboards(search_string, total_lines)
    print(result)

if __name__ == '__main__':
    main(sys.argv[1:])