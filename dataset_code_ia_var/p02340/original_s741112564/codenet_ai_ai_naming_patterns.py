input_total, input_parts = map(int, input().split())
modulus_constant = 10**9 + 7

dp_table = [[0] * (input_parts + 1) for idx_total in range(input_total + 1)]

for idx_total in range(input_total + 1):
    dp_table[idx_total][1] = 1

for idx_parts in range(1, input_parts + 1):
    dp_table[0][idx_parts] = 1

for idx_total in range(1, input_total + 1):
    for idx_parts in range(1, input_parts + 1):
        if idx_total >= idx_parts:
            dp_table[idx_total][idx_parts] = (dp_table[idx_total - idx_parts][idx_parts] + dp_table[idx_total][idx_parts - 1]) % modulus_constant
        else:
            dp_table[idx_total][idx_parts] = dp_table[idx_total][idx_total]

print(dp_table[input_total][input_parts])