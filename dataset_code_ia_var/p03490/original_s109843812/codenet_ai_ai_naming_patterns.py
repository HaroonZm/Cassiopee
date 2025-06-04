import sys
import numpy as np

input_command_sequence = raw_input()
input_target_x, input_target_y = [int(item) for item in raw_input().split(" ")]

command_sequence_augmented = input_command_sequence + "T"

forward_move_segment_list = []
turn_move_segment_list = []
current_segment_length = 0
is_forward_turn = 0

for command_char in command_sequence_augmented:
    if command_char == "F":
        current_segment_length += 1
    elif command_char == "T":
        if is_forward_turn == 0:
            forward_move_segment_list.append(current_segment_length)
        else:
            turn_move_segment_list.append(current_segment_length)
        is_forward_turn ^= 1
        current_segment_length = 0

initial_forward_segment = forward_move_segment_list.pop(0)

relative_target_x = abs(input_target_x - initial_forward_segment)
relative_target_y = abs(input_target_y)

forward_target_sum = sum(forward_move_segment_list) - relative_target_x
turn_target_sum = sum(turn_move_segment_list) - relative_target_y

def is_reachable_segment_sum(segment_list, segment_target):
    dynamic_state = np.zeros((len(segment_list), segment_target + 1))
    dynamic_state[:, 0] = 1
    for segment_index in xrange(len(segment_list)):
        segment_value = segment_list[segment_index]
        if segment_index == 0:
            dynamic_state[segment_index, 2 * segment_value : 2 * segment_value + 1] = 1
        else:
            dynamic_state[segment_index] += dynamic_state[segment_index - 1]
            if segment_value > 0:
                dynamic_state[segment_index, 2 * segment_value :] += dynamic_state[segment_index - 1, :-2 * segment_value]
        if dynamic_state[segment_index, -1] > 0:
            dynamic_state[-1, -1] = 1
            break
    return (dynamic_state[-1, -1] > 0)

if (forward_target_sum < 0) or (turn_target_sum < 0):
    print "No"
    sys.exit()
else:
    if (forward_target_sum > 0):
        if not is_reachable_segment_sum(forward_move_segment_list, forward_target_sum):
            print "No"
            sys.exit()
    if (turn_target_sum > 0):
        if not is_reachable_segment_sum(turn_move_segment_list, turn_target_sum):
            print "No"
            sys.exit()
    print "Yes"