from bisect import bisect_left as bl, bisect_right as br
import fileinput

CONST_MODULO = 1000000007
global_total_entries = 0

def input_process():
    input_iterator = fileinput.input()
    global global_total_entries
    global_total_entries = int(next(input_iterator))
    entity_infos = [None] * global_total_entries
    for idx_entry in range(global_total_entries):
        entry_x, entry_v = next(input_iterator).split()
        entity_infos[idx_entry] = (int(entry_x), int(entry_v))
    return entity_infos

def segment_build(entity_infos):
    segment_indices = [-1] * (global_total_entries + 1)
    segment_velocity_max = [0] * global_total_entries
    segment_velocity_min = [CONST_MODULO] * (global_total_entries + 1)
    for idx_max in range(global_total_entries):
        segment_velocity_max[idx_max] = max(segment_velocity_max[idx_max - 1], entity_infos[idx_max][1])
    for idx_min in range(global_total_entries - 1, -1, -1):
        segment_velocity_min[idx_min] = min(segment_velocity_min[idx_min + 1], entity_infos[idx_min][1])
    for idx_block in range(global_total_entries):
        current_velocity = entity_infos[idx_block][1]
        start_idx = bl(segment_velocity_max, current_velocity)
        end_idx = br(segment_velocity_min, current_velocity) - 1
        segment_indices[end_idx] = max(segment_indices[end_idx], start_idx)
    return segment_indices

def total_possibilities(segment_indices):
    possibilities_count = [1] * (global_total_entries + 2)
    current_zero_position = -2
    for current_idx in range(global_total_entries):
        current_result = 2 * possibilities_count[current_idx - 1]
        while current_zero_position < segment_indices[current_idx] - 1:
            current_result -= possibilities_count[current_zero_position]
            current_zero_position += 1
        possibilities_count[current_idx] = current_result % CONST_MODULO
    return possibilities_count[global_total_entries - 1]

def main_execution():
    processed_infos = input_process()
    processed_infos.sort()
    segments = segment_build(processed_infos)
    return total_possibilities(segments)

if __name__ == '__main__':
    print(main_execution())