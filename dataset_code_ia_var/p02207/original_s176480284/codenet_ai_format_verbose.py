from itertools import product, permutations, combinations, combinations_with_replacement, accumulate
from bisect import bisect_left, bisect_right, insort, insort_left, insort_right
from math import log10, pow
from collections import deque, defaultdict, Counter, namedtuple
from heapq import heapify, heappush, heappop, nlargest, nsmallest
from random import randint, randrange, random, shuffle, choice, seed
import sys

# Augmentation de la limite de récursion pour la compatibilité avec de grandes profondeurs
sys.setrecursionlimit(10 ** 6)

# Fonctions de conversion et de lecture d'entrées
convert_index_to_zero_based = lambda x: int(x) - 1

def print_2D_list(list_2d):
    print(*list_2d, sep="\n")

def read_integer():
    return int(sys.stdin.readline())

def read_integers():
    return map(int, sys.stdin.readline().split())

def read_zero_based_integers():
    return map(convert_index_to_zero_based, sys.stdin.readline().split())

def read_floats():
    return map(float, sys.stdin.readline().split())

def read_integer_list():
    return list(map(int, sys.stdin.readline().split()))

def read_zero_based_integer_list():
    return list(map(convert_index_to_zero_based, sys.stdin.readline().split()))

def read_float_list():
    return list(map(float, sys.stdin.readline().split()))

def read_list_of_integer_lists(number_of_rows):
    return [read_integer_list() for _ in range(number_of_rows)]

# Déplacements (vecteurs de directions pour une grille)
cardinal_directions = [
    (1, 0),   # Bas
    (0, 1),   # Droite
    (-1, 0),  # Haut
    (0, -1)   # Gauche
]

def main():
    number_of_rows = read_integer()
    
    time_stamps_list = []
    reduction_factor_list = []
    
    for _ in range(number_of_rows):
        current_time_stamp, current_reduction_value = read_integers()
        
        time_stamps_list.append(current_time_stamp)
        
        reduction_log_value = log10(10 - current_reduction_value) - 1
        reduction_factor_list.append(reduction_log_value)
    
    prefix_sums_of_reduction_factors = [0]
    for reduction_value in reduction_factor_list:
        new_sum = prefix_sums_of_reduction_factors[-1] + reduction_value
        prefix_sums_of_reduction_factors.append(new_sum)
    
    number_of_queries = read_integer()
    for _ in range(number_of_queries):
        query_left_bound, query_right_bound = read_integers()
        
        left_index = bisect_left(time_stamps_list, query_left_bound)
        right_index = bisect_left(time_stamps_list, query_right_bound)
        
        exponent_value = prefix_sums_of_reduction_factors[right_index] - prefix_sums_of_reduction_factors[left_index] + 9
        result_value = pow(10, exponent_value)
        
        print(result_value)

main()