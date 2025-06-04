import os
import sys
import itertools
import math
from collections import Counter, defaultdict

class MainProcess(object):

    def __init__(self):
        pass

    def execute(self):
        while True:
            max_turns, num_obstacles = map(int, raw_input().split())
            if max_turns == 0 and num_obstacles == 0:
                break
            obstacle_positions = []
            for obstacle_index in range(num_obstacles):
                obstacle_x, obstacle_y = map(int, raw_input().split())
                obstacle_positions.append((obstacle_x, obstacle_y))
            start_x, start_y = map(int, raw_input().split())
            queue = [(start_x, start_y, 0)]
            visited_positions = set([(start_x, start_y)])
            movement_directions = [(1, 0), (1, 1), (0, 1), (-1, 0), (-1, -1), (0, -1)]
            while queue:
                current_x, current_y, current_turn = queue.pop(0)
                if current_turn >= max_turns:
                    break
                for delta_x, delta_y in movement_directions:
                    next_position = (current_x + delta_x, current_y + delta_y)
                    if next_position not in obstacle_positions and next_position not in visited_positions:
                        visited_positions.add(next_position)
                        queue.append((next_position[0], next_position[1], current_turn + 1))
            print len(visited_positions)
        return None

if __name__ == '__main__':
    main_process_instance = MainProcess()
    main_process_instance.execute()