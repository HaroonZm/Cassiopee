import sys
read_input = lambda: sys.stdin.readline().rstrip()
total_length, subseq_sum_limit = map(int, read_input().split())
modulo_value = 998244353

perm_count = [[0] * (2 * idx + 1) for idx in range(total_length + 1)]
perm_count[0][0] = 1
valid_perm_total = [0] * (total_length + 1)

for curr_len in range(total_length):
    for curr_sum in range(curr_len, 2 * curr_len + 1):
        next_len = curr_len + 1
        next_sum_1 = curr_sum + 1
        next_sum_2 = curr_sum + 2
        perm_count[next_len][next_sum_1] += perm_count[curr_len][curr_sum]
        perm_count[next_len][next_sum_2] += perm_count[curr_len][curr_sum]
        if perm_count[next_len][next_sum_1] >= modulo_value:
            perm_count[next_len][next_sum_1] -= modulo_value
        if perm_count[next_len][next_sum_2] >= modulo_value:
            perm_count[next_len][next_sum_2] -= modulo_value

for seq_len in range(total_length + 1):
    for seq_sum in range(seq_len, min(2 * seq_len + 1, subseq_sum_limit)):
        valid_perm_total[seq_len] += perm_count[seq_len][seq_sum]

if subseq_sum_limit % 2 == 1:
    for seq_len in range(subseq_sum_limit, total_length + 1):
        valid_perm_total[seq_len] += 1

for split_point in range(1, subseq_sum_limit):
    auxiliary_val = subseq_sum_limit - 1 - 2 * split_point
    if auxiliary_val < 0:
        continue
    for start_seq in range((auxiliary_val + 1) // 2, auxiliary_val + 1):
        target_len = start_seq + 2 * split_point
        if target_len > total_length:
            break
        valid_perm_total[target_len] += perm_count[start_seq][auxiliary_val]
        if valid_perm_total[target_len] >= modulo_value:
            valid_perm_total[target_len] -= modulo_value

final_answer = 0
for idx, val in enumerate(valid_perm_total):
    final_answer = (final_answer + val * perm_count[-1][-1 - idx]) % modulo_value

print(final_answer)