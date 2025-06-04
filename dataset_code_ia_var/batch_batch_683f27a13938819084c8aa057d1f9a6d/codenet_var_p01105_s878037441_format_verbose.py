MASK_FULL_BITS = 65280
MASK_HIGH_BITS = 61680
MASK_ALT_BITS1 = 52428
MASK_ALT_BITS2 = 43690
MASK_ALL_ONES = 65535

queue_state_levels = [ [] for index in range(17) ]
queue_state_levels[1] = [MASK_FULL_BITS, MASK_HIGH_BITS, MASK_ALT_BITS1, MASK_ALT_BITS2]

level_mapping = {
    MASK_FULL_BITS: 1,
    MASK_HIGH_BITS: 1,
    MASK_ALT_BITS1: 1,
    MASK_ALT_BITS2: 1,
    MASK_ALL_ONES: 1,
    0: 1
}

history_pairs = []

get_level = level_mapping.get
add_to_history = history_pairs.append

for current_level in range(1, 16):

    current_queue = queue_state_levels[current_level]
    next_queue = queue_state_levels[current_level + 1]

    while current_queue:

        current_pattern = current_queue.pop()

        if level_mapping[current_pattern] < current_level:
            continue

        xor_pattern = current_pattern ^ MASK_ALL_ONES
        if current_level + 1 < get_level(xor_pattern, 17):
            level_mapping[xor_pattern] = current_level + 1
            if current_level < 15:
                next_queue.append(xor_pattern)

        if current_level < 13:
            difference_from_13 = 13 - current_level
            sum_with_3 = 3 + current_level

            for prev_pattern, prev_level in history_pairs:

                if prev_level < difference_from_13:
                    and_pattern = current_pattern & prev_pattern
                    if prev_level < get_level(and_pattern, 17) - sum_with_3:
                        level_mapping[and_pattern] = sum_with_3 + prev_level
                        queue_state_levels[sum_with_3 + prev_level].append(and_pattern)

                    xor_pattern = current_pattern ^ prev_pattern
                    if prev_level < get_level(xor_pattern, 17) - sum_with_3:
                        level_mapping[xor_pattern] = sum_with_3 + prev_level
                        queue_state_levels[sum_with_3 + prev_level].append(xor_pattern)

                elif prev_level == difference_from_13:
                    if (current_pattern & prev_pattern) not in level_mapping:
                        level_mapping[current_pattern & prev_pattern] = 16
                    if (current_pattern ^ prev_pattern) not in level_mapping:
                        level_mapping[current_pattern ^ prev_pattern] = 16
                else:
                    break

        if current_level < 7:
            add_to_history((current_pattern, current_level))

import sys

input_line = sys.stdin.read()
operation_string = input_line.replace("-", "~").replace("*", "&").replace("1e", "")
expressions = operation_string.split()[:-1]
mask_expressions = ["MASK_ALL_ONES&" + expr for expr in expressions]
eval_string = ",".join(mask_expressions)
mask_values = eval("[" + eval_string + "]")

output_levels = map(level_mapping.__getitem__, mask_values)
print(*output_levels, sep='\n')