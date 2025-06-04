import sys
from collections import defaultdict

sys.setrecursionlimit(1_000_000)

def dfs(x, y, symbol, land, w, h):
    stack = [(x, y)]
    owner_set = set()
    area = 0
    while stack:
        cx, cy = stack.pop()
        if land[cy][cx] != '.':
            if not land[cy][cx].isdigit():
                owner_set.add(land[cy][cx])
            continue
        land[cy][cx] = str(symbol)
        area += 1
        for nx, ny in ((cx+1, cy), (cx-1, cy), (cx, cy+1), (cx, cy-1)):
            if 0 <= nx < w and 0 <= ny < h:
                stack.append((nx, ny))
    return owner_set, area

def main():
    input_iter = iter(sys.stdin.read().split('\n'))
    while True:
        try:
            w, h = map(int, next(input_iter).split())
        except StopIteration:
            break
        if w == 0 and h == 0:
            break
        land = [list(next(input_iter)) for _ in range(h)]

        symbol = 0
        count_dict = defaultdict(int)

        for y, row in enumerate(land):
            for x, cell in enumerate(row):
                if cell == '.':
                    owners, area = dfs(x, y, symbol, land, w, h)
                    if len(owners) == 1:
                        count_dict[next(iter(owners))] += area
                    symbol += 1

        print(f"{count_dict['B']} {count_dict['W']}")

if __name__ == '__main__':
    main()