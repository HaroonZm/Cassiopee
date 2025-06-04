MODULO = 10**9 + 7
input_n = int(input())

def get_bit_at_position(bit_position):
    return (input_n >> bit_position) & 1

DP_SIZE = 61
STATE_COUNT = 3

dp_table = [[0 for _ in range(STATE_COUNT)] for _ in range(DP_SIZE)]
dp_table[DP_SIZE - 1][0] = 1

for bit_idx in range(DP_SIZE - 2, -1, -1):
    for prev_state in range(STATE_COUNT):
        for k_state in range(STATE_COUNT):
            next_state = min(2, 2 * prev_state + get_bit_at_position(bit_idx) - k_state)
            if next_state >= 0:
                dp_table[bit_idx][next_state] += dp_table[bit_idx + 1][prev_state]

result_total = sum(dp_table[0]) % MODULO
print(result_total)