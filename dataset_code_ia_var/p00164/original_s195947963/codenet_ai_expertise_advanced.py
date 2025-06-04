import sys
from itertools import cycle, islice

def main():
    for line in sys.stdin:
        n = int(line)
        if not n:
            break
        jiro_moves = cycle(map(int, next(sys.stdin).split()))
        ohajiki = 32
        while ohajiki > 0:
            rem = (ohajiki - 1) % 5
            if rem:
                ohajiki -= rem
                print(ohajiki)
            move = next(jiro_moves)
            ohajiki = max(0, ohajiki - move)
            print(ohajiki)

if __name__ == '__main__':
    main()