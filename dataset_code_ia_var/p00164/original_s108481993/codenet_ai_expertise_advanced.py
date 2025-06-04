from itertools import cycle
from sys import stdin

INITIALIZE = 32

lines = iter(stdin.read().splitlines())
for input_count_str in lines:
    input_count = int(input_count_str)
    if input_count == 0:
        break
    get_list = list(map(int, next(lines).split()))
    ohajiki = INITIALIZE
    for get_count in cycle(get_list):
        ohajiki -= (ohajiki - 1) % 5
        print(ohajiki)
        if get_count < ohajiki:
            ohajiki -= get_count
            print(ohajiki)
        else:
            print(0)
            break