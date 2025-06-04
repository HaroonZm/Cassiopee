from collections import defaultdict
from sys import stdin

def main():
    n = int(input())
    stacks = defaultdict(list)
    for i in range(1, n + 1):
        stacks[i] = []
    for line in map(str.strip, stdin):
        if not line:
            continue
        cmd, *args = line.split()
        if cmd == 'quit':
            break
        match cmd, args:
            case 'push', [idx, val]:
                stacks[int(idx)].append(val)
            case 'move', [src, dst]:
                stacks[int(dst)].append(stacks[int(src)].pop())
            case 'pop', [idx]:
                print(stacks[int(idx)].pop())

if __name__ == "__main__":
    main()