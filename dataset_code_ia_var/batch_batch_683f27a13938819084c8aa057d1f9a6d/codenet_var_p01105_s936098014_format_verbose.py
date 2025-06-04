symbol_mask_1 = 65280
symbol_mask_2 = 61680
symbol_mask_3 = 52428
symbol_mask_4 = 43690
symbol_mask_all = 65535

from heapq import heappush, heappop

base_bit_masks = [
    symbol_mask_1,
    symbol_mask_2,
    symbol_mask_3,
    symbol_mask_4,
    symbol_mask_all,
    0
]

queue_bit_distance = [(1, bit_pattern) for bit_pattern in base_bit_masks]

bit_pattern_to_steps = {bit_pattern: 1 for bit_pattern in base_bit_masks}

history_processed = []

get_step_count = bit_pattern_to_steps.get

append_to_history = history_processed.append

while queue_bit_distance:
    current_step_count, current_bit_pattern = heappop(queue_bit_distance)
    
    if bit_pattern_to_steps[current_bit_pattern] < current_step_count:
        continue
    
    next_step_flip = current_step_count + 1
    flipped_bit_pattern = current_bit_pattern ^ symbol_mask_all
    
    if next_step_flip < get_step_count(flipped_bit_pattern, 17):
        bit_pattern_to_steps[flipped_bit_pattern] = next_step_flip
        if next_step_flip < 16:
            heappush(queue_bit_distance, (next_step_flip, flipped_bit_pattern))
    
    next_step_and_xor = current_step_count + 3
    if next_step_and_xor < 16:
        for prior_bit_pattern, prior_step_count in history_processed:
            total_step_count = current_step_count + prior_step_count + 3
            
            if total_step_count <= 16:
                and_pattern = current_bit_pattern & prior_bit_pattern
                if total_step_count < get_step_count(and_pattern, 17):
                    bit_pattern_to_steps[and_pattern] = total_step_count
                    if total_step_count < 16:
                        heappush(queue_bit_distance, (total_step_count, and_pattern))
                
                xor_pattern = current_bit_pattern ^ prior_bit_pattern
                if total_step_count < get_step_count(xor_pattern, 17):
                    bit_pattern_to_steps[xor_pattern] = total_step_count
                    if total_step_count < 16:
                        heappush(queue_bit_distance, (total_step_count, xor_pattern))
            else:
                break
    
    if current_step_count < 7:
        append_to_history((current_bit_pattern, current_step_count))

# Input Parsing and Output
input_mask_line = open(0).read()
input_masks_as_strings = input_mask_line.replace("-", "~").replace("*", "&").replace("1", "e").split()[:-1]
input_masks = eval("symbol_mask_all & %s" % ", symbol_mask_all & ".join(input_masks_as_strings))

for mask in input_masks:
    print(bit_pattern_to_steps[mask])