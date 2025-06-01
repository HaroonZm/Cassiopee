import sys
from sys import stdin
from itertools import cycle
input_line = stdin.readline

def compute_remainder_taro(ohajiki_count):
    return (ohajiki_count - 1) % 5

def main(args):
    while True:
        ohajiki_count = int(input_line())
        if ohajiki_count == 0:
            break

        jiro_moves_cycle = cycle([int(move) for move in input_line().split(' ')])

        while ohajiki_count > 0:
            ohajiki_count -= compute_remainder_taro(ohajiki_count)
            print(ohajiki_count)
            ohajiki_count -= next(jiro_moves_cycle)
            print(max(0, ohajiki_count))

if __name__ == '__main__':
    main(sys.argv[1:])