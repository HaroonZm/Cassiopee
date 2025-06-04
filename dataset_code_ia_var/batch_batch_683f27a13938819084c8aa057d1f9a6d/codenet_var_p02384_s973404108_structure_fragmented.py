from enum import Enum
import sys
import math

BIG_NUM = 2000000000
MOD = 1000000007
EPS = 0.000000001

def create_default_numbers():
    return [i for i in range(6)]

def create_order_string():
    return 'NNNNWNNNWNNNENNNENNNWNNN'

def clone_list(lst):
    return [item for item in lst]

def set_dice_numbers(dice, n0, n1, n2, n3, n4, n5):
    dice.number[0] = n0
    dice.number[1] = n1
    dice.number[2] = n2
    dice.number[3] = n3
    dice.number[4] = n4
    dice.number[5] = n5

def initialize_dice_work(dice):
    for i in range(6):
        dice.work[i] = dice.number[i]

def roll_east(dice):
    set_dice_numbers(dice, dice.work[3], dice.work[1], dice.work[0], dice.work[5], dice.work[4], dice.work[2])

def roll_north(dice):
    set_dice_numbers(dice, dice.work[1], dice.work[5], dice.work[2], dice.work[3], dice.work[0], dice.work[4])

def roll_south(dice):
    set_dice_numbers(dice, dice.work[4], dice.work[0], dice.work[2], dice.work[3], dice.work[5], dice.work[1])

def roll_west(dice):
    set_dice_numbers(dice, dice.work[2], dice.work[1], dice.work[5], dice.work[0], dice.work[4], dice.work[3])

def roll_dice(dice, loc):
    initialize_dice_work(dice)
    if loc == 'E':
        roll_east(dice)
    elif loc == 'N':
        roll_north(dice)
    elif loc == 'S':
        roll_south(dice)
    elif loc == 'W':
        roll_west(dice)

def save_dice_numbers(dice):
    return clone_list(dice.number)

def restore_dice_numbers(dice, saved):
    for i in range(len(dice.number)):
        dice.number[i] = saved[i]

def dice_query(dice, top_num, front_num):
    saved = save_dice_numbers(dice)
    ret = -1
    for i in range(len(dice.order)):
        roll_dice(dice, dice.order[i])
        if dice.number[0] == top_num and dice.number[1] == front_num:
            ret = dice.number[2]
            break
    restore_dice_numbers(dice, saved)
    return ret

class Dice():
    def __init__(self):
        self.number = create_default_numbers()
        self.work = create_default_numbers()
        self.order = create_order_string()
    def setNumber(self, n0, n1, n2, n3, n4, n5):
        set_dice_numbers(self, n0, n1, n2, n3, n4, n5)
    def roll(self, loc):
        roll_dice(self, loc)
    def query(self, top_num, front_num):
        return dice_query(self, top_num, front_num)

def input_numbers():
    return list(map(int, input().split()))

def get_query_count():
    return int(input())

def input_query():
    return tuple(map(int, input().split()))

def handle_queries(dice, num_query):
    for _ in range(num_query):
        top_num, front_num = input_query()
        display_result(dice.query(top_num, front_num))

def display_result(result):
    print("%d" % (result))

def main():
    dice = Dice()
    table = input_numbers()
    dice.setNumber(table[0], table[1], table[2], table[3], table[4], table[5])
    num_query = get_query_count()
    handle_queries(dice, num_query)

main()