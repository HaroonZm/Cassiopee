import copy

def read_dimensions():
    return map(int, raw_input().split())

def read_board(H):
    return [list(raw_input()) for _ in xrange(H)][::-1]

def create_goal_board(H, W):
    return [["."] * W for _ in xrange(H)]

def get_column(A, w, H):
    return "".join(A[h][w] for h in xrange(H))

def fall_column(seq, H):
    seq = seq.replace(".", "")
    return seq + "." * (H - len(seq))

def update_board_with_fall(A, H, W):
    for w in xrange(W):
        seq = get_column(A, w, H)
        fallen = fall_column(seq, H)
        for h in xrange(H):
            A[h][w] = fallen[h]

def initialize_banish_matrix(H, W):
    return [[0] * W for _ in xrange(H)]

def process_row_for_banish(A, B, h, W, n):
    cnt = 1
    c = A[h][0]
    for w in xrange(1, W):
        if A[h][w] == c:
            cnt += 1
        else:
            if cnt >= n and c != ".":
                mark_row_banish(B, h, w, cnt)
            c, cnt = A[h][w], 1
    if cnt >= n and c != ".":
        mark_row_banish(B, h, W, cnt)

def mark_row_banish(B, h, w, cnt):
    for wi in xrange(w - cnt, w):
        B[h][wi] = 1

def process_rows_for_banish(A, B, H, W, n):
    for h in xrange(H):
        process_row_for_banish(A, B, h, W, n)

def process_col_for_banish(A, B, w, H, n):
    cnt = 1
    c = A[0][w]
    for h in xrange(1, H):
        if A[h][w] == c:
            cnt += 1
        else:
            if cnt >= n and c != ".":
                mark_col_banish(B, w, h, cnt)
            c, cnt = A[h][w], 1
    if cnt >= n and c != ".":
        mark_col_banish(B, w, H, cnt)

def mark_col_banish(B, w, h, cnt):
    for hi in xrange(h - cnt, h):
        B[hi][w] = 1

def process_cols_for_banish(A, B, H, W, n):
    for w in xrange(W):
        process_col_for_banish(A, B, w, H, n)

def banish_cells(A, B, H, W):
    banish = False
    for h in xrange(H):
        for w in xrange(W):
            if B[h][w]:
                A[h][w] = "."
                banish = True
    return banish

def equal_board(A, goal):
    return A == goal

def process_once(A, H, W, n):
    update_board_with_fall(A, H, W)
    B = initialize_banish_matrix(H, W)
    process_rows_for_banish(A, B, H, W, n)
    process_cols_for_banish(A, B, H, W, n)
    banished = banish_cells(A, B, H, W)
    return banished

def can_empty(A):
    while True:
        banished = process_once(A, H, W, n)
        if not banished:
            return False
        if equal_board(A, goal):
            return True

def swap_cells(A, h, w, ww):
    A[h][w], A[h][ww] = A[h][ww], A[h][w]

def try_all_swaps(_A, H, W, n, goal):
    for h in xrange(H):
        A = copy.deepcopy(_A)
        for w in xrange(W):
            if w < W - 1:
                if A[h][w] == A[h][w + 1]:
                    continue
                swap_cells(A, h, w, w + 1)
                if can_empty(copy.deepcopy(A)):
                    return True
                swap_cells(A, h, w, w + 1)
    return False

# Entry point
H, W, n = read_dimensions()
_A = read_board(H)
goal = create_goal_board(H, W)
ans = try_all_swaps(_A, H, W, n, goal)
print "YES" if ans else "NO"