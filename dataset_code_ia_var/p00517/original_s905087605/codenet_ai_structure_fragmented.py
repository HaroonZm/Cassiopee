def read_values():
    return list(map(int, input().split()))

def initialize_variables():
    a, b, n = read_values()
    w, h = read_values()
    return a, b, n, w, h

def should_use_sum(h, mh, w, mw):
    return (h < mh and w > mw) or (h > mh and w < mw)

def calculate_difference_sum(h, mh, w, mw):
    return abs(mh - h) + abs(mw - w)

def calculate_difference_max(h, mh, w, mw):
    return max(abs(h - mh), abs(w - mw))

def process_single_move(cnt, w, h):
    mw, mh = read_values()
    if should_use_sum(h, mh, w, mw):
        cnt += calculate_difference_sum(h, mh, w, mw)
    else:
        cnt += calculate_difference_max(h, mh, w, mw)
    return cnt, mw, mh

def process_all_moves(n, w, h):
    cnt = 0
    for _ in range(1, n):
        cnt, w, h = process_single_move(cnt, w, h)
    return cnt

def main():
    a, b, n, w, h = initialize_variables()
    cnt = process_all_moves(n, w, h)
    print(cnt)

main()