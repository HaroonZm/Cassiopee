import copy

def swap_cells_in_row(A, y, x):
    A[y][x], A[y][x+1] = A[y][x+1], A[y][x]

def get_non_empty_cell_count(A, W):
    num = 0
    for a in A:
        num += W - a.count(".")
    return num

def get_column_sequence(A, h, w):
    return "".join(A[h][w] for h in range(H))

def compress_column(seq, H):
    seq = seq.replace(".", "")
    seq += "." * (H - len(seq))
    return seq

def apply_fall(A, H, W):
    for w in range(W):
        col_seq = "".join(A[h][w] for h in range(H))
        col_seq = compress_column(col_seq, H)
        for h in range(H):
            A[h][w] = col_seq[h]

def create_banish_board(H, W):
    return [[0]*W for _ in range(H)]

def mark_banish_horizontal(A, B, H, W, n):
    for h in range(H):
        cnt = 1
        for w in range(1, W):
            if A[h][w] == A[h][w-1]:
                cnt += 1
            else:
                if cnt >= n and A[h][w-1] != ".":
                    for wi in range(w-cnt, w):
                        B[h][wi] = 1
                cnt = 1
        if cnt >= n and A[h][W-1] != ".":
            for wi in range(W-cnt, W):
                B[h][wi] = 1

def mark_banish_vertical(A, B, H, W, n):
    for w in range(W):
        cnt = 1
        for h in range(1, H):
            if A[h][w] == A[h-1][w]:
                cnt += 1
            else:
                if cnt >= n and A[h-1][w] != ".":
                    for hi in range(h-cnt, h):
                        B[hi][w] = 1
                cnt = 1
        if cnt >= n and A[H-1][w] != ".":
            for hi in range(H-cnt, H):
                B[hi][w] = 1

def any_banish(B, H, W):
    for h in range(H):
        for w in range(W):
            if B[h][w]:
                return True
    return False

def process_banish(A, B, H, W, num):
    banished_any = False
    for h in range(H):
        for w in range(W):
            if B[h][w]:
                A[h][w] = "."
                num -= 1
                banished_any = True
    return num, banished_any

def board_is_empty(num):
    return num == 0

def process_fall_and_banish(A, H, W, n, num):
    while True:
        apply_fall(A, H, W)
        B = create_banish_board(H, W)
        mark_banish_horizontal(A, B, H, W, n)
        mark_banish_vertical(A, B, H, W, n)
        num, banished_any = process_banish(A, B, H, W, num)
        if not banished_any:
            return False
        if board_is_empty(num):
            return True

def can_empty(A, y, x):
    swap_cells_in_row(A, y, x)
    num = get_non_empty_cell_count(A, W)
    return process_fall_and_banish(A, H, W, n, num)

def get_input():
    return map(int, raw_input().split())

def get_board(H):
    return [list(raw_input()) for _ in range(H)][::-1]

def get_empty_goal(H, W):
    return [["."] * W for _ in range(H)]

def try_all_moves(A, H, W, n):
    for h in range(H):
        for w in range(W-1):
            if A[h][w] == A[h][w+1]:
                continue
            if can_empty(copy.deepcopy(A), h, w):
                return True
    return False

def print_result(ans):
    print "YES" if ans else "NO"

# Entry point
H, W, n = get_input()
A = get_board(H)
goal = get_empty_goal(H, W)
ans = try_all_moves(A, H, W, n)
print_result(ans)