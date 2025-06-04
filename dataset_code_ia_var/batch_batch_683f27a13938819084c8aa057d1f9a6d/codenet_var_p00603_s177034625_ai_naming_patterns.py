try:
    while True:
        input_total_elements, input_num_operations = map(int, input().split())
        operation_chunk_sizes = list(map(int, input().split()))
        sequence_indices = list(range(input_total_elements))
        for current_chunk_size in operation_chunk_sizes:
            left_partition_size = input_total_elements // 2
            right_partition_size = input_total_elements - left_partition_size
            right_partition = sequence_indices[left_partition_size:]
            left_partition = sequence_indices[:left_partition_size]
            merged_sequence = []
            right_pointer = left_pointer = 0
            while right_pointer < right_partition_size and left_pointer < left_partition_size:
                merged_sequence.extend(right_partition[right_pointer:min(right_pointer+current_chunk_size, right_partition_size)])
                right_pointer += current_chunk_size
                merged_sequence.extend(left_partition[left_pointer:min(left_pointer+current_chunk_size, left_partition_size)])
                left_pointer += current_chunk_size
            if right_pointer < right_partition_size:
                merged_sequence.extend(right_partition[right_pointer:])
            if left_pointer < left_partition_size:
                merged_sequence.extend(left_partition[left_pointer:])
            sequence_indices = merged_sequence
        print(sequence_indices[-1])
except EOFError:
    pass