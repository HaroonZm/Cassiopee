def main():
    
    length_sequence_s, length_sequence_t = map(int, input().split())
    sequence_s = input()
    sequence_t = input()

    very_large_negative_value = -10**18

    dp_state_zero = [[0] * (length_sequence_t + 1) for _ in range(length_sequence_s + 1)]
    dp_state_one = [[very_large_negative_value] * (length_sequence_t + 1) for _ in range(length_sequence_s + 1)]

    for index_s in range(length_sequence_s + 1):
        for index_t in range(length_sequence_t + 1):

            current_value_state_zero = dp_state_zero[index_s][index_t]
            current_value_state_one = dp_state_one[index_s][index_t]

            if index_s < length_sequence_s:
                if sequence_s[index_s] == 'I':
                    dp_state_one[index_s + 1][index_t] = max(dp_state_one[index_s + 1][index_t], current_value_state_zero + 1)
                else:
                    dp_state_zero[index_s + 1][index_t] = max(dp_state_zero[index_s + 1][index_t], current_value_state_one + 1)

            if index_t < length_sequence_t:
                if sequence_t[index_t] == 'I':
                    dp_state_one[index_s][index_t + 1] = max(dp_state_one[index_s][index_t + 1], current_value_state_zero + 1)
                else:
                    dp_state_zero[index_s][index_t + 1] = max(dp_state_zero[index_s][index_t + 1], current_value_state_one + 1)

    maximum_value_in_state_one = max(max(row) for row in dp_state_one)
    print(max(maximum_value_in_state_one, 0))


main()