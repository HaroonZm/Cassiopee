import sys

import math
import collections
import bisect
import itertools
import fractions
import copy
import heapq
import decimal
import queue

sys.setrecursionlimit(10000001)

INFINITY = 10 ** 16
MODULO = 10 ** 9 + 7

read_single_integer = lambda: int(sys.stdin.readline())
read_two_integers = lambda: map(int, sys.stdin.readline().split())
read_integer_list = lambda: list(map(int, sys.stdin.readline().split()))

def main():
    total_weapons, monster_health = read_two_integers()
    
    weapon_attack_powers = []
    special_attack_powers = []
    
    for weapon_index in range(total_weapons):
        normal_attack_power, special_attack_power = read_two_integers()
        weapon_attack_powers.append((normal_attack_power, weapon_index))
        special_attack_powers.append((special_attack_power, weapon_index))
    
    weapon_attack_powers.sort(key=lambda pair: pair[0], reverse=True)
    special_attack_powers.sort(key=lambda pair: pair[0], reverse=True)
    
    maximum_attack_power = weapon_attack_powers[0][0]
    index_of_strongest_weapon = weapon_attack_powers[0][1]
    
    sum_special_attacks_used = 0
    number_of_special_attacks_used = 0
    
    for weapon_index in range(total_weapons):
        if special_attack_powers[weapon_index][0] > maximum_attack_power:
            number_of_special_attacks_used += 1
            sum_special_attacks_used += special_attack_powers[weapon_index][0]
    
    total_attacks_needed = 0
    
    if sum_special_attacks_used <= monster_health:
        remaining_health = monster_health - sum_special_attacks_used
        attacks_needed_with_strongest_weapon = (remaining_health + maximum_attack_power - 1) // maximum_attack_power
        total_attacks_needed += attacks_needed_with_strongest_weapon
        total_attacks_needed += number_of_special_attacks_used
    else:
        current_remaining_health = monster_health
        for weapon_index in range(total_weapons):
            current_remaining_health -= special_attack_powers[weapon_index][0]
            total_attacks_needed += 1
            if current_remaining_health <= 0:
                break
    
    print(total_attacks_needed)

if __name__ == '__main__':
    main()