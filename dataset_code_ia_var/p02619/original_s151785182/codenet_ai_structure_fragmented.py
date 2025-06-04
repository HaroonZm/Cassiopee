import sys
from typing import NamedTuple, List

class Game(NamedTuple):
    c: List[int]
    s: List[List[int]]

def parse_input():
    tokens = iterate_tokens()
    D = read_D(tokens)
    c = read_c(tokens)
    s = read_s(tokens, D)
    t = read_t(tokens, D)
    return D, c, s, t

def iterate_tokens():
    for line in sys.stdin:
        for word in line.split():
            yield word

def read_D(tokens):
    return int(next(tokens))

def read_c(tokens):
    return [int(next(tokens)) for _ in range(26)]

def read_s(tokens, D):
    return [[int(next(tokens)) for _ in range(26)] for _ in range(D)]

def read_t(tokens, D):
    return [int(next(tokens)) for _ in range(D)]

def solve(D: int, c: "List[int]", s: "List[List[int]]", t: "List[int]"):
    initial_ans = [0]
    initial_lasts = [0] * 26
    initial_adjust = 0
    sum_c = compute_sum_c(c)
    daily_loss = sum_c
    for day, tt in enumerate_t_days(t):
        a = compute_s_for_the_day(s, day, tt)
        adjust = update_adjust(initial_adjust, day, c, tt, initial_lasts)
        initial_lasts = update_lasts(initial_lasts, tt, day)
        a = update_a_with_losses_and_adjust(a, daily_loss, adjust)
        initial_ans = append_ans(initial_ans, a)
        daily_loss = update_daily_loss(daily_loss, sum_c)
        initial_adjust = adjust
    return slice_ans(initial_ans)

def compute_sum_c(c):
    return sum(c)

def enumerate_t_days(t):
    return enumerate(t, 1)

def compute_s_for_the_day(s, day, tt):
    return s[day-1][tt-1]

def update_adjust(current_adjust, day, c, tt, lasts):
    return current_adjust + day * c[tt-1] - lasts[tt-1] * c[tt-1]

def update_lasts(lasts, tt, day):
    new_lasts = lasts.copy()
    new_lasts[tt-1] = day
    return new_lasts

def update_a_with_losses_and_adjust(a, daily_loss, adjust):
    return a - daily_loss + adjust

def append_ans(ans, a):
    return ans + [ans[-1] + a]

def update_daily_loss(daily_loss, sum_c):
    return daily_loss + sum_c

def slice_ans(ans):
    return ans[1:]

def print_result(result):
    for line in result:
        print(line)

def main():
    D, c, s, t = parse_input()
    result = solve(D, c, s, t)
    print_result(result)

def test():
    import doctest
    doctest.testmod()

if __name__ == '__main__':
    #test()
    main()