def read_nm():
    return map(int, raw_input().split())

def should_continue(N):
    return N != 0

def read_triplet():
    return map(int, raw_input().split())

def read_ls(M):
    result = []
    for _ in range(M):
        t, s, d = read_triplet()
        result.append((t, s, d))
    return result

def sort_ls(ls):
    return sorted(ls)

def init_cnt(N):
    return [0, 1] + [0] * N

def update_cnt_entry(cnt, p):
    cnt[p[2]] = max(cnt[p[1]], cnt[p[2]])

def process_ls(ls, cnt):
    for p in ls:
        update_cnt_entry(cnt, p)

def sum_cnt(cnt):
    return sum(cnt)

def main_loop():
    while True:
        N, M = read_nm()
        if not should_continue(N):
            break
        ls = read_ls(M)
        sorted_ls = sort_ls(ls)
        cnt = init_cnt(N)
        process_ls(sorted_ls, cnt)
        print sum_cnt(cnt)

main_loop()