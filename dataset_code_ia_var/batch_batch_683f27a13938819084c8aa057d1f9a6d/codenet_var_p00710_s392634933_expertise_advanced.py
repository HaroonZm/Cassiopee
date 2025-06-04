from sys import stdin
from itertools import repeat, islice

def main():
    lines = iter(stdin.read().splitlines())
    while True:
        try:
            count, times = map(int, next(lines).split())
        except StopIteration:
            break
        if count == times == 0:
            break
        hanahuda = list(range(1, count + 1))
        for _ in range(times):
            p, c = map(int, next(lines).split())
            idx = count - (p + c)
            hanahuda.extend(islice((hanahuda.pop(idx + 1) for _ in repeat(None, c)), c))
        print(hanahuda.pop())
        
main()