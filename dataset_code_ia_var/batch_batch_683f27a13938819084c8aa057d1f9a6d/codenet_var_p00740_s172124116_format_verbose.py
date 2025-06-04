import math
import string
import itertools
import fractions
import heapq
import collections
import re
import array
import bisect
import sys
import random
import time
import copy
import functools

sys.setrecursionlimit(10 ** 7)

INFINITE_VALUE = 10 ** 3
EPSILON = 1.0 / 10 ** 10
MODULO = 10 ** 9 + 7

def read_line_of_integers():
    return [int(value) for value in sys.stdin.readline().split()]

def read_line_of_integers_zero_based():
    return [int(value) - 1 for value in sys.stdin.readline().split()]

def read_line_of_floats():
    return [float(value) for value in sys.stdin.readline().split()]

def read_line_of_strings():
    return sys.stdin.readline().split()

def read_single_integer():
    return int(sys.stdin.readline())

def read_single_float():
    return float(sys.stdin.readline())

def read_input_string():
    return input()

def print_and_flush(output_string):
    print(output_string, flush=True)

def main():
    winning_player_indices = []

    while True:
        input_values = read_line_of_integers()
        number_of_players = input_values[0]
        initial_stones_count = input_values[1]
        maximum_stone_per_player = initial_stones_count

        if number_of_players == 0:
            break

        player_stones = [0] * number_of_players
        current_player_index = 0
        current_stones_in_pot = initial_stones_count

        while True:
            if current_stones_in_pot == 0:
                current_stones_in_pot = player_stones[current_player_index]
                player_stones[current_player_index] = 0
            else:
                player_stones[current_player_index] += 1
                current_stones_in_pot -= 1

                if player_stones[current_player_index] == maximum_stone_per_player:
                    break

            current_player_index = (current_player_index + 1) % number_of_players

        winning_player_indices.append(current_player_index)

    return '\n'.join(str(index) for index in winning_player_indices)

print(main())