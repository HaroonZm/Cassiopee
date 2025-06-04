from functools import partial

def step_shift(foot, nxt):
    (is_right, pos, cnt), update = foot, False
    cmp = (pos > nxt) if not is_right else (pos < nxt)
    foot[2] += cmp
    if not cmp:
        foot[0] ^= 1
    foot[1] = nxt
    return foot

s_loc = {1: -1, 4: -1, 7: -1, 2: 0, 8: 0, 3: 1, 6: 1, 9: 1}

try:
    while True:
        step = input()
        if step == "#":
            break
        moves = list(map(int, step))
        init = s_loc[moves[0]]
        foot_l = [False, init, 0]
        foot_r = [True, init, 0]
        for s in map(s_loc.__getitem__, moves[1:]):
            for foot in (foot_l, foot_r):
                step_shift(foot, s)
        print(min(foot_l[2], foot_r[2]))
except EOFError:
    pass