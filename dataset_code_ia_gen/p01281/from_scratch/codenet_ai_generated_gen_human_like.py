def count_tatami_placements(H, W):
    # Ensure H <= W for consistent handling
    if H > W:
        H, W = W, H

    # Each tatami covers 2 squares: 1x2 or 2x1
    if (H * W) % 2 == 1:
        return 0

    # DP approach with bitmask for rows
    from functools import lru_cache

    full = (1 << W) - 1  # all bits set for W columns

    @lru_cache(maxsize=None)
    def dfs(row, mask):
        # row: current row index
        # mask: occupancy of current row (bits set = occupied)
        if row == H:
            return 1 if mask == 0 else 0
        return search_row(row, mask, 0, 0)

    def search_row(row, mask, pos, next_mask):
        # Try to fill current row cells starting at 'pos' with tatamis
        # next_mask: occupancy for next row
        if pos == W:
            # move to next row
            return dfs(row + 1, next_mask)
        # If current cell occupied, skip
        if (mask & (1 << pos)) != 0:
            return search_row(row, mask, pos + 1, next_mask)

        res = 0
        # Try horizontal placement (current cell and next cell in the same row)
        if pos + 1 < W and (mask & (1 << (pos + 1))) == 0:
            res += search_row(row, mask, pos + 2, next_mask)
        # Try vertical placement (current cell and cell in next row)
        if row + 1 < H:
            # Mark cell in next row occupied by vertical tatami
            res += search_row(row, mask, pos + 1, next_mask | (1 << pos))
        return res

def main():
    while True:
        line = input().strip()
        if line == '':
            continue
        H, W = map(int, line.split())
        if H == 0 and W == 0:
            break
        print(count_tatami_placements(H, W))

if __name__ == "__main__":
    main()