import bisect

input_count = int(input())
input_sequence = [int(input()) for _ in range(input_count)]

def compute_lis_length_and_sequence(sequence):
    seq_length = len(sequence)
    max_placeholder = max(sequence) + 10
    lis_dp = [max_placeholder] * seq_length
    lis_current_length = 0

    for idx in range(seq_length):
        insert_pos = bisect.bisect_left(lis_dp, sequence[idx])
        if insert_pos == lis_current_length:
            lis_current_length += 1
        lis_dp[insert_pos] = sequence[idx]

    return lis_current_length, lis_dp

lis_length, _ = compute_lis_length_and_sequence(input_sequence)
print(lis_length)