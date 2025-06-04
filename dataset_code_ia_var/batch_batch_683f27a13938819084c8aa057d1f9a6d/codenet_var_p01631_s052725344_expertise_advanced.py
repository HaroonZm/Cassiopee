import sys
from itertools import product
from functools import lru_cache

# Directions (8-way)
DIRECTIONS = [(*d,) for d in product((-1, 0, 1), repeat=2) if d != (0, 0)]
GRID_SIZE = 4

def parse_input():
    n = int(sys.stdin.readline())
    words = [line.split() for line in (sys.stdin.readline() for _ in range(n))]
    grid = [sys.stdin.readline().strip() for _ in range(GRID_SIZE)]
    W = int(sys.stdin.readline())
    return n, words, grid, W

# Preprocess positions by letter for quick lookup
def build_letter_positions(grid):
    from collections import defaultdict
    letter_pos = defaultdict(list)
    for y, row in enumerate(grid):
        for x, ch in enumerate(row):
            letter_pos[ch].append((y, x))
    return letter_pos

def count_word_paths(word, grid):
    @lru_cache(maxsize=None)
    def dfs(d, y, x, used):
        if d == len(word):
            return 1
        cnt = 0
        for dy, dx in DIRECTIONS:
            ny, nx = y + dy, x + dx
            if 0 <= ny < GRID_SIZE and 0 <= nx < GRID_SIZE:
                idx = ny * GRID_SIZE + nx
                if not (used & (1 << idx)) and grid[ny][nx] == word[d]:
                    cnt += dfs(d+1, ny, nx, used | (1 << idx))
        return cnt
    count = 0
    for y, x in ((y, x) for y in range(GRID_SIZE) for x in range(GRID_SIZE) if grid[y][x] == word[0]):
        used = 1 << (y*GRID_SIZE + x)
        count += dfs(1, y, x, used)
    return count

def main():
    n, word_data, grid, W = parse_input()
    lens = [len(word) for word, _ in word_data]
    values = [int(val) for _, val in word_data]
    counts = [count_word_paths(word, grid) for word, _ in word_data]

    dp = [0] * (W+1)
    for i in range(n):
        w, v, m = lens[i], values[i], counts[i]
        if w == 0 or m == 0: continue
        # Monotonic queue optimized bounded knapsack
        for r in range(w):
            deq, deqv = [], []
            for k, idx in enumerate(range(r, W+1, w)):
                val = dp[idx] - k * v
                while deq and deqv[-1] <= val:
                    deq.pop(); deqv.pop()
                deq.append(k); deqv.append(val)
                if deq[0] < k - m:
                    deq.pop(0); deqv.pop(0)
                dp[idx] = deqv[0] + k * v
    print(dp[W])

if __name__ == "__main__":
    main()