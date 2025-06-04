def rdp_calculate_trace(depth_count: int, position_index: int) -> list:
    def recursive_trace(node_count: int, node_index: int) -> list:
        if node_count == 1:
            return []
        if node_index <= node_count // 2:
            trace_list = recursive_trace(node_count // 2, (node_count // 2) - node_index + 1)
            trace_list.append(node_index)
            return trace_list
        else:
            trace_list = recursive_trace(node_count // 2, node_index - (node_count // 2))
            trace_list.append(node_index)
            return trace_list
    return recursive_trace(2 ** depth_count, position_index)

def rdp_read_input() -> bool:
    global current_depth, current_index_i, current_index_j
    current_depth, current_index_i, current_index_j = map(int, input().split())
    if current_depth == current_index_i == current_index_j == 0:
        return False
    return True

if __name__ == '__main__':
    while rdp_read_input():
        result_sequence = []
        temp_j = current_index_j
        for level_index, node_value in zip(range(current_depth), rdp_calculate_trace(current_depth, current_index_i)):
            mid_value = (2 ** (level_index + 1)) // 2
            segment_size = 2 ** (current_depth - level_index)
            half_segment = segment_size // 2
            if node_value <= mid_value:
                if temp_j <= half_segment:
                    result_sequence.append('L')
                    temp_j = half_segment - temp_j + 1
                else:
                    result_sequence.append('R')
                    temp_j = segment_size - temp_j + 1
            else:
                if temp_j <= half_segment:
                    result_sequence.append('R')
                else:
                    result_sequence.append('L')
                    temp_j = temp_j - half_segment
        print(''.join(result_sequence))