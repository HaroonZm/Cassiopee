import sys

sys.setrecursionlimit(10 ** 6)

def input_int(): return int(sys.stdin.readline())
def input_map(): return map(int, sys.stdin.readline().split())
def input_list(): return list(map(int, sys.stdin.readline().split()))
def input_list_of_lists(num_rows): return [input_list() for _ in range(num_rows)]
def input_str(): return sys.stdin.readline().rstrip()
def print_2d(lst): print(*lst, sep="\n")
def index_adj(x): return int(x) - 1

from collections import deque

def process_knapsack():
    item_count, capacity = input_map()
    dp_arr = [0] * (capacity + 1)
    for _ in range(item_count):
        value, weight, amount = input_map()
        for residue in range(weight):
            max_deque = deque()
            max_items = (capacity - residue) // weight + 1
            for idx in range(max_items):
                curr_index = idx * weight + residue
                adjusted_value = dp_arr[curr_index] - value * idx
                while max_deque and max_deque[-1][1] <= adjusted_value:
                    max_deque.pop()
                max_deque.append((idx, adjusted_value))
                dp_arr[curr_index] = max_deque[0][1] + value * idx
                if max_deque[0][0] == idx - amount:
                    max_deque.popleft()
    print(dp_arr[-1])

process_knapsack()