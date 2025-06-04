import sys
sys.setrecursionlimit(10**7)

DIRECTIONS = [-5, 5, -1, 1, -6, 6, -4, 4]

def neighbors(i):
    r, c = divmod(i, 4)
    res = []
    # vertical and horizontal
    for dr, dc in [(-1,0),(1,0),(0,-1),(0,1)]:
        nr, nc = r+dr, c+dc
        if 0 <= nr < 5 and 0 <= nc < 4:
            res.append(nr*4+nc)
    # diagonal
    for dr, dc in [(-1,-1),(-1,1),(1,-1),(1,1)]:
        nr, nc = r+dr, c+dc
        if 0 <= nr < 5 and 0 <= nc < 4:
            res.append(nr*4+nc)
    return res

adjacent = [neighbors(i) for i in range(20)]

def compact(cards):
    new_cards = [c for c in cards if c != 0]
    new_cards += [0]*(20 - len(new_cards))
    return tuple(new_cards)

from functools import lru_cache

@lru_cache(None)
def dfs(cards):
    cards = compact(cards)
    # find pairs
    pairs = []
    for i in range(20):
        if cards[i]==0:
            continue
        for j in adjacent[i]:
            if j > i and cards[j] == cards[i]:
                pairs.append((i,j))
    if not pairs:
        return sum(1 for c in cards if c !=0)
    res = 20
    for i,j in pairs:
        lst = list(cards)
        lst[i] = 0
        lst[j] = 0
        res = min(res, dfs(tuple(lst)))
    return res

def main():
    input = sys.stdin.read().strip().split()
    n = int(input[0])
    idx = 1
    for _ in range(n):
        cards = tuple(int(x) for x in input[idx:idx+20])
        idx += 20
        print(dfs(cards))
    # no further input to process

if __name__ == "__main__":
    main()