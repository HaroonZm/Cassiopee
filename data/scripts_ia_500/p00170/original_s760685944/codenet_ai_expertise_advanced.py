from sys import stdin
from collections import namedtuple
input = stdin.readline
item = namedtuple('item', ['name', 'w', 's'])

def main():
    while (n := int(input())):
        items = [item(*line.split()[0:1], int(line.split()[1]), int(line.split()[2])) for line in (input() for _ in range(n))]
        items.sort(key=lambda it: it.w, reverse=True)
        ans = []
        total_weight = sum(it.w for it in items)
        while items:
            for i, it in enumerate(items):
                if it.s >= total_weight - it.w:
                    ans.append(it.name)
                    total_weight -= it.w
                    items.pop(i)
                    break
        print('\n'.join(ans))

if __name__ == '__main__':
    main()