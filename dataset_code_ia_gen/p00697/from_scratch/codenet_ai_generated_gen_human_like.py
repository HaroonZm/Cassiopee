def rotate(piece):
    return piece[3] + piece[0] + piece[1] + piece[2]

def all_rotations(piece):
    rotations = [piece]
    for _ in range(3):
        piece = rotate(piece)
        rotations.append(piece)
    return rotations

def match(edge1, edge2):
    pairs = {'R':'r', 'G':'g', 'B':'b', 'W':'w'}
    return pairs.get(edge1) == edge2

def can_place(grid, pieces, used, pos, piece):
    r, c = divmod(pos, 3)
    # check top neighbor
    if r > 0:
        top_piece = grid[pos - 3]
        if not match(top_piece[2], piece[0]):
            return False
    # check left neighbor
    if c > 0:
        left_piece = grid[pos - 1]
        if not match(left_piece[1], piece[3]):
            return False
    return True

def solve(grid, pieces, used, pos):
    if pos == 9:
        return 1
    count = 0
    for i, rotations in enumerate(pieces):
        if used[i]:
            continue
        for piece in rotations:
            if can_place(grid, pieces, used, pos, piece):
                grid[pos] = piece
                used[i] = True
                count += solve(grid, pieces, used, pos + 1)
                used[i] = False
    return count

def main():
    import sys
    input = sys.stdin.readline
    N = int(input())
    for _ in range(N):
        line = input().strip()
        raw_pieces = line.split()
        pieces = []
        for p in raw_pieces:
            rotations = all_rotations(p)
            pieces.append(rotations)
        # no identical or rotationally equal pieces and no rotationally symmetric pieces by problem statement
        used = [False]*9
        grid = [None]*9
        result = solve(grid, pieces, used, 0)
        print(result)

if __name__ == "__main__":
    main()