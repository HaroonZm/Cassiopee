import sys

sys.setrecursionlimit(10 ** 7)

total_number_of_items, required_minimum_number = map(int, input().split())

if total_number_of_items <= required_minimum_number:
    print(1)
else:
    print(0)