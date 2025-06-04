from collections import defaultdict
from itertools import count

def main():
    n = int(raw_input())
    stacks = defaultdict(list)
    for i in xrange(n + 1):
        stacks[i]  # pre-populate

    ops = {
        'push': lambda s, idx, val: s[idx].append(val),
        'pop':  lambda s, idx: print(s[idx].pop()),
        'move': lambda s, src, dst: s[dst].append(s[src].pop())
    }

    for _ in count():
        line = raw_input().split()
        cmd, *args = line
        if cmd == 'quit':
            break
        elif cmd == 'push':
            ops[cmd](stacks, int(args[0]), args[1])
        elif cmd == 'pop':
            ops[cmd](stacks, int(args[0]))
        elif cmd == 'move':
            ops[cmd](stacks, int(args[0]), int(args[1]))

if __name__ == "__main__":
    main()