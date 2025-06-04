def rotate_90(grid):
    return [''.join(grid[7 - 1 - c][r] for c in range(7)) for r in range(7)]
def rotate_270(grid):
    return [''.join(grid[c][7 - 1 - r] for c in range(7)) for r in range(7)]
def flip_lr(grid):
    return [line[::-1] for line in grid]
def flip_ud(grid):
    return grid[::-1]
def parse_digit(grid):
    # All digits keys in normalized form (not rotated)
    digits = {
        1: ["#######",
            "#.....#",
            "#...|.#",
            "#.....#",
            "#...|.#",
            "#..-..#",
            "#######"],
        2: ["#######",
            "#..-..#",
            "#...|.#",
            "#..-..#",
            "#.|...#",
            "#..-..#",
            "#######"],
        3: ["#######",
            "#..-..#",
            "#...|.#",
            "#..-..#",
            "#...|.#",
            "#..-..#",
            "#######"],
        4: ["#######",
            "#.....#",
            "#.|.|.#",
            "#..-..#",
            "#...|.#",
            "#.....#",
            "#######"],
        5: ["#######",
            "#..-..#",
            "#.|...#",
            "#..-..#",
            "#...|.#",
            "#..-..#",
            "#######"],
        6: ["#######",
            "#..-..#",
            "#.|...#",
            "#..-..#",
            "#.|.|.#",
            "#..-..#",
            "#######"],
        7: ["#######",
            "#..-..#",
            "#...|.#",
            "#.....#",
            "#...|.#",
            "#.....#",
            "#######"],
        8: ["#######",
            "#..-..#",
            "#.|.|.#",
            "#..-..#",
            "#.|.|.#",
            "#..-..#",
            "#######"],
        9: ["#######",
            "#..-..#",
            "#.|.|.#",
            "#..-..#",
            "#...|.#",
            "#..-..#",
            "#######"]
    }
    # Try all digits with rotations due to orientation
    # The problem states '|' and '-' swap on rotation 90° or 270°
    def swap_pipe_minus(g):
        res = []
        for line in g:
            new_line = ''
            for ch in line:
                if ch == '|':
                    new_line += '-'
                elif ch == '-':
                    new_line += '|'
                else:
                    new_line += ch
            res.append(new_line)
        return res
    for d, pattern in digits.items():
        # direct compare
        if grid == pattern:
            return d
        # flip_lr + rotate_ccw90
        # The input digits are flipped LR, then possibly rotated CCW 90 or 270.
        # We reverse transform the input digit by applying transformations
        # so matching is direct.
    return None
def norm_digit(grid):
    # Try to inverse the transformations:
    # The transformations are
    # 0: flip_lr
    # 1: flip_lr + rotate_90_ccw = flip_lr + rotate_270_cw
    # 2: flip_lr
    # 3: flip_lr + rotate_270_ccw = flip_lr + rotate_90_cw
    # 4: flip_lr
    # 5: flip_ud + flip_lr
    # But digits could be transformed by these in any of the 6 faces
    # So try all to identify digit
    # The problem states digit is transformed by
    # transformation number:
    # 0: flip_lr
    # 1: flip_lr then rotate 90 ccw (i.e. 270 cw)
    # 2: flip_lr
    # 3: flip_lr then rotate 270 ccw (i.e. 90 cw)
    # 4: flip_lr
    # 5: flip_ud then flip_lr
    # So flipping LR always present, so first undo flip_lr, then check.
    candidates = []
    # Undo flip_lr
    g0 = flip_lr(grid)
    candidates.append(g0)
    # Undo flip_lr + rotate 90 cw (rotate 270 ccw)
    candidates.append(rotate_90(g0))
    # Undo flip_lr + rotate 270 cw (rotate 90 ccw)
    candidates.append(rotate_270(g0))
    # For 5: undo flip_ud + flip_lr -> flip_ud the original grid then flip_lr
    candidates.append(flip_ud(grid))
    # Also check original grid and flip_ud original grid as last resort
    candidates.append(grid)
    candidates.append(flip_ud(flip_lr(grid)))
    # Check for each candidate
    # Build digits dict for matching
    digits = {
        1: ["#######",
            "#.....#",
            "#...|.#",
            "#.....#",
            "#...|.#",
            "#..-..#",
            "#######"],
        2: ["#######",
            "#..-..#",
            "#...|.#",
            "#..-..#",
            "#.|...#",
            "#..-..#",
            "#######"],
        3: ["#######",
            "#..-..#",
            "#...|.#",
            "#..-..#",
            "#...|.#",
            "#..-..#",
            "#######"],
        4: ["#######",
            "#.....#",
            "#.|.|.#",
            "#..-..#",
            "#...|.#",
            "#.....#",
            "#######"],
        5: ["#######",
            "#..-..#",
            "#.|...#",
            "#..-..#",
            "#...|.#",
            "#..-..#",
            "#######"],
        6: ["#######",
            "#..-..#",
            "#.|...#",
            "#..-..#",
            "#.|.|.#",
            "#..-..#",
            "#######"],
        7: ["#######",
            "#..-..#",
            "#...|.#",
            "#.....#",
            "#...|.#",
            "#.....#",
            "#######"],
        8: ["#######",
            "#..-..#",
            "#.|.|.#",
            "#..-..#",
            "#.|.|.#",
            "#..-..#",
            "#######"],
        9: ["#######",
            "#..-..#",
            "#.|.|.#",
            "#..-..#",
            "#...|.#",
            "#..-..#",
            "#######"]
    }
    # On rotations 90 or 270, '|' and '-' swap roles, so prepare transformed digit patterns
    def swap_pm(pattern):
        res = []
        for line in pattern:
            new_line = ''
            for ch in line:
                if ch == '|':
                    new_line += '-'
                elif ch == '-':
                    new_line += '|'
                else:
                    new_line += ch
            res.append(new_line)
        return res
    # Patterns with swapped '|','-'
    digits_swapped = {d: swap_pm(p) for d, p in digits.items()}
    for candidate in candidates:
        for d in range(1,10):
            # Try direct match with original digit patterns
            if candidate == digits[d]:
                return d
            # Or match with swapped patterns
            if candidate == digits_swapped[d]:
                return d
    return None
def extract_faces(grid, offsets):
    faces = []
    for (r,c) in offsets:
        face = [grid[r+i][c:c+7] for i in range(7)]
        faces.append(face)
    return faces
def read_input():
    grids = []
    while True:
        lines = []
        for _ in range(21):
            line = input()
            if line == '0':
                return grids
            lines.append(line)
        grids.append(lines)
def main():
    face_offsets_player = [(0,0),(7,0),(7,7),(7,14),(7,21),(14,7)]
    face_offsets_dealer = [(0,36),(7,29),(7,36),(7,43),(7,50),(14,36)]
    grids = []
    while True:
        try:
            lines = [input() for _ in range(21)]
        except EOFError:
            break
        if lines[0]=='0':
            break
        grids.append(lines)
    for grid in grids:
        # extract player and dealer faces
        p_faces = extract_faces([line[:28] for line in grid], face_offsets_player)
        d_faces = extract_faces([line[29:] for line in grid], face_offsets_dealer)
        p_nums = [norm_digit(face) for face in p_faces]
        d_nums = [norm_digit(face) for face in d_faces]
        # Sum their probabilities: dice faces appear with equal probability
        total_p = len(p_nums)
        total_d = len(d_nums)
        # Compute probability player > dealer and player < dealer
        cnt_high = 0
        cnt_low = 0
        for pv in p_nums:
            for dv in d_nums:
                if pv > dv:
                    cnt_high += 1
                elif pv < dv:
                    cnt_low += 1
        # We ignore equal case according to problem
        # Compare probabilities
        if cnt_high*total_d >= cnt_low*total_p:
            print("HIGH")
        else:
            print("LOW")
if __name__=="__main__":
    main()