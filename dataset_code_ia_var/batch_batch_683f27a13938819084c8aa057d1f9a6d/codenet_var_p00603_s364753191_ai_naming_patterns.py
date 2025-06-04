while True:
    try:
        num_total, num_rounds = map(int, raw_input().split())
        if num_rounds == 1:
            round_counts = [int(raw_input())]
        else:
            round_counts = map(int, raw_input().split())
    except:
        break
    sequence_all = range(num_total)
    sequence_a = sequence_all[num_total//2:]
    sequence_b = sequence_all[:num_total//2]
    sequence_temp = []
    for round_index in range(num_rounds):
        count = round_counts[round_index]
        while sequence_a or sequence_b:
            sequence_temp += sequence_a[:count] + sequence_b[:count]
            sequence_a = sequence_a[count:]
            sequence_b = sequence_b[count:]
        sequence_a = sequence_temp[num_total//2:]
        sequence_b = sequence_temp[:num_total//2]
        sequence_temp = []
    print sequence_b[-1]