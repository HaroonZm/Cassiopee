def process_sequence():
    input_m_value, input_k_value = map(int, input().split())
    sequence_limit = 1 << input_m_value
    if input_k_value >= sequence_limit:
        print(-1)
        return
    if input_m_value == 0:
        print('0 0')
        return
    if input_m_value == 1:
        if input_k_value == 0:
            print('0 0 1 1')
        else:
            print(-1)
        return
    result_sequence = [0] * (2 * sequence_limit)
    result_sequence[0] = input_k_value
    result_sequence[sequence_limit] = input_k_value
    for index_lower in range(input_k_value):
        result_sequence[index_lower + 1] = index_lower
        result_sequence[-index_lower - 1] = index_lower
    for index_upper in range(input_k_value + 1, sequence_limit):
        result_sequence[index_upper] = index_upper
        result_sequence[-index_upper] = index_upper
    print(' '.join(map(str, result_sequence)))
process_sequence()