#!/usr/bin/env python3

from collections import defaultdict, deque
from heapq import heappush, heappop
import sys
import math
import bisect
import random

def read_int_list():
    return [int(x) for x in sys.stdin.readline().split()]

def read_single_int():
    return int(sys.stdin.readline())

def read_list_of_strings():
    return [list(x) for x in sys.stdin.readline().split()]

def read_single_string_as_list():
    return list(sys.stdin.readline())[:-1]

def read_n_single_ints(number_of_lines):
    return [read_single_int() for _ in range(number_of_lines)]

def read_n_int_lists(number_of_lines):
    return [read_int_list() for _ in range(number_of_lines)]

def read_n_single_string_lists(number_of_lines):
    return [read_single_string_as_list() for _ in range(number_of_lines)]

def read_n_lists_of_strings(number_of_lines):
    return [read_list_of_strings() for _ in range(number_of_lines)]

sys.setrecursionlimit(1000000)
MODULO = 1000000007

def solve(number_of_stations):

    station_times_and_positions = read_n_int_lists(number_of_stations)

    if station_times_and_positions[0][0] > station_times_and_positions[0][1]:
        print("NG 1")
        return

    minimum_steps_to_station_with_jump = [
        [float("inf") for jump_count in range(4)] 
        for station_index in range(number_of_stations)
    ]

    minimum_steps_to_station_with_jump[0][1] = station_times_and_positions[0][0]

    for current_station_index in range(number_of_stations - 1):

        next_station_index = current_station_index + 1

        current_position, current_time = station_times_and_positions[current_station_index]

        for current_jump_count in range(4):

            next_position, next_time = station_times_and_positions[next_station_index]

            # Attempt incrementing jump by 1, up to max 3 jumps
            if current_jump_count < 3:
                next_jump_count = current_jump_count + 1
                arrival_time_with_jump = current_time + next_jump_count * abs(next_position - current_position)
                if arrival_time_with_jump <= next_time:
                    total_distance = minimum_steps_to_station_with_jump[current_station_index][current_jump_count] + abs(next_position - current_position)
                    if total_distance < minimum_steps_to_station_with_jump[next_station_index][next_jump_count]:
                        minimum_steps_to_station_with_jump[next_station_index][next_jump_count] = total_distance

            # Try resetting jump count to 1
            next_jump_count = 1
            arrival_time_with_teleport = current_time + (current_jump_count + 1) * current_position + next_position
            if arrival_time_with_teleport > next_time:
                continue
            total_distance = minimum_steps_to_station_with_jump[current_station_index][current_jump_count] + next_position + current_position
            if total_distance < minimum_steps_to_station_with_jump[next_station_index][next_jump_count]:
                minimum_steps_to_station_with_jump[next_station_index][next_jump_count] = total_distance

    minimal_total_distance = float("inf")
    for jump_count in range(4):
        minimal_total_distance = min(
            minimal_total_distance,
            minimum_steps_to_station_with_jump[-1][jump_count] + station_times_and_positions[-1][0]
        )

    if minimal_total_distance == float("inf"):
        for station_index in range(number_of_stations):
            if min(minimum_steps_to_station_with_jump[station_index]) == float("inf"):
                print("NG", station_index + 1)
                return

    print("OK", minimal_total_distance)
    return

# Main execution loop
if __name__ == "__main__":
    while True:
        number_of_stations = read_single_int()
        if number_of_stations == 0:
            break
        solve(number_of_stations)