import sys
import math
import bisect
import random
from collections import defaultdict, deque
from heapq import heappush, heappop

def read_int_list(): return [int(token) for token in sys.stdin.readline().split()]
def read_int(): return int(sys.stdin.readline())
def read_str_list(): return [list(token) for token in sys.stdin.readline().split()]
def read_char_list():
    res = list(sys.stdin.readline())
    if res and res[-1] == "\n":
        return res[:-1]
    return res
def read_int_lines(line_count):
    return [read_int() for _ in range(line_count)]
def read_int_list_lines(line_count):
    return [read_int_list() for _ in range(line_count)]
def read_char_lines(line_count):
    return [read_char_list() for _ in range(line_count)]
def read_str_list_lines(line_count):
    return [read_str_list() for _ in range(line_count)]

sys.setrecursionlimit(1000000)
MODULO = 1000000007

def solve_A():
    num_x, num_y = read_int_list()
    if num_x < 0:
        if num_y < 0:
            if num_x < num_y:
                print(num_y - num_x)
            else:
                print(num_x - num_y + 2)
        else:
            if abs(num_x) < num_y:
                print(num_y - abs(num_x) + 1)
            else:
                print(-num_y - num_x + (num_y > 0))
    else:
        if num_y < 0:
            if num_x < abs(num_y):
                print(abs(num_y) - num_x + 1)
            else:
                print(num_x + num_y + 1)
        else:
            if num_x < num_y:
                print(num_y - num_x)
            else:
                print(num_x - num_y + (num_x > 0) + (num_y > 0))

def solve_B():
    return

def solve_C():
    values = read_int_list()
    if values[0] > 0 and values[3] > 0 and values[4] > 0:
        res1 = 2 * (values[0] // 2) + values[1] + 2 * (values[3] // 2) + 2 * (values[4] // 2)
        res2 = 2 * ((values[0] - 1) // 2) + values[1] + 2 * ((values[3] - 1) // 2) + 2 * ((values[4] - 1) // 2) + 3
        print(max(res1, res2))
    else:
        res = 2 * (values[0] // 2) + values[1] + 2 * (values[3] // 2) + 2 * (values[4] // 2)
        print(res)
    return

def solve_D():
    list_n = read_int()
    list_x = read_int_list()
    indexed_pairs = [(list_x[index], index) for index in range(list_n)]
    indexed_pairs.sort()
    temp_list = []
    for num_val, idx in indexed_pairs:
        temp_list += [idx + 1] * idx
    for num_val, idx in indexed_pairs:
        temp_list += [idx + 1] * (list_n - idx - 1)
    result_list = []
    temp_index = 0
    for num_val, idx in indexed_pairs:
        while len(result_list) + 1 < num_val:
            if temp_index == len(temp_list):
                break
            result_list.append(temp_list[temp_index])
            temp_index += 1
        result_list.append(idx + 1)
    for idx in range(temp_index, len(temp_list)):
        result_list.append(temp_list[idx])
    count_list = [0] * list_n
    for idx in range(len(result_list)):
        current_index = result_list[idx] - 1
        if count_list[current_index] == current_index:
            if idx + 1 != list_x[current_index]:
                print("No")
                return
        count_list[current_index] += 1
    print("Yes")
    print(*result_list)
    return

def solve_E():
    return

def solve_F():
    return

if __name__ == "__main__":
    solve_D()