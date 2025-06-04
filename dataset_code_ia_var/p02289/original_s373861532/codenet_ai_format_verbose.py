def percolate_up_max_heap(heap, start_position):
    """
    Move the value at start_position up the max-heap until the heap property is restored.
    """
    value_to_insert = heap[start_position]
    current_position = start_position
    
    while current_position > 0:
        parent_position = (current_position - 1) // 2
        parent_value = heap[parent_position]
        
        if parent_value < value_to_insert:
            heap[current_position] = parent_value
            current_position = parent_position
            continue
        break
    
    heap[current_position] = value_to_insert

def percolate_down_max_heap(heap, start_position):
    """
    Move the value at start_position down the max-heap until the heap property is restored.
    """
    end_position = len(heap)
    value_to_move = heap[start_position]
    current_position = start_position
    left_child_position = 2 * current_position + 1

    while left_child_position < end_position:
        right_child_position = left_child_position + 1
        
        if right_child_position < end_position and heap[right_child_position] > heap[left_child_position]:
            swap_child_position = right_child_position
        else:
            swap_child_position = left_child_position
        
        swap_child_value = heap[swap_child_position]
        
        if value_to_move >= swap_child_value:
            break
        
        heap[current_position] = swap_child_value
        current_position = swap_child_position
        left_child_position = 2 * current_position + 1

    heap[current_position] = value_to_move

def insert_into_max_heap(heap, value_to_insert):
    """
    Insert a new value into the max-heap and maintain the heap property.
    """
    heap.append(value_to_insert)
    percolate_up_max_heap(heap, len(heap) - 1)

def extract_max_from_heap(heap):
    """
    Remove and return the maximum value from the max-heap.
    """
    last_value = heap.pop()
    if heap:
        maximum_value = heap[0]
        heap[0] = last_value
        percolate_down_max_heap(heap, 0)
        return maximum_value
    return last_value

import sys

max_heap = []

output_values = []

for input_line in sys.stdin.readlines():
    if input_line[0] == 'i':
        value_to_add = int(input_line[7:])
        insert_into_max_heap(max_heap, value_to_add)
    elif input_line[1] == 'x':
        output_values.append(extract_max_from_heap(max_heap))
    else:
        pass

print(*output_values, sep='\n')