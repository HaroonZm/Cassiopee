import copy

def swap_cells(A, y, x):
    A[y][x], A[y][x+1] = A[y][x+1], A[y][x]

def count_non_empty(A, W):
    return sum(W - row.count(".") for row in A)

def generate_column_sequence(A, w, H):
    seq = "".join(A[h][w] for h in range(H))
    return seq.replace(".", "")

def fill_column(A, seq, w, H):
    seq += "." * (H - len(seq))
    for h in range(H):
        A[h][w] = seq[h]

def fall_processing(A, W, H):
    for w in range(W):
        seq = generate_column_sequence(A, w, H)
        fill_column(A, seq, w, H)

def create_banish_board(W, H):
    return [[0]*W for _ in range(H)]

def mark_horizontal_banish(A, B, H, W, n):
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

def mark_vertical_banish(A, B, H, W, n):
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

def banish_tiles(A, B, H, W):
    banish = False
    num_removed = 0
    for h in range(H):
        for w in range(W):
            if B[h][w]:
                A[h][w] = "."
                num_removed += 1
                banish = True
    return banish, num_removed

def do_fall_and_banish(A, W, H, n, num):
    while True:
        fall_processing(A, W, H)
        B = create_banish_board(W, H)
        mark_horizontal_banish(A, B, H, W, n)
        mark_vertical_banish(A, B, H, W, n)
        banish, num_removed = banish_tiles(A, B, H, W)
        num -= num_removed
        if not banish:
            return False
        if num == 0:
            return True

def can_empty(A, y, x):
    swap_cells(A, y, x)
    num = count_non_empty(A, len(A[0]))
    return do_fall_and_banish(A, len(A[0]), len(A), n, num)

def parse_input():
    H, W, n = map(int, raw_input().split())
    A = [list(raw_input()) for _ in range(H)][::-1]
    return H, W, n, A

def test_one_swap(A, H, W):
    for h in range(H):
        for w in range(W-1):
            if A[h][w] == A[h][w+1]:
                continue
            if can_empty(copy.deepcopy(A), h, w):
                return True
    return False

def main():
    global H, W, n
    H, W, n, A = parse_input()
    ans = test_one_swap(A, H, W)
    print "YES" if ans else "NO"

main()