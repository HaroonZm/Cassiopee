import sys

sys.setrecursionlimit(10 ** 6)

from bisect import *
from collections import *
from heapq import *

convert_str_to_zero_based_int = lambda string_value: int(string_value) - 1

print_2d_list = lambda list_2d: print(*list_2d, sep="\n")

def read_single_int():
    return int(sys.stdin.readline())

def read_single_str():
    return sys.stdin.readline()[:-1]

def read_multiple_ints():
    return map(int, sys.stdin.readline().split())

def read_multiple_zero_based_ints():
    return map(convert_str_to_zero_based_int, sys.stdin.readline().split())

def read_multiple_floats():
    return map(float, sys.stdin.readline().split())

def read_list_of_ints():
    return list(map(int, sys.stdin.readline().split()))

def read_list_of_zero_based_ints():
    return list(map(convert_str_to_zero_based_int, sys.stdin.readline().split()))

def read_list_of_floats():
    return list(map(float, sys.stdin.readline().split()))

def read_multiple_lists_of_ints(number_of_rows):
    return [read_list_of_ints() for _ in range(number_of_rows)]

four_direction_vectors = [
    (0, 1),
    (1, 0),
    (0, -1),
    (-1, 0)
]

def solve_passing_stones_problem():
    while True:
        total_players, initial_stones = read_multiple_ints()
        if total_players == 0:
            break

        current_player_index = 0
        stones_held_by_player = [0] * total_players
        stones_in_hand = initial_stones

        while True:
            if stones_in_hand:
                stones_held_by_player[current_player_index] += 1

                if stones_held_by_player[current_player_index] == initial_stones:
                    break

                stones_in_hand -= 1

            else:
                stones_in_hand += stones_held_by_player[current_player_index]
                stones_held_by_player[current_player_index] = 0

            current_player_index = (current_player_index + 1) % total_players

        print(current_player_index)

solve_passing_stones_problem()