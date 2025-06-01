import sys
sys.setrecursionlimit(10**6)

height, num_positions = map(int, input().split())
position_bitmasks = [0] * height

for position_index in range(num_positions):
    coord_x, coord_y = map(int, input().split())
    position_bitmasks[coord_y] |= 1 << coord_x

memoization_table = [[-1] * 16 for _ in range(height)]
for state_index in range(16):
    memoization_table[height - 1][state_index] = 0

def depth_first_search(row_index, current_state):
    if memoization_table[row_index][current_state] != -1:
        return memoization_table[row_index][current_state]
    
    next_row_bitmask = position_bitmasks[row_index + 1]
    combined_state = current_state | next_row_bitmask
    
    max_rectangles = depth_first_search(row_index + 1, next_row_bitmask)
    
    if (combined_state & 0b0011) == 0:
        max_rectangles = max(max_rectangles, depth_first_search(row_index + 1, next_row_bitmask | 0b0011) + 1)
    if (combined_state & 0b0110) == 0:
        max_rectangles = max(max_rectangles, depth_first_search(row_index + 1, next_row_bitmask | 0b0110) + 1)
    if (combined_state & 0b1100) == 0:
        max_rectangles = max(max_rectangles, depth_first_search(row_index + 1, next_row_bitmask | 0b1100) + 1)
    if (combined_state & 0b1111) == 0:
        max_rectangles = max(max_rectangles, depth_first_search(row_index + 1, 0b1111) + 2)
    
    memoization_table[row_index][current_state] = max_rectangles
    return max_rectangles

print(depth_first_search(0, position_bitmasks[0]))