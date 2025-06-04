import sys
import copy

def find_matches(board):
    remove = [[False]*5 for _ in range(5)]
    for i in range(5):
        count = 1
        for j in range(1,5):
            if board[i][j] != 0 and board[i][j] == board[i][j-1]:
                count += 1
            else:
                if count >= 3:
                    for k in range(j-count, j):
                        remove[i][k] = True
                count = 1
        if count >= 3:
            for k in range(5-count, 5):
                remove[i][k] = True

    for j in range(5):
        count = 1
        for i in range(1,5):
            if board[i][j] != 0 and board[i][j] == board[i-1][j]:
                count += 1
            else:
                if count >= 3:
                    for k in range(i-count, i):
                        remove[k][j] = True
                count = 1
        if count >= 3:
            for k in range(5-count, 5):
                remove[k][j] = True
    return remove

def apply_gravity(board):
    for j in range(5):
        stack = []
        for i in range(4,-1,-1):
            if board[i][j] != 0:
                stack.append(board[i][j])
        for i in range(5):
            if i < len(stack):
                board[4-i][j] = stack[i]
            else:
                board[4-i][j] = 0

def calc_score_and_remove(board, scores, bonus):
    remove = find_matches(board)
    matched = False
    total = 0
    for i in range(5):
        for j in range(5):
            if remove[i][j]:
                matched = True
                total += scores[board[i][j]-1]*bonus
                board[i][j] = 0
    return matched, total

def move_blocks(board, r1, c1, r2, c2):
    b = copy.deepcopy(board)
    b[r1][c1], b[r2][c2] = b[r2][c2], b[r1][c1]
    return b

def dfs(board, scores, n, pos, moves_left, bonus):
    if moves_left == 0:
        # calculate final score after matches, chain reactions
        b = copy.deepcopy(board)
        total_score = 0
        cur_bonus = bonus
        while True:
            matched, sc = calc_score_and_remove(b, scores, cur_bonus)
            if not matched:
                break
            total_score += sc
            apply_gravity(b)
            cur_bonus += 1
        return total_score

    max_score = 0
    r, c = pos
    directions = [(-1,0),(1,0),(0,-1),(0,1)]
    for dr, dc in directions:
        nr, nc = r+dr, c+dc
        if 0 <= nr < 5 and 0 <= nc < 5:
            new_board = move_blocks(board, r, c, nr, nc)
            # after move, check matches and chain reactions
            b = copy.deepcopy(new_board)
            total_score = 0
            cur_bonus = bonus
            while True:
                matched, sc = calc_score_and_remove(b, scores, cur_bonus)
                if not matched:
                    break
                total_score += sc
                apply_gravity(b)
                cur_bonus += 1
            next_score = total_score + dfs(b, scores, n, (nr,nc), moves_left-1, cur_bonus)
            if next_score > max_score:
                max_score = next_score
    # also consider not moving further
    # finalize score with current board and bonus
    # but that would be counted in dfs with moves_left=0, so skip here to avoid double counting
    return max_score

def solve_dataset(n, board, scores):
    max_total = 0
    if n == 0:
        # no moves, just remove matches if any and chain
        b = copy.deepcopy(board)
        total_score = 0
        bonus = 1
        while True:
            matched, sc = calc_score_and_remove(b, scores, bonus)
            if not matched:
                break
            total_score += sc
            apply_gravity(b)
            bonus += 1
        return total_score

    for r in range(5):
        for c in range(5):
            score = dfs(board, scores, n, (r,c), n, 1)
            if score > max_total:
                max_total = score
    return max_total

def main():
    input_lines = sys.stdin.read().splitlines()
    idx = 0
    while True:
        if idx >= len(input_lines):
            break
        n = int(input_lines[idx])
        idx += 1
        if n == -1:
            break
        board = []
        for _ in range(5):
            row = list(map(int, input_lines[idx].split()))
            idx += 1
            board.append(row)
        scores = list(map(int, input_lines[idx].split()))
        idx += 1
        res = solve_dataset(n, board, scores)
        print(res)

if __name__ == "__main__":
    main()