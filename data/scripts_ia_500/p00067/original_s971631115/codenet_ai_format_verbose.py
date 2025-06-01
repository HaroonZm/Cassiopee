#!/usr/bin/env python

from __future__ import (division, absolute_import, print_function,
                        unicode_literals)
from sys import stdin

def count_distinct_connected_components(grid):
    
    current_label = 0
    labeled_components = set()
    
    for row_index in range(12):
        
        for column_index in range(12):
            
            if not grid[row_index][column_index]:
                continue
            
            elif row_index > 0 and grid[row_index - 1][column_index]:
                grid[row_index][column_index] = grid[row_index - 1][column_index]
            
            elif column_index > 0 and grid[row_index][column_index - 1]:
                grid[row_index][column_index] = grid[row_index][column_index - 1]
            
            else:
                current_label += 1
                labeled_components.add(current_label)
                grid[row_index][column_index] = current_label
        
        for column_index in range(10, -1, -1):
            if (grid[row_index][column_index] and
                grid[row_index][column_index + 1] and
                grid[row_index][column_index] != grid[row_index][column_index + 1]):
                
                labeled_components.discard(grid[row_index][column_index])
                grid[row_index][column_index] = grid[row_index][column_index + 1]
    
    return len(labeled_components)

input_line = '\n'

while input_line:
    
    input_grid = []
    
    for _ in range(12):
        input_line = stdin.readline().rstrip()
        input_grid.append([int(character) for character in input_line])
    
    print(count_distinct_connected_components(input_grid))
    
    input_line = stdin.readline()