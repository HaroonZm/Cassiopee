import sys

from operator import methodcaller, itemgetter

_ = input()
s = set()

for line in map(str.split, sys.stdin):
    match line:
        case ['0', x]:
            s.add(x := int(x))
            print(len(s))
        case ['1', x]:
            print(int((x := int(x)) in s))
        case ['2', x]:
            s.discard(int(x))
        case [_, left, right]:
            l, r = map(int, (left, right))
            rng = r - l + 1
            if len(s) > rng:
                print(*(i for i in range(l, r + 1) if i in s), sep='\n')
            else:
                print(*sorted(filter(lambda v: l <= v <= r, s)), sep='\n')