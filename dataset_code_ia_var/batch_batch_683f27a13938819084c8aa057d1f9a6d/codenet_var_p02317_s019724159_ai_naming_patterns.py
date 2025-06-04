from bisect import bisect_left

CONSTANT_INF = 10 ** 18

input_count = int(input())
input_sequence = [int(input()) for _ in range(input_count)]

lis_table = [CONSTANT_INF] * (input_count + 1)
lis_table[0] = -1

for idx in range(input_count):
    position = bisect_left(lis_table, input_sequence[idx])
    lis_table[position] = input_sequence[idx]

longest_length = -1
for length in range(input_count + 1):
    if lis_table[length] == CONSTANT_INF:
        break
    longest_length = length

print(longest_length)