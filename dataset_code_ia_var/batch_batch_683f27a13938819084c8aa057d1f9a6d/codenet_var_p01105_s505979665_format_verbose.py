initial_value_1 = 65280
initial_value_2 = 61680
initial_value_3 = 52428
initial_value_4 = 43690
final_mask = 65535

queue_by_step = [[] for step_index in range(17)]
queue_by_step[1] = [initial_value_1, initial_value_2, initial_value_3, initial_value_4]

visited_steps = {
    initial_value_1: 1,
    initial_value_2: 1,
    initial_value_3: 1,
    initial_value_4: 1,
    final_mask: 1,
    0: 1
}

history_stack = []

get_visited_step = visited_steps.get
push_to_history = history_stack.append

for current_step in range(1, 16):

    current_queue = queue_by_step[current_step]
    limit_for_q_r = 13 - current_step
    step_plus_three = current_step + 3
    next_step = current_step + 1
    pop_from_queue = current_queue.pop
    push_to_next_queue = queue_by_step[next_step].append

    while current_queue:

        pattern = pop_from_queue()

        if visited_steps[pattern] < current_step:
            continue

        if next_step < get_visited_step(pattern ^ final_mask, 17):
            visited_steps[pattern ^ final_mask] = next_step
            if current_step < 12:
                push_to_next_queue(pattern ^ final_mask)

        if current_step < 13:
            for queued_pattern, queued_step in history_stack:
                if queued_step < limit_for_q_r:

                    if step_plus_three + queued_step < get_visited_step(pattern & queued_pattern, 17):
                        visited_steps[pattern & queued_pattern] = step_plus_three + queued_step
                        queue_by_step[step_plus_three + queued_step].append(pattern & queued_pattern)

                    if step_plus_three + queued_step < get_visited_step(pattern ^ queued_pattern, 17):
                        visited_steps[pattern ^ queued_pattern] = step_plus_three + queued_step
                        queue_by_step[step_plus_three + queued_step].append(pattern ^ queued_pattern)

                elif queued_step == limit_for_q_r:

                    if pattern & queued_pattern not in visited_steps:
                        visited_steps[pattern & queued_pattern] = 16

                    if pattern ^ queued_pattern not in visited_steps:
                        visited_steps[pattern ^ queued_pattern] = 16

                else:
                    break

            if current_step < 7:
                push_to_history( (pattern, current_step) )


import sys

user_input_text = sys.stdin.read()
transformed_input_text = (
    user_input_text
    .replace('-', '~')
    .replace('*', '&')
    .replace('1e', '')
)

input_masks = transformed_input_text.split()[:-1]

eval_expression = 'final_mask&' + ',final_mask&'.join(input_masks)
masks_to_evaluate = eval(eval_expression)

for mask in masks_to_evaluate:
    print(visited_steps[mask])