def count_hits_and_blows(seq_a, seq_b):
    count_hit = 0
    count_blow = 0
    for idx_a in range(4):
        for idx_b in range(4):
            if seq_a[idx_a] == seq_b[idx_b]:
                if idx_a == idx_b:
                    count_hit += 1
                else:
                    count_blow += 1
    return [count_hit, count_blow]

while True:
    try:
        input_seq_a = input().split()
        input_seq_b = input().split()
        result_hits_blows = count_hits_and_blows(input_seq_a, input_seq_b)
        print(result_hits_blows[0], result_hits_blows[1])
    except:
        break