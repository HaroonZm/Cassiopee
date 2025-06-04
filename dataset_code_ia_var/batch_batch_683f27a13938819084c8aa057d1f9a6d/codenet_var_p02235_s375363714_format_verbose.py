def compute_longest_common_subsequence_length(source_string, target_string):
    
    subsequence_indices_in_source = []
    
    for target_character in target_string:
        
        previous_source_index = -1
        
        for subsequence_position, current_index_in_source in enumerate(subsequence_indices_in_source):
            
            found_source_index = source_string.find(target_character, previous_source_index + 1)
            
            if found_source_index < 0:
                break
            
            subsequence_indices_in_source[subsequence_position] = min(current_index_in_source, found_source_index)
            
            previous_source_index = current_index_in_source
        
        else:
            found_source_index = source_string.find(target_character, previous_source_index + 1)
            
            if found_source_index >= 0:
                subsequence_indices_in_source.append(found_source_index)
    
    return len(subsequence_indices_in_source)


def main():
    
    number_of_queries = int(input())
    
    for _ in range(number_of_queries):
        
        input_source_string = input()
        input_target_string = input()
        
        longest_subsequence_length = compute_longest_common_subsequence_length(
            input_source_string,
            input_target_string
        )
        
        print(longest_subsequence_length)


if __name__ == "__main__":
    
    main()