while True:
    try:
        total_cards, num_iterations = map(int, raw_input().split())
    except EOFError:
        break
    split_counts = map(int, raw_input().split())
    sequence_indices = range(total_cards)
    for split_count in split_counts:
        upper_half = sequence_indices[total_cards // 2:]
        lower_half = sequence_indices[:total_cards // 2]
        merged_sequence = []
        while upper_half != [] or lower_half != []:
            if split_count <= len(upper_half):
                merged_sequence += upper_half[:split_count]
                upper_half = upper_half[split_count:]
            else:
                merged_sequence += upper_half[:]
                upper_half = []
            if split_count <= len(lower_half):
                merged_sequence += lower_half[:split_count]
                lower_half = lower_half[split_count:]
            else:
                merged_sequence += lower_half[:]
                lower_half = []
        sequence_indices = merged_sequence[:]
    print merged_sequence[-1]