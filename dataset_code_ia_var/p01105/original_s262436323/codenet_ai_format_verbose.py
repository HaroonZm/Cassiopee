initial_bitmask_a = 65280
initial_bitmask_b = 61680
initial_bitmask_c = 52428
initial_bitmask_d = 43690
initial_bitmask_e = 65535

from heapq import heappush, heappop

all_initial_bitmasks = [
    initial_bitmask_a,
    initial_bitmask_b,
    initial_bitmask_c,
    initial_bitmask_d,
    initial_bitmask_e,
    0
]

priority_queue = [
    (1, bitmask) for bitmask in all_initial_bitmasks
]

minimum_steps_for_bitmask = {
    bitmask: 1 for bitmask in all_initial_bitmasks
}

processed_pairs = []

while priority_queue:
    current_steps, current_bitmask = heappop(priority_queue)

    if minimum_steps_for_bitmask[current_bitmask] < current_steps:
        continue

    toggled_bitmask = current_bitmask ^ initial_bitmask_e
    steps_after_toggle = current_steps + 1

    if steps_after_toggle < minimum_steps_for_bitmask.get(toggled_bitmask, 17):
        minimum_steps_for_bitmask[toggled_bitmask] = steps_after_toggle
        if steps_after_toggle < 16:
            heappush(priority_queue, (steps_after_toggle, toggled_bitmask))

    if current_steps + 3 < 16:
        for reference_bitmask, reference_steps in processed_pairs:
            combined_steps = current_steps + reference_steps + 3

            if combined_steps <= 16:
                and_result_bitmask = current_bitmask & reference_bitmask
                xor_result_bitmask = current_bitmask ^ reference_bitmask

                if combined_steps < minimum_steps_for_bitmask.get(and_result_bitmask, 17):
                    minimum_steps_for_bitmask[and_result_bitmask] = combined_steps
                    if combined_steps < 16:
                        heappush(priority_queue, (combined_steps, and_result_bitmask))

                if combined_steps < minimum_steps_for_bitmask.get(xor_result_bitmask, 17):
                    minimum_steps_for_bitmask[xor_result_bitmask] = combined_steps
                    if combined_steps < 16:
                        heappush(priority_queue, (combined_steps, xor_result_bitmask))
            else:
                break

    if current_steps < 7:
        processed_pairs.append((current_bitmask, current_steps))

# Input parsing and processing part

input_text = open(0).read()
parsed_input_text = input_text.replace("-", "~").replace("*", "&").replace("1", "e")
input_elements = parsed_input_text.split()[:-1]

expression_pieces = [
    "initial_bitmask_e&" + item for item in input_elements
]

final_expression = ",".join(expression_pieces)
evaluated_bitmasks = eval(final_expression)

for bitmask in map(minimum_steps_for_bitmask.__getitem__, evaluated_bitmasks):
    print(bitmask)