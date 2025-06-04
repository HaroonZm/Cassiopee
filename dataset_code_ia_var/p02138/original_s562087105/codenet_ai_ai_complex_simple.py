from functools import reduce
from itertools import cycle, count, islice, accumulate

A, B = map(int, input().split())

def elaborate_play(A, B, gen_strat, cond_strat):
    def next_step(state, ab_flag):
        score_a, score_b, a, b, score = state
        if ab_flag:
            score_b -= a
            if score_b <= 0:
                return (score_a, score_b, a, b, score)
            score += 1
            if cond_strat[0](score_b, b, A, B):
                b = gen_strat[0](score_b, b, A, B)
            return (score_a, score_b, a, b, score)
        else:
            score_a -= b
            if score_a <= 0:
                return (score_a, score_b, a, b, score)
            score += 1
            if cond_strat[1](score_a, a, A, B):
                a = gen_strat[1](score_a, a, A, B)
            return (score_a, score_b, a, b, score)
    state = (A*2, B*2, A, B, 0)
    moves = cycle([True, False])
    for _ in count():
        prev = state
        flag = next(moves)
        new_state = next_step(state, flag)
        if prev == new_state or new_state[0] <= 0 or new_state[1] <= 0:
            break
        state = new_state
    # Add last move if one falls at 0
    if state[0] <= 0 or state[1] <= 0:
        state = new_state
    return state[4]

id_ = lambda x, *_: x
cond1 = (lambda x, b, *_: x < b, lambda x, a, *_: x < a)
gen1  = (lambda x, *_: x, lambda x, *_: x)

def cond2_b(x, b, A, B): return x < b and A < B or (x < b and A > B)
def cond2_a(x, a, A, B): return x < a and A > B or (x < a and A < B)
def gen2_b(x, b, A, B):
    if A < B: return x
    return (x+1)//2
def gen2_a(x, a, A, B):
    if A > B: return x
    return (x+1)//2

gen2 = (gen2_b, gen2_a)
cond2 = (cond2_b, cond2_a)

ans1 = elaborate_play(A, B, gen1, cond1)

ans2 = elaborate_play(A, B, gen2, cond2)

print(min(ans1, ans2))