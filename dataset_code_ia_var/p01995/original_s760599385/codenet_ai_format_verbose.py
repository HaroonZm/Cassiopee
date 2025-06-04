def main():
    
    from bisect import bisect_left as bisect_left_search
    from bisect import bisect_right as bisect_right_search
    
    input_string = input()
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    input_length = len(input_string)
    
    letter_to_index = {character: index for index, character in enumerate(alphabet)}
    
    positions_by_letter = [[] for _ in range(26)]
    
    modulo = 10 ** 9 + 7
    
    for position in range(input_length):
        letter_index = letter_to_index[input_string[position]]
        positions_by_letter[letter_index].append(position)
    
    dynamic_programming_table = [[0] * (input_length + 1) for _ in range(input_length + 1)]
    dynamic_programming_table[0][input_length] = 1
    
    total_answer = 0
    
    for start_index in range(input_length):
        for end_index in range(start_index + 1, input_length + 1):
            
            current_value = dynamic_programming_table[start_index][end_index]
            
            if current_value == 0:
                continue
            
            for alphabet_index in range(26):
                left_position = bisect_left_search(positions_by_letter[alphabet_index], start_index)
                right_position = bisect_right_search(positions_by_letter[alphabet_index], end_index - 1) - 1
                
                if left_position > right_position:
                    continue
                
                total_answer += current_value
                
                if left_position < right_position:
                    left_letter_index = positions_by_letter[alphabet_index][left_position]
                    right_letter_index = positions_by_letter[alphabet_index][right_position]
                    dynamic_programming_table[left_letter_index + 1][right_letter_index] = (
                        dynamic_programming_table[left_letter_index + 1][right_letter_index] + current_value
                    ) % modulo
            
            total_answer = total_answer % modulo
    
    total_answer = (total_answer + sum([sum(row) % modulo for row in dynamic_programming_table]) + modulo - 1) % modulo
    
    print(total_answer)
    
if __name__ == '__main__':
    main()