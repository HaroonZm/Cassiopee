from itertools import cycle, islice
from sys import stdin

INITIALIZE = 32

def process(input_count, get_list):
    ohajiki = INITIALIZE
    output = []
    cycler = cycle(get_list)
    while True:
        ohajiki -= (ohajiki - 1) % 5
        output.append(ohajiki)
        get_count = next(cycler)
        if get_count < ohajiki:
            ohajiki -= get_count
            output.append(ohajiki)
        else:
            output.append(0)
            break
    return output

it = iter(stdin)
while True:
    try:
        input_count = int(next(it))
    except StopIteration:
        break
    if input_count == 0:
        break
    get_list = list(map(int, next(it).split()))
    print('\n'.join(map(str, process(input_count, get_list))))