from bisect import bisect_left

def create_empty_last():
    return [[] for _ in range(26)]

def update_score_with_s(score, i, ti, s):
    return score + s[i][ti - 1]

def append_last_day(last, ti, i):
    last[ti - 1].append(i + 1)

def compute_penalty_for_type(last, tj, i, c):
    if last[tj - 1] == []:
        return -c[tj - 1] * (i + 1)
    else:
        return -c[tj - 1] * ((i + 1) - last[tj - 1][-1])

def update_score_with_c_and_last(score, last, i, c):
    for tj in range(26):
        score += compute_penalty_for_type(last, tj, i, c)
    return score

def print_score(score):
    print(score)

def process_single_day(score, last, i, ti, s, c):
    score = update_score_with_s(score, i, ti, s)
    append_last_day(last, ti, i)
    score = update_score_with_c_and_last(score, last, i, c)
    print_score(score)
    return score

def main_score_loop(t, s, c):
    score = 0
    last = create_empty_last()
    for i, ti in enumerate(t):
        score = process_single_day(score, last, i, ti, s, c)
    return score, last

def penalty_if_last_empty(lastti, i, ci):
    if lastti == []:
        return -ci * (i + 1)
    else:
        return -ci * ((i + 1) - lastti[-1])

def process_single_day2(score, last, i, ti, s, c):
    score += s[i][ti - 1]
    score += penalty_if_last_empty(last[ti - 1], i, c[i])
    append_last_day(last, ti, i)
    print_score(score)
    return score

def main_score_loop2(t, s, c):
    score = 0
    last = create_empty_last()
    for i, ti in enumerate(t):
        score = process_single_day2(score, last, i, ti, s, c)
    return score, last

def apply_end_penalties(score, last, c, D):
    for i in range(26):
        if last[i] == []:
            score -= c[i] * D
        else:
            score -= c[i] * (D - last[i][-1])
    return score

class score:
    def __init__(self, t) -> None:
        self.t = t
        self.score, _ = main_score_loop(t, s, c)
    def a__init__(self, t) -> None:
        score = 0
        last = create_empty_last()
        for i, ti in enumerate(t):
            score = process_single_day2(score, last, i, ti, s, c)
        score = apply_end_penalties(score, last, c, D)
        self.score = score
        self.t = t

def read_int():
    return int(input())

def read_int_list():
    return list(map(int, input().split()))

def read_matrix(D):
    return [list(map(int, input().split())) for _ in range(D)]

def read_t_list(D):
    return [int(input()) for _ in range(D)]

def main():
    global D, c, s, t
    D = read_int()
    c = read_int_list()
    s = read_matrix(D)
    t = read_t_list(D)
    sc = score(t)
    #print(sc.score)

main()