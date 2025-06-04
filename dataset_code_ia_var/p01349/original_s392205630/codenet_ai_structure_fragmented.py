import copy

def read_input():
    H, W, n = map(int, raw_input().split())
    board = [list(raw_input()) for _ in xrange(H)][::-1]
    goal = [["."] * W for _ in xrange(H)]
    return H, W, n, board, goal

def swap_cells(A, h, w):
    A[h][w], A[h][w+1] = A[h][w+1], A[h][w]

def get_column_sequence(A, H, w):
    return "".join(A[h][w] for h in xrange(H)).replace(".","")

def fill_column(A, H, w, seq):
    seq += "." * (H - len(seq))
    for h in xrange(H):
        A[h][w] = seq[h]

def process_fall(A, H, W):
    for w in xrange(W):
        seq = get_column_sequence(A, H, w)
        fill_column(A, H, w, seq)

def create_banish_board(H, W):
    return [[0]*W for _ in xrange(H)]

def mark_banish_horizontal(A, B, H, W, n):
    for h in xrange(H):
        cnt = 1
        for w in xrange(1, W):
            if A[h][w] == A[h][w-1]:
                cnt += 1
            else:
                if cnt >= n and A[h][w-1] != ".":
                    for wi in xrange(w-cnt, w):
                        B[h][wi] = 1
                cnt = 1
        if cnt >= n and A[h][W-1] != ".":
            for wi in xrange(W-cnt, W):
                B[h][wi] = 1

def mark_banish_vertical(A, B, H, W, n):
    for w in xrange(W):
        cnt = 1
        for h in xrange(1, H):
            if A[h][w] == A[h-1][w]:
                cnt += 1
            else:
                if cnt >= n and A[h-1][w] != ".":
                    for hi in xrange(h-cnt, h):
                        B[hi][w] = 1
                cnt = 1
        if cnt >= n and A[H-1][w] != ".":
            for hi in xrange(H-cnt, H):
                B[hi][w] = 1

def process_banish(A, H, W, n):
    B = create_banish_board(H, W)
    mark_banish_horizontal(A, B, H, W, n)
    mark_banish_vertical(A, B, H, W, n)
    banished = False
    for h in xrange(H):
        for w in xrange(W):
            if B[h][w]:
                A[h][w] = "."
                banished = True
    return banished

def is_goal_reached(A, goal):
    return A == goal

def can_empty(A, hh, ww, H, W, n, goal):
    swap_cells(A, hh, ww)
    while True:
        process_fall(A, H, W)
        banished = process_banish(A, H, W, n)
        if not banished:
            return False
        if is_goal_reached(A, goal):
            return True

def try_swap_and_check(A, h, W, can_empty_func):
    for w in xrange(W-1):
        if A[h][w] == A[h][w+1]:
            continue
        if can_empty_func(copy.deepcopy(A), h, w):
            return True
    return False

def main():
    H, W, n, _A, goal = read_input()
    def can_empty_func(B, h, w):
        return can_empty(B, h, w, H, W, n, goal)
    ans = False
    for h in xrange(H):
        A = copy.deepcopy(_A)
        if try_swap_and_check(A, h, W, can_empty_func):
            ans = True
            break
    print "YES" if ans else "NO"

main()